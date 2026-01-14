from sqlmodel import Session, select
from typing import List, Optional
from app.models import User
from app.exceptions import NotFoundError, BusinessRuleError

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, name: str) -> User:
        if not name.strip():
            raise BusinessRuleError("USER_NAME_REQUIRED")
        user = User(name=name)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def get_by_id(self, user_id: int) -> Optional[User]:
        user =  self.session.get(User, user_id)
        if not user:
            raise NotFoundError("USER_NOT_FOUND")
        return user

    def get_all(self) -> List[User]:
        return self.session.exec(select(User)).all()

    def update(self, user_id: int, data: dict) -> Optional[User]:
        user = self.get_by_id(user_id)
        
        for key,value in data.items():
            setattr(user, key, value)
            
        self.session.commit()
        self.session.refresh(user)
        return user

    def delete(self, user_id: int):
        user = self.get_by_id(user_id)
        if not user:
            raise NotFoundError("USER_NOT_FOUND")
        self.session.delete(user)
        self.session.commit()
        return
