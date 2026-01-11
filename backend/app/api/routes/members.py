from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.core.db import get_session
from app.repositories.member_repository import MemberRepository
from app.schemas import MemberCreate, MemberRead
from app.exceptions import NotFoundError

router = APIRouter(prefix="/members", tags=["members"])

@router.post("/", response_model=MemberRead)
def add_member(member: MemberCreate, session: Session = Depends(get_session)):
    repo = MemberRepository(session)
    try:
        db_member = repo.add_member(team_id=member.team_id, user_id=member.user_id)
        return db_member
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{team_id}/{user_id}")
def remove_member(team_id: int, user_id: int, session: Session = Depends(get_session)):
    repo = MemberRepository(session)
    try:
        repo.remove_member(team_id=team_id, user_id=user_id)
        return {"message": "Member removed successfully"}
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))