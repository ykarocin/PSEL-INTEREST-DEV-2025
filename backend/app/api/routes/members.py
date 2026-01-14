from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from typing import List
from app.core.db import get_session
from app.repositories.member_repository import MemberRepository
from app.schemas import MemberCreate, MemberRead

router = APIRouter(prefix="/members", tags=["members"])

@router.post("/", response_model=MemberRead)
def add_member(member: MemberCreate, session: Session = Depends(get_session)):
    repo = MemberRepository(session)
    db_member = repo.add_member(team_id=member.team_id, user_id=member.user_id)
    return db_member

@router.get("/", response_model=List[MemberRead])
def list_members(team_id: int, session: Session = Depends(get_session)):
    repo = MemberRepository(session)
    members = repo.get_members_by_team(team_id=team_id)
    return members

@router.delete("/{team_id}/{user_id}")
def remove_member(team_id: int, user_id: int, session: Session = Depends(get_session)):
    repo = MemberRepository(session)
    repo.remove_member(team_id=team_id, user_id=user_id)
    return {"message": "Member removed successfully"}