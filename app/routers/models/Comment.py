from uuid import UUID

from pydantic import BaseModel


class Comment(BaseModel):
    user_id: UUID
    date_time: str
    text: str
