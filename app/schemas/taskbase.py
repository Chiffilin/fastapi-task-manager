from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, field_validator


class TaskBase(BaseModel):
    title: str = Field(
        ..., min_length=1, max_length=100, examples=["Buy groceries", "Learn FastAPI"]
    )
    description: Optional[str] = Field(
        None, max_length=500, examples=["Milk, eggs, bread", "Study documentation"]
    )
    completed: bool = Field(default=False, examples=[False, True])

    model_config = ConfigDict(from_attributes=True)

    @field_validator("title")
    @classmethod
    def title_validator(cls, v):
        if not v.strip():
            raise ValueError("title cannot be empty")
        return v.strip()


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(
        None, min_length=1, max_length=100, examples=["Updated task"]
    )
    description: Optional[str] = Field(
        None, max_length=500, examples=["Updated description"]
    )
    completed: Optional[bool] = Field(None, examples=[True])

    model_config = ConfigDict(from_attributes=True)

    @field_validator("title")
    @classmethod
    def title_validator(cls, v):
        if v is not None and not v.strip():
            raise ValueError("title cannot be empty")
        return v.strip() if v else v


class TaskOut(TaskBase):
    id: int = Field(examples=[1, 2, 3])
    created_at: datetime = Field(examples=["2024-01-15T10:30:00Z"])
    updated_at: Optional[datetime] = Field(None, examples=["2024-01-15T11:00:00Z"])

    model_config = ConfigDict(from_attributes=True)
