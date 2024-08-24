from typing import Tuple

from src.infra.gemini import TextGemini, AudioGemini
from src.infra.firebase import FirebaseAdapter
from src.service.conversation import ConversationService
from src.service.transcription import TranscriptionService
from src.repository.transcription import TranscriptionRepository

def bootstrap() -> tuple[ConversationService, TranscriptionService]:
    text_gemini = TextGemini()
    audio_gemini = AudioGemini()
    db = FirebaseAdapter()

    transcription_repo = TranscriptionRepository(db)
    
    conversation_service = ConversationService(
        user_id = None,
        gemini = text_gemini,
    )

    audio_service = TranscriptionService(
        user_id = None,
        transcription_repo = transcription_repo,
        gemini = audio_gemini,
    )

    return conversation_service, audio_service
