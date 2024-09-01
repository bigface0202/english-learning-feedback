from typing import Tuple

from src.infra.gemini import TextGemini, AudioGemini
from src.infra.firebase import FirebaseAdapter
from src.service.suggestion import SuggestionService
from src.service.transcription import TranscriptionService
from src.repository.transcription import TranscriptionRepository
from src.repository.word_count import WordCountRepository
from src.repository.suggestion import SuggestionRepository

def bootstrap() -> Tuple[SuggestionService, TranscriptionService]:
    text_gemini = TextGemini()
    audio_gemini = AudioGemini()
    db = FirebaseAdapter()

    transcription_repo = TranscriptionRepository(
        db = db,
        )

    word_count_repo = WordCountRepository(
        db = db,
        )
    
    suggestion_repo = SuggestionRepository(
        db = db,
    )
    
    suggestion_service = SuggestionService(
        transcription_repo = transcription_repo,
        suggestion_repo = suggestion_repo,
        gemini = text_gemini,
    )

    audio_service = TranscriptionService(
        transcription_repo = transcription_repo,
        word_count_repo = word_count_repo,
        gemini = audio_gemini,
    )

    return suggestion_service, audio_service
