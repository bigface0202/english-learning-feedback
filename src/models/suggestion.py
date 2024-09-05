from typing import List

from src.models.suggestion_detail import SuggestionDetail

class Suggestion:
    def __init__(self,
                suggestion_id: str,
                transcription_id: str,
                model: str,
                suggestion_details : List[SuggestionDetail],
                lesson_date: str,
                created_at: str) -> None:
        self.suggestion_id = suggestion_id
        self.created_at = created_at
        self.lesson_date = lesson_date
        self.transcription_id = transcription_id
        self.model = model
        self.suggestion_details = suggestion_details
