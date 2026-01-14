from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List

from app.core.db import get_session
from app.models import User
from app.schemas import UserCreate, UserRead, UserUpdate
from app.repositories.user_repository import UserRepository

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, session: Session = Depends(get_session)):
    repo = UserRepository(session)
    return repo.create(user.name)

@router.get("/", response_model=List[UserRead])
def list_users(session: Session = Depends(get_session)):
    repo = UserRepository(session)
    return repo.get_all()

@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: int, session: Session = Depends(get_session)):
    repo = UserRepository(session)
    return repo.get_by_id(user_id)

@router.put("/{user_id}", response_model=UserRead)
def update_user(user_id: int, user_update: UserUpdate, session: Session = Depends(get_session)):
    repo = UserRepository(session)
    data = user_update.model_dump(exclude_unset=True)
    return repo.update(user_id, data)

@router.delete("/{user_id}")
def delete_user(user_id: int, session: Session = Depends(get_session)):
    repo = UserRepository(session)
    repo.delete(user_id)
    return {"message": "User deleted successfully"}