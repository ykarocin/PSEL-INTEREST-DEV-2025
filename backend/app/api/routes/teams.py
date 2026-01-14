from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select, delete
from typing import List

from app.core.db import get_session
from app.schemas import TeamCreate, TeamRead, TeamUpdate
from app.repositories.team_repository import TeamRepository

router = APIRouter(prefix="/teams", tags=["teams"])

@router.post("/", response_model=TeamRead)
def create_team(team: TeamCreate, session: Session = Depends(get_session)):
    repo = TeamRepository(session)
    return repo.create(name=team.name, leader_id=team.leader_id)

@router.get("/", response_model=List[TeamRead])
def list_teams(session: Session = Depends(get_session)):
    repo = TeamRepository(session)
    return repo.get_all()

@router.get("/{team_id}", response_model=TeamRead)
def get_team(team_id: int, session: Session = Depends(get_session)):
    repo = TeamRepository(session)
    return repo.get_by_id(team_id)

@router.put("/{team_id}", response_model=TeamRead)
def update_team(team_id: int, team_update: TeamUpdate, session: Session = Depends(get_session)):
    repo = TeamRepository(session)
    return repo.update(team_id=team_id, name=team_update.name, leader_id=team_update.leader_id)

@router.delete("/{team_id}")
def delete_team(team_id: int, session: Session = Depends(get_session)):
    repo = TeamRepository(session)
    repo.delete(team_id)
    return {"message": "Team deleted successfully"}