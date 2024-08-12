class Audio:
    def __init__(self,
                 audio_id: str, 
                 user_id: str,
                 file_path: str,
                 created_at: str) -> None:
        self.audio_id = audio_id
        self.user_id = user_id
        self.file_path = file_path
        self.created_at = created_at
