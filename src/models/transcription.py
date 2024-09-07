from src.models.message import Message
from typing import List

class Transcription:
    def __init__(self,
                 transcription_id: str,
                 model: str,
                 audio_file: str,
                 download_url: str,
                 created_at: str,
                 lesson_date: str,
                 note: str,
                 messages: List[Message] = [],
                 ) -> None:
        self.transcription_id = transcription_id
        self.model = model
        self.audio_file = audio_file
        self.download_url = download_url
        self.messages = messages
        self.created_at = created_at
        self.lesson_date = lesson_date
        self.note = note
