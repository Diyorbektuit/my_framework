from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# PostgreSQL ulanish stringi
DATABASE_URL = "postgresql://diyorbek0906:diyorbek0906@localhost:5432/my_test"

# Engine va session yaratish
engine = create_engine(DATABASE_URL, echo=True)  # echo=True - SQL so'rovlarini konsolda ko'rish
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base klassi, undan barcha model klasslari meros oladi
Base = declarative_base()

# Sessionni yaratish va unga ulanish
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
