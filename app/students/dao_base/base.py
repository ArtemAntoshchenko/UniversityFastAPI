from sqlalchemy.future import select
from app.database import async_session_maker
from app.students.models import Student


class BaseDAO:
    model= None
    