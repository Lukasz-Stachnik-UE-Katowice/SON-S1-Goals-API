from uuid import UUID

from pydantic import BaseModel

from app.routers.models.Comment import Comment
from app.routers.models.LinkedResources import LinkedResource
from app.routers.models.Note import Note
from app.routers.models.Reminder import Reminder


class Goal(BaseModel):
    id: str
    due_date: str
    frequency: str


