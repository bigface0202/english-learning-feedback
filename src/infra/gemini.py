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
        ## Your Role
        You are an experienced English teacher. Your task is to provide suggestions for advanced phrases based on the conversation.

        ## Guidelines
        - Focus on generating feedback for key parts of the conversation; it's not necessary to cover every sentence.
        - Extract and enhance representative sentences that demonstrate advanced vocabulary and natural expression.
        
        ## Output Format
        - Your suggestions should be formatted as HTML for use in a Vue.js application, utilizing Vuetify components for a polished UI.
        - Ensure that the output is plain HTML, without using <template>, Markdown, or code block formatting.
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
        ## Your Role
        You are an experienced English transcriber. Your task is to accurately transcribe conversations from an online English learning platform between a student and a teacher.

        ## Context
        - Speakers:
            - The teacher is usually a woman with a high-pitched voice.
            - The student is a man with a low-pitched voice.
        - Distinguishing Speakers:
            - Use contextual cues from the conversation to determine who is speaking.
        
        ## Output Format
        Please transcribe the conversation with timestamps, speaker identification, and the spoken text, using the following format:
        
        ## Output Format
        Please transcribe with timestamp, people, and script following this format:
        00:00 Teacher: Hello.
        00:02 Student: Hi.
        00:04 Teacher: How are you doing?
        00:07 Student: Yeah, I'm good. Today is a great day.
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
