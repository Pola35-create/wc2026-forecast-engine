from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///wc2026.db", echo=False)
SessionLocal = sessionmaker(bind=engine)