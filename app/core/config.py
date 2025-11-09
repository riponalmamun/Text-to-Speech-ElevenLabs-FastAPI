from pydantic import BaseModel
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

class Settings(BaseModel):
    # -------------------------
    # Server Configuration
    # -------------------------
    app_name: str = os.getenv("APP_NAME", "TTS API")
    app_env: str = os.getenv("APP_ENV", "dev")
    debug: bool = os.getenv("APP_DEBUG", "true").lower() == "true"
    host: str = os.getenv("APP_HOST", "0.0.0.0")
    port: int = int(os.getenv("APP_PORT", "8000"))

    # -------------------------
    # TTS Provider
    # -------------------------
    tts_provider: str = os.getenv("TTS_PROVIDER", "elevenlabs")

    # -------------------------
    # OpenAI TTS Configuration
    # -------------------------
    openai_api_key: str | None = os.getenv("OPENAI_API_KEY")
    openai_tts_model: str = os.getenv("OPENAI_TTS_MODEL", "gpt-4o-mini-tts")
    openai_tts_voice: str = os.getenv("OPENAI_TTS_VOICE", "alloy")
    openai_tts_format: str = os.getenv("OPENAI_TTS_FORMAT", "mp3")

    # -------------------------
    # ElevenLabs Configuration
    # -------------------------
    eleven_api_key: str | None = os.getenv("ELEVEN_API_KEY")
    eleven_voice_id: str | None = os.getenv("ELEVEN_VOICE_ID")
    eleven_model_id: str = os.getenv("ELEVEN_MODEL_ID", "eleven_multilingual_v2")
    eleven_output_format: str = os.getenv("ELEVEN_OUTPUT_FORMAT", "mp3_44100_128")

# Instantiate the global settings object
settings = Settings()
