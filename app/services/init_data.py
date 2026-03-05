# Bad (circular import):
from app import db

db.session.commit()  # runs on import → triggers errors

# Good:
def add_initial_data():
    from app import db
    from ..models import MissionGoal
    goal = MissionGoal(target_ksh=500000, target_usd=3000)
    db.session.add(goal)
    db.session.commit()
