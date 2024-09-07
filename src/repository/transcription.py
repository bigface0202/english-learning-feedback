from src.models.transcription import Transcription
from src.infra.firebase import FirebaseAdapter

class TranscriptionRepository:
    def __init__(self, db:FirebaseAdapter) -> None:
        self.db = db

    def persist(self, user_uid:str, transcription: Transcription) -> None:
        self.db.set_data(
            user_uid = user_uid,
            collection_name = "transcriptions",
            document_id = transcription.transcription_id,
            data = {
                "model": transcription.model,
                "audio_file": transcription.audio_file,
                "download_url": transcription.download_url,
                "messages": [
                    {
                        "text": m.text,
                        "speaker": m.speaker,
                        "timestamp": m.timestamp,
                    } for m in transcription.messages
                ],
                "created_at": transcription.created_at,
                "lesson_date": transcription.lesson_date,
                "note": transcription.note,
            }
        )
    
    def extract(self, user_uid:str, transcription_id: str) -> Transcription:
        transcription:Transcription = self.db.get_data(
            user_uid = user_uid,
            collection_name = "transcriptions",
            document_id = transcription_id,
        )

        return transcription
