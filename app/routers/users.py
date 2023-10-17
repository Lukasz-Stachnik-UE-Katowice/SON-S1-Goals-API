from uuid import UUID


class User:
    def __init__(self, id: UUID, name: str) -> None:
        self.id = id
        self.name = name