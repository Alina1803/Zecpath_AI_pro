from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:Alina1803@localhost:5432/ai_pipeline"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)