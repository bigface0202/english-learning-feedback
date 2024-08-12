class Message:
    def __init__(self,
                 text: str,
                 variant: str,
                 timestamp: str) -> None:
        self.text = text
        self.variant = variant
        self.timestamp = timestamp
