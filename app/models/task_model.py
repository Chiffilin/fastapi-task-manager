from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.sql import func

from app.db.database import Base


class Task(Base):
    __tablename__: str = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), index=True, nullable=False)  # Length limitation
    description = Column(String(500), nullable=True)  # Length limitation
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<Task(id={self.id}, title='{self.title}', completed={self.completed})>"
