from typing import Tuple

from src.infra.gemini import TextGemini, AudioGemini
from src.service.conversation import ConversationService
from src.service.audio import AudioService

def bootstrap() -> tuple[ConversationService, AudioService]:
    text_gemini = TextGemini()
    audio_gemini = AudioGemini()
    
    conversation_service = ConversationService(
        user_id = None,
        gemini = text_gemini,
    )

    audio_service = AudioService(
        user_id = None,
        gemini = audio_gemini,
    )

    return conversation_service, audio_service
