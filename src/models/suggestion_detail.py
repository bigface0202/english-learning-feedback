from typing import List

from src.models.suggested_item import SuggetedItem
from src.models.duration import Duration

class SuggestionDetail:
    def __init__(self,
                 topic: str,
                 duration: Duration,
                 suggestion_items: List[SuggetedItem]) -> None:
        self.topic = topic
        self.duration = duration
        self.suggestion_items = suggestion_items
