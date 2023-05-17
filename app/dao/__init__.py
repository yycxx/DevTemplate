from app.models import Base, engine
from app.models.user import User

#
Base.metadata.create_all(engine)
