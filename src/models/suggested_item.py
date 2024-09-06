class SuggetedItem:
    def __init__(self,
                 original_sentence: str,
                 improved_sentence: str,
                 reasoning: str) -> None:
        self.original_sentence = original_sentence
        self.improved_sentence = improved_sentence
        self.reasoning = reasoning
