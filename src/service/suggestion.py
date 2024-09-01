import string
import random
import datetime

from src.infra.gemini import TextGemini
from src.models.message import Message
from src.models.suggestion import Suggestion
from src.repository.transcription import TranscriptionRepository
from src.repository.suggestion import SuggestionRepository
from src.service import transform_data

class SuggestionService:
    def __init__(self,
                 transcription_repo: TranscriptionRepository,
                 suggestion_repo: SuggestionRepository,
                 gemini: TextGemini) -> None:
        self.transcription_repo = transcription_repo
        self.suggestion_repo = suggestion_repo
        self.gemini = gemini
    
    def _generate_random_string(self,
                                n: int) -> str:
        characters = string.ascii_letters + string.digits
        random_string = "".join(random.choices(characters, k = n))
        return random_string
    
    def make_suggestion(self, 
                   transcription_id: str,
                   user_uid: str) -> None:
        transcription = self.transcription_repo.extract(
            user_uid = user_uid,
            transcription_id = transcription_id
        )

        conversation_prompt = transform_data.create_conversation_prompt(
            transcription = transcription)
        
        response = self.gemini.generate(conversation_prompt)

        suggestion = Suggestion(
            suggestion_id = self._generate_random_string(10),
            created_at = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=9))),
            transcription_id = transcription_id,
            model = "gemini-1.5-flash-001",
            lesson_date = transcription["lesson_date"],
            suggestion = response.text
        )

        self.suggestion_repo.persist(
            user_uid = user_uid,
            suggestion = suggestion
        )

