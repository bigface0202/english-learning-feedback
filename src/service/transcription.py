import string
import random

from src.infra.gemini import AudioGemini
from src.models.transcription import Transcription
from src.repository.transcription import TranscriptionRepository
from src.service import transform_data

class TranscriptionService:
    def __init__(self,
                 user_id: str,
                 transcription_repo: TranscriptionRepository,
                 gemini: AudioGemini) -> None:
        self.user_id = user_id
        self.transcriptin_repo = transcription_repo
        self.gemini = gemini
    
    def _generate_random_string(self,
                                n: int) -> str:
        characters = string.ascii_letters + string.digits
        random_string = "".join(random.choices(characters, k = n))
        return random_string
    
    def transcribe(self, 
                   message: str) -> None:   
        response = self.gemini.generate(message)
        messages = transform_data.parse_conversation_data(response.text)
        transcription = Transcription(
            id = self._generate_random_string(10),
            transcription_id = self._generate_random_string(10),
            user_id = self.user_id,
            model = "gemini-1.5-flash-001",
            messages = messages
        )

        self.transcriptin_repo.persist(transcription)
