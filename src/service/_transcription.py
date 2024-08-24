# import string
# import random

# from src.infra.s2p import SpeechToText

# class TranscriptionService:
#     def __init__(self,
#                  user_id: str,
#                  s2p: SpeechToText) -> None:
#         self.user_id = user_id
#         self.s2p = s2p
    
#     def _generate_random_string(self,
#                                 n: int) -> str:
#         characters = string.ascii_letters + string.digits
#         random_string = "".join(random.choices(characters, k = n))
#         return random_string
    
#     def make_transcription(self,
#                            gcs_uri: str) -> str:
#         response = self.s2p.generate_text(gcs_uri=gcs_uri)
#         # TODO: Store the transcprited text to DB
        
#         return response
