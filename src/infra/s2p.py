from google.cloud import speech

class SpeechToText:
    def __init__(self) -> None:
        self.client = speech.SpeechClient()
        self.config = speech.RecognitionConfig(
            encoding = speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz = 16000,
            language_code = "en-US",
        )

    def generate_text(self,
                      gcs_uri: str) -> str:
        audio = speech.RecognitionAudio(uri = gcs_uri)
        response = self.client.recognize(config = self.config,
                                         audio = audio)
        
        # TODO: Do I need to return multiple results?
        return response.results[0].alternatives[0].transcript
