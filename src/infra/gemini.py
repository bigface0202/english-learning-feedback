import vertexai
import os
from typing import List
from vertexai.generative_models import GenerativeModel, SafetySetting, Part, GenerationResponse
from abc import ABC, abstractmethod

from src.models.message import Message

class Gemini(ABC):
    def __init__(self) -> None:
        self.safety_settings = [
            SafetySetting(
                category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
                threshold=SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
            ),
            SafetySetting(
                category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
            ),
            SafetySetting(
                category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
                threshold=SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
            ),
            SafetySetting(
                category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
                threshold=SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
            ),
        ]
        vertexai.init(project = os.environ["PROJECT_ID"], location = os.environ["LOCATION"])
        self.generation_config = {
            "max_output_tokens": 8192,
            "temperature": 1,
            "top_p": 0.95,
        }
        self.model = GenerativeModel("gemini-1.5-flash-001")

    @abstractmethod
    def generate(self, *args, **kwargs):
        pass

class TextGemini(Gemini):
    def __init__(self,
                 conversation_history: List[Message] = []) -> None:
        super().__init__()
        self.conversation_history = conversation_history

    def generate(self, human_message: str) -> GenerationResponse:
        last_5_messages = self.conversation_history[-6:]
        input = "".join(f"{message.speaker}: {message.text}" for message in last_5_messages) + f"human: {human_message}"
        instruction = """
        ## Condition
        You are English professional teacher. 
        Point out uncorrect word and grammer of student speaking.
        Generate recommended useful phrases instead of unnatural tone.
        """

        response = self.model.generate_content(
            [
                instruction,
                input
            ],
            generation_config=self.generation_config,
            safety_settings=self.safety_settings,
            stream=False,
        
        )

        return response

class AudioGemini(Gemini):
    def generate(self, audio_file_uri: str) -> GenerationResponse:
        instruction = """
        ## Condition
        Can you transcribe this English conversation class, in the format of timecode, speaker, caption.
        Speakers are teacher, who is woman and high toned voice, and student, who is man and low toned voice.
        Please follow this format:
        00:00 Teacher Hello.
        00:02 Student Hi.
        ...
        """
        audio_file = Part.from_uri(audio_file_uri, mime_type = "audio/mpeg")
        response = self.model.generate_content(
            [
                audio_file,
                instruction,
            ],
            generation_config = self.generation_config,
            safety_settings = self.safety_settings,
            stream = False,
        )

        return response
