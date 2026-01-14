from sqlmodel import Session, select
from app.models import TeamMember, User, Team
from app.exceptions import NotFoundError, BusinessRuleError

class MemberRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_member(self, team_id: int, user_id: int) -> TeamMember:
        # Verificações
        team = self.session.get(Team, team_id)
        if not team:
            raise NotFoundError("TEAM_NOT_FOUND")

        user = self.session.get(User, user_id)
        if not user:
            raise NotFoundError("USER_NOT_FOUND")

        existing_member = self.session.exec(
            select(TeamMember).where(TeamMember.user_id == user_id)
        ).first()
        if existing_member:
            raise BusinessRuleError("USER_ALREADY_BELONGS_TO_A_TEAM")

        member = TeamMember(team_id=team_id, user_id=user_id)
        self.session.add(member)
        self.session.commit()
        self.session.refresh(member)
        return member

    def remove_member(self, team_id: int, user_id: int) -> bool:
        team = self.session.get(Team, team_id)
        if not team:
            raise NotFoundError("TEAM_NOT_FOUND")

        if team.leader_id == user_id:
            raise BusinessRuleError("CANNOT_REMOVE_TEAM_LEADER")

        member = self.session.exec(
            select(TeamMember).where(
                TeamMember.team_id == team_id,
                TeamMember.user_id == user_id
            )
        ).first()
        if not member:
            raise NotFoundError("MEMBER_NOT_FOUND")

        self.session.delete(member)
        self.session.commit()
        return True