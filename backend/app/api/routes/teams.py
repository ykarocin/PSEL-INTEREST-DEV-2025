from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select, delete
from typing import List

from app.core.db import get_session
from app.models import Team, User, TeamMember
from app.schemas import TeamCreate, TeamRead, TeamUpdate

router = APIRouter(prefix="/teams", tags=["teams"])

@router.post("/", response_model=TeamRead)
def create_team(team: TeamCreate, session: Session = Depends(get_session)):
    # Verificar se o líder existe
    leader = session.get(User, team.leader_id)
    if not leader:
        raise HTTPException(status_code=404, detail="Leader not found")
    
    # Verificar se o líder já lidera outra equipe
    existing_team = session.exec(select(Team).where(Team.leader_id == team.leader_id)).first()
    if existing_team:
        raise HTTPException(status_code=400, detail="User is already leading another team")
    
    # Criar equipe
    db_team = Team(name=team.name, leader_id=team.leader_id)
    session.add(db_team)
    session.commit()
    session.refresh(db_team)
    
    # Adicionar líder como membro automaticamente
    member = TeamMember(team_id=db_team.id, user_id=team.leader_id)
    session.add(member)
    session.commit()
    
    # Carregar relacionamentos para resposta
    team_with_relations = session.exec(
        select(Team).where(Team.id == db_team.id)
    ).first()
    return team_with_relations

@router.get("/", response_model=List[TeamRead])
def list_teams(session: Session = Depends(get_session)):
    teams = session.exec(select(Team)).all()
    return teams

@router.get("/{team_id}", response_model=TeamRead)
def get_team(team_id: int, session: Session = Depends(get_session)):
    team = session.get(Team, team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team

@router.put("/{team_id}", response_model=TeamRead)
def update_team(team_id: int, team_update: TeamUpdate, session: Session = Depends(get_session)):
    team = session.get(Team, team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    
    update_data = team_update.model_dump(exclude_unset=True)
    
    if "leader_id" in update_data:
        new_leader_id = update_data["leader_id"]
        # Verificar se novo líder existe
        new_leader = session.get(User, new_leader_id)
        if not new_leader:
            raise HTTPException(status_code=404, detail="New leader not found")
        
        # Verificar se novo líder já lidera outra equipe
        existing_team = session.exec(select(Team).where(Team.leader_id == new_leader_id)).first()
        if existing_team and existing_team.id != team_id:
            raise HTTPException(status_code=400, detail="User is already leading another team")
        
        # Remover antigo líder como membro (se não for mais membro)
        old_leader_member = session.exec(
            select(TeamMember).where(TeamMember.team_id == team_id, TeamMember.user_id == team.leader_id)
        ).first()
        if old_leader_member:
            session.delete(old_leader_member)
        
        # Adicionar novo líder como membro
        new_member = TeamMember(team_id=team_id, user_id=new_leader_id)
        session.add(new_member)
    
    for key, value in update_data.items():
        setattr(team, key, value)
    
    session.commit()
    session.refresh(team)
    return team

@router.delete("/{team_id}")
def delete_team(team_id: int, session: Session = Depends(get_session)):
    team = session.get(Team, team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    
    # Remover membros associados
    session.exec(delete(TeamMember).where(TeamMember.team_id == team_id))
    
    session.delete(team)
    session.commit()
    return {"message": "Team deleted successfully"}