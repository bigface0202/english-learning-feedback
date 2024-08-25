from src.models.message import Message
from typing import List

class Transcription:
    def __init__(self,
                 transcription_id: str,
                 model: str,
                 audio_file:str,
                 created_at: str,
                 messages: List[Message] = [],
                 ) -> None:
        self.transcription_id = transcription_id
        self.model = model
        self.audio_file = audio_file
        self.messags = messages
        self.created_at = created_at
