from fastapi import FastAPI
from app.routers import goals

app = FastAPI()

app.include_router(goals.router)

@app.get("/")
async def root():
    return {"message": "Hello Students!"}