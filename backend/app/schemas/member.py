from pydantic import BaseModel

class MemberCreate(BaseModel):
    team_id: int
    user_id: int

class MemberRead(BaseModel):
    team_id: int
    user_id: int