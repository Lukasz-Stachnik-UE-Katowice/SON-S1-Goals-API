from fastapi import FastAPI, HTTPException
from datetime import datetime
from typing import List
from pydantic import BaseModel
from .routers import goals

app = FastAPI()

app.include_router(goals.router)


class Goal(BaseModel):
    id: int
    due_date: datetime  # You can use a date format
    frequency: str  # You can use an enum for 'daily', 'weekly', 'monthly'
    progress: float
    reminders: List[dict] | None = None  # List of reminders with 'date_time' and 'message'
    notes: List[dict] | None = None  # List of notes with 'date_time' and 'text'
    privacy: str | None = None  # You can use an enum for 'private', 'shared', 'public'
    shared_with: List[str] | None = None  # List of user_ids
    tags: List[str] | None = None
    linked_resources: List[dict] | None = None  # List of linked resources with 'title' and 'url'
    comments: List[dict] | None = None # List of comments with 'user_id', 'date_time', and 'text'
    badges: List[str] | None = None


@app.get("/")
async def root():
    return {"message": "Hello Students!"}

@app.delete("/goals/{goal_id}")
async def delete_goal(goal_id: int):
    global goals
    goal_to_delete = None

    for goal in goals:
        if goal["goal_id"] == goal_id:
            goals.remove(goal_id)
            break

    if goal_to_delete is None:
        raise HTTPException(status_code=404, detail="Cel o podanym goal_id nie istnieje")

    goals.remove(goal_to_delete)
    return {"message": "Cel został usunięty"}