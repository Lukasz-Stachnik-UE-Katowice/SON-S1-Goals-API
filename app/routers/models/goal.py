from pydantic import BaseModel
from datetime import datetime

class Goal(BaseModel):
    id: str
    progress: float
