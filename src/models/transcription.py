from src.models.message import Message
from typing import List

class Transcription:
    def __init__(self,
                 id: str,
                 user_id: str,
                 transcription_id: str,
                 model: str,
                 messages: List[Message] = []) -> None:
        self.id = id
        self.user_id = user_id
        self.transcription_id = transcription_id
        self.model = model
        self.messags = messages
