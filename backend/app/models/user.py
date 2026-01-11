from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=100)

    # Relacionamentos
    led_team: Optional["Team"] = Relationship(back_populates="leader")
    member_teams: List["TeamMember"] = Relationship(back_populates="user")