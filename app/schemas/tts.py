from pydantic import BaseModel, Field
from typing import Optional, Literal

AudioFormat = Literal["mp3", "wav", "opus"]

class TTSRequest(BaseModel):
    text: str = Field(..., min_length=1)
    voice: Optional[str] = None
    format: Optional[AudioFormat] = None
    model: Optional[str] = None

class TTSResponse(BaseModel):
    provider: str
    model: str
    voice: str
    format: AudioFormat
