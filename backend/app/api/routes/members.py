from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.core.db import get_session
from app.models import TeamMember, User, Team
from app.schemas import MemberCreate, MemberRead

router = APIRouter(prefix="/members", tags=["members"])

@router.post("/", response_model=MemberRead)
def add_member(member: MemberCreate, session: Session = Depends(get_session)):
    # Verificar se a equipe existe
    team = session.get(Team, member.team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    
    # Verificar se o usuário existe
    user = session.get(User, member.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Verificar se o usuário já está em alguma equipe
    existing_member = session.exec(
        select(TeamMember).where(TeamMember.user_id == member.user_id)
    ).first()
    if existing_member:
        raise HTTPException(status_code=400, detail="User is already a member of another team")
    
    # Adicionar membro
    db_member = TeamMember(team_id=member.team_id, user_id=member.user_id)
    session.add(db_member)
    session.commit()
    session.refresh(db_member)
    return db_member

@router.delete("/{team_id}/{user_id}")
def remove_member(team_id: int, user_id: int, session: Session = Depends(get_session)):
    # Verificar se a equipe existe
    team = session.get(Team, team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    
    # Verificar se o usuário é o líder (não permitir remover líder)
    if team.leader_id == user_id:
        raise HTTPException(status_code=400, detail="Cannot remove the team leader")
    
    # Verificar se o membro existe na equipe
    member = session.exec(
        select(TeamMember).where(
            TeamMember.team_id == team_id,
            TeamMember.user_id == user_id
        )
    ).first()
    if not member:
        raise HTTPException(status_code=404, detail="Member not found in this team")
    
    # Remover membro
    session.delete(member)
    session.commit()
    return {"message": "Member removed successfully"}