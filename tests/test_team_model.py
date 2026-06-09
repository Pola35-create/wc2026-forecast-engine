from src.db.session import SessionLocal
from src.models.team import Team

session = SessionLocal()

teams = session.query(Team).all()

for t in teams:
    print(t.name, t.rating)

session.close()