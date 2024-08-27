from src.models.word_count import WordCount

class WordCountRepository:
    def __init__(self, db) -> None:
        self.db = db

    def persist(self, user_uid:str, word_count: WordCount) -> None:
        self.db.set_data(
            user_uid = user_uid,
            collection_name = "word_count",
            document_id = word_count.word_count_id,
            data = {
                "transcription_id": word_count.transcription_id,
                "teacher_word_count": word_count.teacher_word_count,
                "student_word_count": word_count.student_word_count,
                "created_at": word_count.created_at,
            }
        )
