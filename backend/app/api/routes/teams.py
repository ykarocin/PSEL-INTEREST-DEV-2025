from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select, delete
from typing import List

from app.core.db import get_session
from app.schemas import TeamCreate, TeamRead, TeamUpdate
from app.repositories.team_repository import TeamRepository
from app.exceptions import NotFoundError

router = APIRouter(prefix="/teams", tags=["teams"])

@router.post("/", response_model=TeamRead)
def create_team(team: TeamCreate, session: Session = Depends(get_session)):
    repo = TeamRepository(session)
    
    try:
        return repo.create(name=team.name, leader_id=team.leader_id)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[TeamRead])
def list_teams(session: Session = Depends(get_session)):
    repo = TeamRepository(session)
    return repo.get_all()

@router.get("/{team_id}", response_model=TeamRead)
def get_team(team_id: int, session: Session = Depends(get_session)):
    repo = TeamRepository(session)
    team = repo.get_by_id(team_id)
    
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    
    return team

@router.put("/{team_id}", response_model=TeamRead)
def update_team(team_id: int, team_update: TeamUpdate, session: Session = Depends(get_session)):
    repo = TeamRepository(session)
    
    try:
        team = repo.update(team_id=team_id, name=team_update.name, leader_id=team_update.leader_id)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    
    return team

@router.delete("/{team_id}")
def delete_team(team_id: int, session: Session = Depends(get_session)):
    repo = TeamRepository(session)
    
    deleted = repo.delete(team_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Team not found")
    
    return {"message": "Team deleted successfully"}