import string
import random
import datetime

from src.infra.gemini import AudioGemini
from src.models.transcription import Transcription
from src.models.word_count import WordCount
from src.repository.transcription import TranscriptionRepository
from src.repository.word_count import WordCountRepository
from src.service import transform_data

class TranscriptionService:
    def __init__(self,
                 transcription_repo: TranscriptionRepository,
                 word_count_repo: WordCountRepository,
                 gemini: AudioGemini) -> None:
        self.transcriptin_repo = transcription_repo
        self.word_count_repo = word_count_repo
        self.gemini = gemini
    
    def _generate_random_string(self,
                                n: int) -> str:
        characters = string.ascii_letters + string.digits
        random_string = "".join(random.choices(characters, k = n))
        return random_string
    
    def transcribe(self, 
                   gcs_uri: str,
                   user_uid: str,
                   lesson_date: str,
                   note: str,) -> None:   
        response = self.gemini.generate(gcs_uri)
        messages = transform_data.parse_conversation_data(response.text)
        teacher_word_count, student_word_count = transform_data.count_words_by_speaker(
            conversation = messages,
            )
        
        # Cnvert string to timestamp
        formatted_lesson_date = datetime.datetime.strptime(lesson_date, "%a %b %d %Y")

        transcription = Transcription(
            transcription_id = self._generate_random_string(10),
            model = "gemini-1.5-flash-001",
            audio_file = gcs_uri, 
            messages = messages,
            created_at = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=9))),
            lesson_date = formatted_lesson_date,
            note = note,
            )

        word_count = WordCount(
            word_count_id = self._generate_random_string(10),
            transcription_id = transcription.transcription_id,
            teacher_word_count = teacher_word_count,
            student_word_count = student_word_count,
            created_at = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=9))),
            lesson_date = formatted_lesson_date
            )

        self.transcriptin_repo.persist(
            user_uid = user_uid,
            transcription = transcription,
            )

        self.word_count_repo.persist(
            user_uid = user_uid,
            word_count = word_count,
            )   
