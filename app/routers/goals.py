from uuid import UUID

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from .models.goal import Goal
from .models.user import User
from .models.helpers import Frequency


# FAKE DATA
# =======================================================================
goals: list[Goal] = [
    Goal(id=1, title="Learn rust", due_date="07.11.2023", progress= 0.6, frequency=Frequency.DAILY),
    Goal(id=2, title="Learn FastAPI", due_date="07.12.2023", progress= 0.75, frequency=Frequency.MONTHLY),
    Goal(id=3, title="Gain some weight", due_date="01.01.2024", progress= 0.5, frequency=Frequency.DAILY),
    Goal(id=4, title="Lose some weight", due_date="01.02.2024", progress= -2, frequency=Frequency.WEEKLY),
]

users: list[User] = [
    User(id=UUID("de305d54-75b4-431b-adb2-eb6b9e546013"), name="John"),
    User(id=UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8"), name="Paul"),
    User(id=UUID("f47ac10b-58cc-4372-a567-0e02b2c3d479"), name="Rob"),
    User(id=UUID("68b65546-6784-40d8-a111-84126b2cb188"), name="Bob"),
]

data: dict[str, list[Goal]] = {
    user.name: [goal]
    for user, goal in zip(users, goals)
}
# =======================================================================


router = APIRouter()

@router.get("/goals/{goal_id}", tags=["goals"])
async def get_goal(goals_id: int):
    # Here we want to return goal that user whant's to see the details of
    return []

@router.post("/goals", tags=["goals"])
async def post_goal(goal): #Here we need to add goal model that is going to be created https://fastapi.tiangolo.com/tutorial/body/
    # Here we want to add new goal to the database and return it back with status
    return data

@router.get("/goals", tags=["goals"])
async def get_goals():
    # Here we want to return all goals in the database
    content = jsonable_encoder(list(data.values()))
    return JSONResponse(content=content)

@router.get("/users/{username}/goals", tags=["goals"])
async def get_user_goals(username: str):
    # Here we want to return all goals in the database for given user
    try:
        content = jsonable_encoder(data[username]) 
        return JSONResponse(content=content)
    except KeyError:
        raise HTTPException(404, "User with this name could not be found.")

@router.put("/goals/{goal_id}", tags=["goals"])
async def update_goal(goal_id: int, goal_obj: Goal):
    # Here we want to update goal in the database and return only status
    for goal in goals:
        if goal.id == goal_id:
            goal.id = goal_obj.id
            goal.progress = goal_obj.progress
            return goal
    raise HTTPException(404, "Goal doesn't exist")

@router.delete("/goals/{goal_id}", tags=["goals"])
async def delete_goal(goal_id: str):
    for goal in goals:
        if goal.id == goal_id:
            goals.remove(goal)
            return {"message": "Targeted goal destroyed"}
    return HTTPException(status_code=404, detail="Targeted goal does not exist")

@router.post("/goals/{goal_id}/progress", tags=["goals"])
async def post_progress_goal(goal_id: int, progress: float):
    # Here we want to update the progress with given value
    for goal in goals:
        if goal.id == goal_id:
            goal.progress = progress
            return {"goal": goal}
    raise HTTPException(status_code=400, detail="Targeted goal does not exist")

@router.post("/goals/{goal_id}/archive", tags=["goals"])
async def archive_goal(goal_id: str):
    # Here we want to archive the goal
    return
