from typing import Tuple

from src.infra.gemini import Gemini
from src.infra.s2p import SpeechToText
from src.service.conversation import ConversationService
from src.service.transcription import TranscriptionService

def bootstrap() -> Tuple[ConversationService, TranscriptionService]:
    gemini = Gemini()
    s2p = SpeechToText()
    
    conversation_service = ConversationService(
        user_id = None,
        gemini = gemini
    )

    transcription_servce = TranscriptionService(
        user_id = None,
        s2p = s2p
    )

    return conversation_service, transcription_servce
