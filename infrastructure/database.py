from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from domain.models import Base
import os
from dotenv import load_dotenv

load_dotenv(override=True)

db_uri = os.getenv("DB_URI")
DATABASE_URL = f"mysql+pymysql://{db_uri}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()