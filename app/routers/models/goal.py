from pydantic import BaseModel

class Goal(BaseModel):
    id: str
    progress: float
