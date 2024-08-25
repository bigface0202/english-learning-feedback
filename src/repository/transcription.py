from src.models.transcription import Transcription

class TranscriptionRepository:
    def __init__(self, db) -> None:
        self.db = db

    def persist(self, user_uid:str, transcription: Transcription) -> None:
        self.db.set_data(
            user_uid = user_uid,
            collection_name = "transcriptions",
            document_id = transcription.transcription_id,
            data = {
                "model": transcription.model,
                "messages": [
                    {
                        "text": m.text,
                        "speaker": m.speaker,
                        "timestamp": m.timestamp,
                    } for m in transcription.messags
                ],
                "created_at": transcription.created_at,
            }
        )
