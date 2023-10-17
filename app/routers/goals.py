from uuid import UUID, uuid4
import uuid
from fastapi import APIRouter

from app.routers.models.Comment import Comment
from app.routers.models.Goal import Goal
from app.routers.models.LinkedResources import LinkedResource
from app.routers.models.Note import Note
from app.routers.models.Reminder import Reminder

router = APIRouter()


@router.get("/goals", tags=["goals"])
async def get_goals() -> list[Goal]:
    sample_goal = Goal(
        id= str(uuid4()),
        due_date='2023-12-31',
        frequency='weekly'
    )

    return [sample_goal]


@router.get("/goals/{goal_id}", tags=["goals"])
async def get_goal(goals_id: UUID):
    # Here we want to return goal that user whant's to see the details of
    return []


@router.get("/goals/{username}", tags=["goals"])
async def get_user_goals(username: str):
    # Here we want to return all goals in the database for given user
    return [{"goal": "Learn Python"}]


@router.post("/goals", tags=["goals"])
async def post_goal(
        goal):  # Here we need to add goal model that is going to be created https://fastapi.tiangolo.com/tutorial/body/
    # Here we want to add new goal to the database and return it back with status
    return ""


@router.put("/goals/{goal_id}", tags=["goals"])
async def update_goal(goal_id: UUID, goal):
    # Here we want to update goal in the database and return only status
    return


@router.delete("/goals/{goal_id}", tags=["goals"])
async def delete_goal(goal_id: UUID):
    # Here we want to delete goal from the database, and return status
    return
