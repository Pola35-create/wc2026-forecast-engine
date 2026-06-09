from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.db.base import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)
    country = Column(String, nullable=False)

    position = Column(String, nullable=False)
    age = Column(Integer, nullable=True)

    overall_rating = Column(Float, default=1500)
    attack_rating = Column(Float, default=1500)
    midfield_rating = Column(Float, default=1500)
    defense_rating = Column(Float, default=1500)

    team_id = Column(Integer, ForeignKey("teams.id"))