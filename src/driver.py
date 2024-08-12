from src.infra.gemini import Gemini
from src.service.conversation import ConversationService

def bootstrap() -> ConversationService:
    gemini = Gemini()
    
    conversation_service = ConversationService(
        user_id = None,
        gemini = gemini
    )

    return conversation_service
