class Message:
    def __init__(self,
                 text: str,
                 speaker: str,
                 timestamp: str) -> None:
        self.text = text
        self.speaker = speaker
        self.timestamp = timestamp
