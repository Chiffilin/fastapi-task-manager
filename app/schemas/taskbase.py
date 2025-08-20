from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator


class TaskBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
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
        title: Optional[str] = Field(None, min_length=1, max_length=100)
        description: Optional[str] = Field(None, max_length=500)
        completed: Optional[bool] = None


class TaskOut(TaskBase):
    id: int
