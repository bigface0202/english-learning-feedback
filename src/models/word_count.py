class WordCount:
    def __init__(self,
                 word_count_id: str,
                 transcription_id: str,
                 teacher_word_count: object,
                 student_word_count: object,
                 created_at: str,
                 lesson_date: str) -> None:
        self.word_count_id = word_count_id
        self.transcription_id = transcription_id
        self.teacher_word_count = teacher_word_count
        self.student_word_count = student_word_count
        self.created_at = created_at
        self.lesson_date = lesson_date
