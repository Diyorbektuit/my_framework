from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from Database.db import Base, get_db
import uuid


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(DateTime, default=func.now())

    @classmethod
    def create_user(cls, username, email, password=None):
        if password is None:
            password = str(uuid.uuid4())
        db = next(get_db())
        db_user = User(username=username, email=email, password=password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @classmethod
    def get_users(cls):
        db = next(get_db())
        user = db.query(cls).all()
        return user

    @classmethod
    def get_user_by_id(cls, user_id):
        db = next(get_db())
        user = db.query(User).filter(User.id == user_id).first()

        return user

