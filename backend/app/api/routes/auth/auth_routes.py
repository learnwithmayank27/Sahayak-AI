from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.sql.database import SessionLocal
from app.db.sql import crud
from app.auth.security import hash_password, verify_password
from app.auth.jwt_handler import create_token
from app.schemas.user_schema import UserCreate, UserLogin

router = APIRouter()

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing = crud.get_user(db, user.username)

    if existing:
        return {"error": "User already exists"}

    hashed = hash_password(user.password)
    crud.create_user(db, user.username, hashed, user.role)

    return {"message": "User created successfully"}


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user.username)

    if not db_user:
        return {"error": "User not found"}

    if not verify_password(user.password, db_user.password):
        return {"error": "Invalid password"}

    token = create_token({
        "username": db_user.username,
        "role": db_user.role
    })

    return {"access_token": token}
