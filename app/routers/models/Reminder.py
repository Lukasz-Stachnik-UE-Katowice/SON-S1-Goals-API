from pydantic import BaseModel

class Reminder(BaseModel):
    date_time: str
    message: str