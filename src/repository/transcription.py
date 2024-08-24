from src.models.message import Message
from src.models.transcription import Transcription

class TranscriptionRepository:
    def __init__(self, db) -> None:
        self.db = db

    def persist(self, transcription: Transcription) -> None:
        self.db.set_data(
            "transcriptions",
            transcription.id,
            {
                "id": transcription.id,
                "model": transcription.model,
                "user_id": transcription.user_id,
                "transcription_id": transcription.transcription_id,
                "messages": [
                    {
                        "text": m.text,
                        "speaker": m.speaker,
                        "timestamp": m.timestamp,
                    } for m in transcription.messags
                ]
            }
        )
