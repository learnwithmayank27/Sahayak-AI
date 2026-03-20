from sqlalchemy.orm import Session
from app.db.sql.models import User

def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, username: str, password: str, role: str):
    user = User(username=username, password=password, role=role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
