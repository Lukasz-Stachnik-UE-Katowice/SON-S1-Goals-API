from pydantic import BaseModel


class Comment(BaseModel):
    user_id: str
    date_time: str
    text: str
