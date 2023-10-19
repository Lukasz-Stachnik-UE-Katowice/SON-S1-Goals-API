from pydantic import BaseModel
from datetime import datetime

class Goal(BaseModel):
    id: str
    due_date: datetime  # You can use a date format