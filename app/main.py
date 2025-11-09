from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.tts import router as tts_router
from app.core.config import settings

# Initialize FastAPI app
app = FastAPI(title=settings.app_name)

# Enable CORS (allowing frontend apps or local testing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # Allow all origins (frontend, local, etc.)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register the TTS routes
app.include_router(tts_router)

# Root route (basic info)
@app.get("/")
async def root():
    return {
        "app_name": settings.app_name,
        "environment": settings.app_env,
        "provider": settings.tts_provider,
        "model": settings.eleven_model_id,
        "voice_id": settings.eleven_voice_id,
        "output_format": settings.eleven_output_format,
    }

# Optional: health check endpoint
@app.get("/health")
async def health():
    return {"status": "ok", "message": "TTS API is running!"}
