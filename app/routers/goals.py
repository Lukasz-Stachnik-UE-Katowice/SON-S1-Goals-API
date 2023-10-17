from uuid import UUID
from fastapi import APIRouter

router = APIRouter()

class Goal(BaseModel):
    id: int
    progress: float

goal = Goal(id=1, progress=12)

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
async def update_goal(goal_id: UUID, goal): 
    # Here we want to update goal in the database and return only status
    return 

@router.delete("/goals/{goal_id}", tags=["goals"])
async def delete_goal(goal_id: UUID): 
    # Here we want to delete goal from the database, and return status
    return
