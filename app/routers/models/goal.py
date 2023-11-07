from uuid import UUID
from pydantic import BaseModel



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



