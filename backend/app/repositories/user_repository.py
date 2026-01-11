from sqlmodel import Session, select
from typing import List, Optional
from app.models import User

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, name: str) -> User:
        user = User(name=name)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def get_by_id(self, user_id: int) -> Optional[User]:
        return self.session.get(User, user_id)

    def get_all(self) -> List[User]:
        return self.session.exec(select(User)).all()

    def update(self, user_id: int, data: dict) -> Optional[User]:
        user = self.get_by_id(user_id)
        
        for key,value in data.items():
            setattr(user, key, value)
            
        self.session.commit()
        self.session.refresh(user)
        return user

    def delete(self, user: User):
        self.session.delete(user)
        self.session.commit()
        return
