from src.models.message import Message
from typing import List

class Conversation:
    def __init__(self,
                 id: str,
                 user_id: str,
                 conversation_id: str,
                 ai_model: str,
                 is_finished: str,
                 messages: List[Message] = []) -> None:
        self.id = id
        self.user_id = user_id
        self.conversation_id = conversation_id
        self.ai_model = ai_model
        self.is_finished = is_finished
        self.messages = messages
