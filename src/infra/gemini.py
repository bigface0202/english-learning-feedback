import vertexai
import json
from vertexai.generative_models import GenerativeModel, Part, SafetySetting, FinishReason


class Gemini:
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
        # TODO: 環境変数の埋め込み
        with open("../environments/env.json") as f:
            env = json.load(f)
        vertexai.init(project = env["project_id"], location = env["location"])
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
        self.model = GenerativeModel(
            "gemini-1.5-flash-001",
            system_instruction = [
                self.instrcution
                ]
        )


    def generate_response(self, 
                          human_message: str) -> str:
        response = self.model.generate_content(
            [
                human_message
            ],
            generation_config=self.generation_config,
            safety_settings=self.safety_settings,
            stream=False,
        )

        response_str = response.candidates[0].content.parts[0]

        return response_str
