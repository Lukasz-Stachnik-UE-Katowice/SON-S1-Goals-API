from fastapi import HTTPException
from uuid import UUID
from fastapi import APIRouter
from pydantic import BaseModel

class Goal(BaseModel):
    id: str
    progress: float


router = APIRouter()

goals = [Goal(id="1", progress=0.1)]

@router.get("/goals", tags=["goals"])
async def get_goals():
    # Here we want to return all goals in the database
    return []

@router.get("/goals/{goal_id}", tags=["goals"])
async def get_goal(goals_id: UUID):
    # Here we want to return goal that user whant's to see the details of
    return []

@router.get("/goals/{username}", tags=["goals"])
async def get_user_goals(username: str): 
    # Here we want to return all goals in the database for given user
    return [{"goal": "Learn Python"}]

@router.post("/goals", tags=["goals"])
async def post_goal(goal): #Here we need to add goal model that is going to be created https://fastapi.tiangolo.com/tutorial/body/
    # Here we want to add new goal to the database and return it back with status
    return ""

@router.put("/goals/{goal_id}", tags=["goals"])
async def update_goal(goal_id: str, goal_obj: Goal): 
    # Here we want to update goal in the database and return only status
    for goal in goals:
        if goal.id == goal_id:
            goal.id = goal_obj.id
            goal.progress = goal_obj.progress
            return goal
    raise HTTPException(404, "Goal doesn't exist")


@router.delete("/goals/{goal_id}", tags=["goals"])
async def delete_goal(goal_id: UUID): 
    # Here we want to delete goal from the database, and return status
    return


@router.post("/goals/{goal_id}/progress", tags=["goals"])
async def post_progress_goal(goal_id: int, progress: float):
    # Here we want to update the progress with given value
    for goal in goals:
        if goal.id == goal_id:
            goal.progress = progress
            return {"goal": goal}
    raise HTTPException(status_code=400, detail="Targeted goal does not exist")
