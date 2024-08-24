import string
import random
from datetime import datetime

from src.infra.gemini import TextGemini
from src.models.message import Message
from src.models.conversation import Conversation

class ConversationService:
    def __init__(self,
                 user_id: str,
                 gemini: TextGemini) -> None:
        self.user_id = user_id
        self.gemini = gemini
    
    def _generate_random_string(self,
                                n: int) -> str:
        characters = string.ascii_letters + string.digits
        random_string = "".join(random.choices(characters, k = n))
        return random_string
    
    def make_reply(self, 
                   message: str):
        # TODO: Firebaseから会話履歴を同期
        conversations = []
        if (len(conversations) == 0):
            conversation = Conversation(
                id = self._generate_random_string(10),
                conversation_id = self._generate_random_string(10),
                user_id = self.user_id,
                ai_model = "gemini-1.5-flash-001",
                is_finished = False,
                messages = []
            )
            conversations = [conversation]
        latest_conversation = conversations[-1]

        # Pass the latest conversation as history to Gemini
        self.gemini.conversation_history = latest_conversation.messages

        # Generate next response from Gemini
        response = self.gemini.generate(message)

        # Add new human message
        human_msg = Message(
            text = message,
            speaker = "human",
            timestamp = datetime.now().isoformat()
        )
        latest_conversation.messages.append(human_msg)

        # Add new Gemini message
        system_msg = Message(
            text = message,
            speaker = "system",
            timestamp = datetime.now().isoformat()
        )
        latest_conversation.messages.append(system_msg)

        # TODO: Store the conversation to DB

        return response
