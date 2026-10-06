from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base, Session

DATABASE_URL = "sqlite:///./url_data.db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class urlshort(Base):
    __tablename__ = "urlist"

    id = Column(Integer, primary_key=True , index=True)

    long_url = Column(String)

    short_id = Column(String)


Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()