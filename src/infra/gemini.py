import vertexai
import os
from typing import List
from vertexai.generative_models import GenerativeModel, SafetySetting

from src.models.message import Message

class Gemini:
    def __init__(self,
                 conversation_history: List[Message] = []) -> None:
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
        self.instruction = """
            ## Condition
            - You are English professional teacher. 
            - Point out uncorrect word and grammer.
            - Generate three to five recommended useful phrase instead of unnatural tone.
            """
        self.generation_config = {
            "max_output_tokens": 8192,
            "temperature": 1,
            "top_p": 0.95,
        }
        self.conversation_history = conversation_history
        self.model = GenerativeModel(
            "gemini-1.5-flash-001",
            system_instruction = [
                self.instruction
                ]
        )


    def generate_response(self, 
                          human_message: str) -> str:
        # Create prompt
        last_5_messages = self.conversation_history[-6:]
        input = "".join(f"{message.variant}: {message.text}" for message in last_5_messages) + f"human: {human_message}"

        response = self.model.generate_content(
            [
                input
            ],
            generation_config=self.generation_config,
            safety_settings=self.safety_settings,
            stream=False,
        )

        response_str = response.candidates[0].content.parts[0].text

        return response_str
