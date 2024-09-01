import re
from typing import List

from src.models.message import Message
from src.models.transcription import Transcription

def parse_conversation_data(text:str) ->List[Message]:
    conversation = []
    lines = text.strip().split("\n")
    for line in lines:
        match = re.match(r"(\d{2}:\d{2})\s+(Teacher|Student)\s+(.*)", line)
        if match:
            timestamp, speaker, text = match.groups()
            message = Message(
                timestamp=timestamp,
                speaker=speaker,
                text=text
            )
            conversation.append(message)

    return conversation
        
def count_words_by_speaker(conversation:List[Message]) -> tuple[object, object]:
    teacher_word_count = {}
    student_word_count = {}

    for entry in conversation:
        speaker = entry.speaker
        message = entry.text

        message = re.sub(r'[?.,!]', '', message)
        words = message.split()

        if speaker == "Teacher":
            for word in words:
                if word in teacher_word_count:
                    teacher_word_count[word] += 1
                else:
                    teacher_word_count[word] = 1
        else:
            for word in words:
                if word in student_word_count:
                    student_word_count[word] += 1
                else:
                    student_word_count[word] = 1
    return teacher_word_count, student_word_count

def create_conversation_prompt(transcription:Transcription) -> str:
    messages:List[Message] = transcription["messages"]
    prompt_parts = [f"{message['timestamp']} {message['speaker']}:{message['text']}\n" for message in messages]
    prompt = "".join(prompt_parts)

    return prompt
