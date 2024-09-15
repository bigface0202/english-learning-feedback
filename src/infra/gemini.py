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
        - Ignore interjections or filler words like "Uh," "Um," "Ah," "Er," and other similar sounds during the suggestion process.
        - Ensure that the suggestions are concise but clear.
        - Please output **only 10 suggestions** in total.

        ## Formatting Instructions
        - Output the suggestions strictly as **valid JSON**.
            - Do not foget put comma and brackets.
            - Avoid trailing commas, and make sure every comma is correctly placed.
            - Ensure that the JSON keys and values are properly enclosed in double quotes.
        - Your max output tokens are 8192, do not exceed the token to generate your suggestions.
        - Do not use any extra characters like backticks, quotation marks for keys, or Markdown formatting.

        ## Output Format
        The JSON should follow this structure exactly:
        [
            {
                "topic": "Introducing Yourself",
                "time_frame": {
                    "start": "0:30",
                    "end": "1:00"
                },
                "suggestions": [
                    {
                        "original_sentence": "This is our first lesson together.",
                        "improved_sentence": "I'm excited to begin our journey together today.",
                        "reasoning": "The revised phrase is more engaging and personal."
                    },
                    {
                        "original_sentence": "It is quite difficult to find on the map normally for the students.",
                        "improved_sentence": "It often proves tricky for students to locate on a map.",
                        "reasoning": "The alternative phrasing sounds more natural and concise."
                    },
                ],
            },
        ]
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
