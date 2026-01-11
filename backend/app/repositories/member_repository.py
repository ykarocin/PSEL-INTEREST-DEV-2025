from sqlmodel import Session, select
from app.models import TeamMember, User, Team
from app.exceptions import NotFoundError

class MemberRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_member(self, team_id: int, user_id: int) -> TeamMember:
        # Verificações
        team = self.session.get(Team, team_id)
        if not team:
            raise NotFoundError("Team not found")

        user = self.session.get(User, user_id)
        if not user:
            raise NotFoundError("User not found")

        existing_member = self.session.exec(
            select(TeamMember).where(TeamMember.user_id == user_id)
        ).first()
        if existing_member:
            raise ValueError("User is already a member of another team")

        member = TeamMember(team_id=team_id, user_id=user_id)
        self.session.add(member)
        self.session.commit()
        self.session.refresh(member)
        return member

    def remove_member(self, team_id: int, user_id: int) -> bool:
        team = self.session.get(Team, team_id)
        if not team:
            raise NotFoundError("Team not found")

        if team.leader_id == user_id:
            raise ValueError("Cannot remove the team leader")

        member = self.session.exec(
            select(TeamMember).where(
                TeamMember.team_id == team_id,
                TeamMember.user_id == user_id
            )
        ).first()
        if not member:
            raise NotFoundError("Member not found in this team")

        self.session.delete(member)
        self.session.commit()
        return True