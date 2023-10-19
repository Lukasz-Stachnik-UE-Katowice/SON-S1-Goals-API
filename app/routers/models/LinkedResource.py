from pydantic import BaseModel


class LinkedResource(BaseModel):
    title: str
    url: str