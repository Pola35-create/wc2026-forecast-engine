from src.db.base import Base
from src.db.session import engine
from src.models.team import Team

Base.metadata.create_all(bind=engine)
print("DB initialized")