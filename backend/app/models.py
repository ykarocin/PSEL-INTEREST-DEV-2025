from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

# Arquivo base para criação de todos os modelos necessários
# Serve como base para User e Team models
# Através dele a exportação para o alembic deve ser executada

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=100)

    # Relacionamentos
    led_team: Optional["Team"] = Relationship(back_populates="leader")
    member_teams: List["TeamMember"] = Relationship(back_populates="user")

class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=100)
    leader_id: int = Field(foreign_key="user.id", unique=True)  # Unicidade de líder

    # Relacionamentos
    leader: User = Relationship(back_populates="led_team")
    members: List["TeamMember"] = Relationship(back_populates="team")

class TeamMember(SQLModel, table=True):
    team_id: int = Field(foreign_key="team.id", primary_key=True)
    user_id: int = Field(foreign_key="user.id", primary_key=True, unique=True)  # Unicidade de membro

    # Relacionamentos
    team: Team = Relationship(back_populates="members")
    user: User = Relationship(back_populates="member_teams")