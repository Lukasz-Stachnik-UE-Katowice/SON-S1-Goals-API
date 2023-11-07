from uuid import UUID
from fastapi import APIRouter, HTTPException
from app.routers.sample_data.SampleGoal import sample_goals
from app.routers.models.Goal import Goal

router = APIRouter()


@router.get("/goals", tags=["goals"])
async def get_goals() -> list[Goal]:
    return sample_goals


@router.get("/goals/{goal_id}", tags=["goals"])
async def get_goal(goals_id: UUID) -> Goal:
    for x in sample_goals:
        if x.id == goals_id:
            return x
    raise HTTPException(status_code=404, detail="Item not found")


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
async def delete_goal(goal_id: str):
    for goal in goalTestList:
        if goal.id == goal_id:
            goalTestList.remove(goal)
            return {"message": "Targeted goal destroyed"}
    return HTTPException(status_code=404, detail="Targeted goal does not exist")

@router.post("/goals/{goal_id}", tags=["goals"])
async def post_progress_goal(progress: float): 
    # Here we want to update the progress with given on or by given value
    return 

@router.post("/goals/{goal_id}/archive", tags=["goals"])
async def archive_goal(goal_id: str): 
    # Here we want to archive the goal 
    return 