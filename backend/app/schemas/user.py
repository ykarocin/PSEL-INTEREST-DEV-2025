from pydantic import BaseModel, Field
from typing import Optional

class UserCreate(BaseModel):
    name: str = Field(max_length=100)

class UserRead(BaseModel):
    id: int
    name: str

class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=100)