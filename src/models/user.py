class User:
    def __init__(self,
                 user_id: str,
                 name: str,
                 email: str,
                 created_at: str) -> None:
        self.user_id = user_id
        self.name = name
        self.email = email
        self.created_at = created_at
