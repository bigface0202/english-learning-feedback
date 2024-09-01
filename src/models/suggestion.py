from src.models.message import Message
from typing import List

class Suggestion:
    def __init__(self,
                suggestion_id: str,
                transcription_id: str,
                model: str,
                suggestion : str,
                lesson_date: str,
                created_at: str) -> None:
        self.suggestion_id = suggestion_id
        self.created_at = created_at
        self.lesson_date = lesson_date
        self.transcription_id = transcription_id
        self.model = model
        self.suggestion = suggestion
