class SuggetedItem:
    def __init__(self,
                 original_sentence,
                 improved_sentence,
                 reasoning) -> None:
        self.original_sentence = original_sentence
        self.improved_sentence = improved_sentence
        self.reasoning = reasoning
