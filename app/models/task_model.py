from sqlalchemy import Boolean, Column, Integer, String

from app.db.database import Base


class Task(Base):
    __tablename__: str = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
