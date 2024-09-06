from typing import List

from src.models.suggested_item import SuggetedItem
from src.models.time_frame import TimeFrame

class SuggestionDetail:
    def __init__(self,
                 topic: str,
                 time_frame: TimeFrame,
                 suggestion_items: List[SuggetedItem]) -> None:
        self.topic = topic
        self.time_frame = time_frame
        self.suggestion_items = suggestion_items
