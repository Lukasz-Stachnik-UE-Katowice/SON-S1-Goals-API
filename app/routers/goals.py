from uuid import UUID
from fastapi import APIRouter

router = APIRouter()

@router.get("/goals", tags=["goals"])
async def get_goals():
    sample_data = {
    "id": 1,
    "due_date": "2023-12-31",  # Format daty YYYY-MM-DD
    "frequency": "monthly",
    "progress": 0.75,
    "reminders": [
        {"date_time": "2023-10-17T10:00:00", "message": "Don't forget to work on your goal."},
        {"date_time": "2023-11-01T09:00:00", "message": "Monthly check-in."}
    ],
    "notes": [
        {"date_time": "2023-10-15T15:30:00", "text": "Started working on the goal."},
        {"date_time": "2023-11-05T14:15:00", "text": "Made good progress this month."}
    ],
    "privacy": "private",
    "shared_with": ["user1", "user2", "user3"],
    "tags": ["health", "fitness", "2023 goals"],
    "linked_resources": [
        {"title": "Online Workout Plan", "url": "https://example.com/workout-plan"},
        {"title": "Healthy Eating Guide", "url": "https://example.com/healthy-eating"}
    ],
    "comments": [
        {"user_id": "user4", "date_time": "2023-10-20T18:45:00", "text": "You're doing great! Keep it up."},
        {"user_id": "user5", "date_time": "2023-11-10T12:30:00", "text": "I'm inspired by your progress."}
    ],
    "badges": ["dedicated", "achiever"]
}

    return sample_data

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