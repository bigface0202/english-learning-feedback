import string
import random
import datetime

from src.infra.gemini import AudioGemini
from src.models.transcription import Transcription
from src.repository.transcription import TranscriptionRepository
from src.service import transform_data

class TranscriptionService:
    def __init__(self,
                 transcription_repo: TranscriptionRepository,
                 gemini: AudioGemini) -> None:
        self.transcriptin_repo = transcription_repo
        self.gemini = gemini
    
    def _generate_random_string(self,
                                n: int) -> str:
        characters = string.ascii_letters + string.digits
        random_string = "".join(random.choices(characters, k = n))
        return random_string
    
    def transcribe(self, 
                   gcs_uri: str,
                   user_uid: str) -> None:   
        response = self.gemini.generate(gcs_uri)
        messages = transform_data.parse_conversation_data(response.text)
        transcription = Transcription(
            transcription_id = self._generate_random_string(10),
            model = "gemini-1.5-flash-001",
            audio_file = gcs_uri, 
            messages = messages,
            created_at = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=9)))
        )

        self.transcriptin_repo.persist(
            user_uid = user_uid,
            transcription = transcription
        )
