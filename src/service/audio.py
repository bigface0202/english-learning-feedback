import string
import random

from src.infra.gemini import AudioGemini

class AudioService:
    def __init__(self,
                 user_id: str,
                 gemini: AudioGemini) -> None:
        self.user_id = user_id
        self.gemini = gemini
    
    def _generate_random_string(self,
                                n: int) -> str:
        characters = string.ascii_letters + string.digits
        random_string = "".join(random.choices(characters, k = n))
        return random_string
    
    def make_reply(self, 
                   message: str) -> str:        
        response = self.gemini.generate(message)

        return response
