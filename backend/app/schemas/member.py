from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MemberCreate(BaseModel):
    team_id: int
    user_id: int

class MemberRead(BaseModel):
    team_id: int
    user_id: int