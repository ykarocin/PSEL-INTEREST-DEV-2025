from sqlmodel import SQLModel, Field, Relationship

class TeamMember(SQLModel, table=True):
    team_id: int = Field(foreign_key="team.id", primary_key=True)
    user_id: int = Field(foreign_key="user.id", primary_key=True, unique=True)  # Unicidade de membro

    # Relacionamentos
    team: "Team" = Relationship(back_populates="members")
    user: "User" = Relationship(back_populates="member_teams")