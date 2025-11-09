from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse, FileResponse, JSONResponse
from app.schemas.tts import TTSRequest
from app.services.tts import TTSService
from app.core.config import settings
import tempfile
import os
from mutagen.mp3 import MP3

router = APIRouter(prefix="/api", tags=["tts"])

MIME_MAP = {
    "mp3": "audio/mpeg",
    "wav": "audio/wav",
    "opus": "audio/ogg",
}


@router.post("/tts", response_class=FileResponse)
async def tts(req: TTSRequest):
    """
    Generate and download an audio file (TTS) with duration info.
    """
    try:
        # Generate audio bytes
        audio, provider, model, voice = TTSService.synthesize_bytes(
            req.text, req.voice, req.format, req.model
        )
        fmt = (req.format or "mp3").lower()
        mime = MIME_MAP.get(fmt, "audio/mpeg")

        # Save temporarily to file
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=f".{fmt}")
        temp_file.write(audio)
        temp_file.close()

        # Calculate duration
        duration = 0
        if fmt == "mp3":
            try:
                duration = round(MP3(temp_file.name).info.length, 2)
            except Exception:
                pass

        # Return response with metadata
        headers = {"X-Audio-Duration": str(duration)}
        return FileResponse(
            temp_file.name,
            media_type=mime,
            filename=f"tts_output.{fmt}",
            headers=headers,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/tts/stream")
async def tts_stream(req: TTSRequest):
    """
    Stream TTS audio chunks progressively.
    """
    try:
        fmt = (req.format or "mp3").lower()
        mime = MIME_MAP.get(fmt, "audio/mpeg")

        def gen():
            for chunk in TTSService.synthesize_stream(req.text, req.voice, req.format, req.model):
                yield chunk

        return StreamingResponse(
            gen(),
            media_type=mime,
            headers={"Content-Disposition": f"inline; filename=tts_stream.{fmt}"},
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
