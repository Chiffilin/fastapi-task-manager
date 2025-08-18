from typing import Optional

from pydantic import BaseModel, ConfigDict, field_validator


class TaskBase(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False

    model_config = ConfigDict(from_attributes=True)

    @field_validator("title")
    @classmethod
    def title_validator(cls, v):
        if not v.strip():
            raise ValueError("title cannot be empty")
        return v


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    class TaskUpdate(BaseModel):
        title: Optional[str] = None
        description: Optional[str] = None
        completed: Optional[bool] = None


class TaskOut(TaskBase):
    id: int
