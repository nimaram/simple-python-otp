from app.db.session import SessionLocal
from app.db.models.user import User
from sqlalchemy.orm import Session
from datetime import datetime

def get_or_create_user(phone: str) -> User:
    db: Session = SessionLocal()
    user = db.query(User).filter(User.phone == phone).first()
    if not user:
        user = User(phone=phone, created_at=datetime.utcnow())
        db.add(user)
        db.commit()
        db.refresh(user)
    return user