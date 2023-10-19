from pydantic import BaseModel

class Goal(BaseModel):
    def __init__(self, id, progress, archived=False):
        self.id = str
        self.progress = float
        self.archived = bool