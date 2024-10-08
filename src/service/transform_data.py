import re
import json
import sys
from typing import List

from src.models.message import Message
from src.models.suggestion_detail import SuggestionDetail
from src.models.transcription import Transcription
from src.models.suggested_item import SuggetedItem
from src.models.time_frame import TimeFrame

def parse_conversation_data(text:str) ->List[Message]:
    conversation = []
    lines = text.strip().split("\n")
    for line in lines:
        match = re.match(r"(\d{2}:\d{2})\s+(Teacher|Student):\s+(.*)", line)
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

def parse_suggestions(raw_suggestion:str) -> List[SuggestionDetail]:
    suggestion_details = []
    try:
        data = json.loads(raw_suggestion)
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}\n Data was {raw_suggestion}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}\n Data was {raw_suggestion}", file=sys.stderr)

    for item in data:
        suggestion_detail = SuggestionDetail(
            topic = item["topic"],
            time_frame = TimeFrame(
                start = item["time_frame"]["start"],
                end = item["time_frame"]["end"],
            ),
            suggestion_items = [
                SuggetedItem(
                    original_sentence = s["original_sentence"],
                    improved_sentence = s["improved_sentence"],
                    reasoning = s["reasoning"]
                )
                for s in item["suggestions"]
            ]
        )
        suggestion_details.append(suggestion_detail)

    return suggestion_details

