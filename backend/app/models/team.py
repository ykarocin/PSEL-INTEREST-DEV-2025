from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=100)
    leader_id: int = Field(foreign_key="user.id", unique=True)  # Unicidade de líder

    # Relacionamentos
    leader: "User" = Relationship(back_populates="led_team")
    members: List["TeamMember"] = Relationship(back_populates="team")