from sqlalchemy import Column, Integer, String, Float
from src.db.base import Base

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    country_code = Column(String(3), nullable=False)

    rating = Column(Float, default=1500)

    attack_rating = Column(Float, default=1500)
    defense_rating = Column(Float, default=1500)

    fifa_rank = Column(Integer, nullable=False)
    fifa_points = Column(Float, nullable=False)

    formation_primary = Column(String, nullable=True)

    playstyle_possession = Column(Float, default=1500)
    playstyle_directness = Column(Float, default=1500)
    playstyle_pressing = Column(Float, default=1500)
    playstyle_creativity = Column(Float, default=1500)
    playstyle_physicality = Column(Float, default=1500)