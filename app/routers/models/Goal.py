from uuid import UUID
from app.routers.models import Comment
from pydantic import BaseModel

from app.routers.models.Comment import Comment
from app.routers.models.LinkedResource import LinkedResource
from app.routers.models.Note import Note
from app.routers.models.Reminder import Reminder


class Goal(BaseModel):
    id: UUID
    due_date: str
    frequency: str
    comment: list
    progress: float
    reminders: list
    notes: list
    privacy: str
    shared_with: list
    tags: list
    linked_resources: list
    badges: list



