from pydantic import BaseModel
from .helpers import Frequency


class Goal(BaseModel):
    id: int
    title: str  # added
    due_date: str
    frequency: Frequency
    progress: float
    archived: bool = False  # archived default: False
