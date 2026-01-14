from sqlmodel import Session, select, delete
from typing import List, Optional
from app.models import Team, User, TeamMember
from app.exceptions import NotFoundError, BusinessRuleError

class TeamRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, name: str, leader_id: int) -> Team:
        # Verificar se líder existe e não pertence a outra equipe
        leader = self.session.get(User, leader_id)
        if not leader:
            raise NotFoundError("LEADER_NOT_FOUND")
        existing_team = self.session.exec(
            select(TeamMember).where(TeamMember.user_id == leader_id)).first()
        if existing_team:
            raise BusinessRuleError("USER_ALREADY_BELONGS_TO_A_TEAM")

        team = Team(name=name, leader_id=leader_id)
        self.session.add(team)
        self.session.flush()

        # Adicionar líder como membro
        member = TeamMember(team_id=team.id, user_id=leader_id)
        self.session.add(member)
        self.session.commit()
        self.session.refresh(team)

        return team

    def get_by_id(self, team_id: int) -> Optional[Team]:
        team = self.session.get(Team, team_id)
        if not team:
            raise NotFoundError("TEAM_NOT_FOUND")
        return team
        

    def get_all(self) -> List[Team]:
        return self.session.exec(select(Team)).all()

    def update(self, team_id: int, name: Optional[str] = None, leader_id: Optional[int] = None) -> Optional[Team]:
        team = self.get_by_id(team_id)
        if not team:
            raise NotFoundError("NEW_LEADER_NOT_FOUND")

        if name:
            team.name = name

        if leader_id:
            # Verificações similares ao create
            new_leader = self.session.get(User, leader_id)
            if not new_leader:
                raise NotFoundError("NEW_LEADER_NOT_FOUND")
            existing_team = self.session.exec(select(Team).where(Team.leader_id == leader_id)).first()
            if existing_team and existing_team.id != team_id:
                raise BusinessRuleError("USER_IS_ALREADY_LEADING_ANOTHER_TEAM")

            # Remover antigo líder como membro
            old_member = self.session.exec(
                select(TeamMember).where(TeamMember.team_id == team_id, TeamMember.user_id == team.leader_id)
            ).first()
            if old_member:
                self.session.delete(old_member)

            team.leader_id = leader_id

            # Adicionar novo líder como membro
            new_member = TeamMember(team_id=team_id, user_id=leader_id)
            self.session.add(new_member)

        self.session.commit()
        self.session.refresh(team)
        return team

    def delete(self, team_id: int):
        team = self.get_by_id(team_id)
        if team:
            # Remover membros
            self.session.exec(delete(TeamMember).where(TeamMember.team_id == team_id))
            self.session.delete(team)
            self.session.commit()
            return
        raise NotFoundError("TEAM_NOT_FOUND")
