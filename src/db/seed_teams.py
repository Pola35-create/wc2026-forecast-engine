from src.db.session import SessionLocal
from src.models.team import Team

session = SessionLocal()

teams_data = [
    Team(name="France", country_code="FRA", rating=1850, attack_rating=1880, defense_rating=1800, fifa_rank = 3, fifa_points = 1870.70),
    Team(name="Brazil", country_code="BRA", rating=1830, attack_rating=1900, defense_rating=1820, fifa_rank = 6, fifa_points = 1765.86),
    Team(name="Germany", country_code="GER", rating=1780, attack_rating=1740, defense_rating=1820, fifa_rank = 10, fifa_points = 1735.77),
]

session.add_all(teams_data)
session.commit()
session.close()