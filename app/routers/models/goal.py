from pydantic import BaseModel

class Goal(BaseModel):
    id: str
    progress: float
    archived: bool = False  # archived default: False
