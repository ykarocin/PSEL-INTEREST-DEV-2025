from pydantic import BaseModel, Field
from typing import Optional

class TeamCreate(BaseModel):
    name: str = Field(max_length=100)
    leader_id: int

class TeamRead(BaseModel):
    id: int
    name: str
    leader_id: int

class TeamUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=100)
    leader_id: Optional[int] = Field(None)