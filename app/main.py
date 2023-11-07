from fastapi import FastAPI
from .routers import goals

app = FastAPI()

app.include_router(goals.router)

@app.get("/")
async def root():
    return {"message": "Hello Students!"}