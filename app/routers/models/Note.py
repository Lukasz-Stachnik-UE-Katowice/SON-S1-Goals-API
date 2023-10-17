from pydantic import BaseModel


class Note(BaseModel):
    date_time: str
    text: str