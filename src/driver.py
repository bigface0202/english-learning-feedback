from typing import Tuple

from src.infra.gemini import TextGemini, AudioGemini
from src.infra.firebase import FirebaseAdapter
from src.service.conversation import ConversationService
from src.service.transcription import TranscriptionService
from src.repository.transcription import TranscriptionRepository
from src.repository.word_count import WordCountRepository

def bootstrap() -> Tuple[ConversationService, TranscriptionService]:
    text_gemini = TextGemini()
    audio_gemini = AudioGemini()
    db = FirebaseAdapter()

    transcription_repo = TranscriptionRepository(
        db = db,
        )

    word_count_repo = WordCountRepository(
        db = db,
        )
    
    conversation_service = ConversationService(
        user_id = None,
        gemini = text_gemini,
    )

    audio_service = TranscriptionService(
        transcription_repo = transcription_repo,
        word_count_repo = word_count_repo,
        gemini = audio_gemini,
    )

    return conversation_service, audio_service
