from fastapi import FastAPI, HTTPException
from .routers import goals

app = FastAPI()

app.include_router(goals.router)

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