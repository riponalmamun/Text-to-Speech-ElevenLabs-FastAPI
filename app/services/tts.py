import requests
from app.core.config import settings


class TTSService:
    provider = "elevenlabs"

    @staticmethod
    def synthesize_bytes(text: str, voice: str | None = None, fmt: str | None = None, model: str | None = None):
        """Generate a full audio file from ElevenLabs API."""
        voice_id = voice or settings.eleven_voice_id
        model_id = model or settings.eleven_model_id

        url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
        headers = {
            "xi-api-key": settings.eleven_api_key,
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
        }
        payload = {
            "text": text,
            "model_id": model_id,
            "voice_settings": {"stability": 0.5, "similarity_boost": 0.75},
        }

        response = requests.post(url, headers=headers, json=payload)
        if response.status_code != 200:
            raise Exception(f"ElevenLabs Error: {response.text}")

        return response.content, "elevenlabs", model_id, voice_id

    @staticmethod
    def synthesize_stream(text: str, voice: str | None = None, fmt: str | None = None, model: str | None = None):
        """Stream TTS audio progressively from ElevenLabs."""
        voice_id = voice or settings.eleven_voice_id
        model_id = model or settings.eleven_model_id

        url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream"
        headers = {
            "xi-api-key": settings.eleven_api_key,
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
        }
        payload = {
            "text": text,
            "model_id": model_id,
            "voice_settings": {"stability": 0.5, "similarity_boost": 0.75},
        }

        with requests.post(url, headers=headers, json=payload, stream=True) as r:
            if r.status_code != 200:
                raise Exception(f"ElevenLabs Stream Error: {r.text}")
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    yield chunk
