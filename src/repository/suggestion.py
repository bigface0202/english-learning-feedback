from src.models.suggestion import Suggestion
from src.infra.firebase import FirebaseAdapter

class SuggestionRepository:
    def __init__(self, db:FirebaseAdapter) -> None:
        self.db = db
    
    def persist(self, user_uid:str, suggestion: Suggestion) -> None:
        self.db.set_data(
            user_uid = user_uid,
            collection_name = "suggestions",
            document_id = suggestion.suggestion_id,
            data = {
                "transcription_id": suggestion.transcription_id,
                "created_at": suggestion.created_at,
                "model": suggestion.model,
                "suggestion": suggestion.suggestion,
                "lesson_date": suggestion.lesson_date,
            }
        )
