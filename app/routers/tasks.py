# app/routers/tasks.py
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

# It's assumed the crud functions are also async
from app.crud.tasks import (
    create_task,
    delete_task,
    get_task_by_id,
    get_tasks,
    update_task,
)
from app.db.database import get_db_session
from app.schemas.taskbase import TaskCreate, TaskOut, TaskUpdate

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
async def create_new_task(task: TaskCreate, db: AsyncSession = Depends(get_db_session)):
    """
    Creates a new task.
    """
    return await create_task(db=db, task=task)


@router.get("/{task_id}", response_model=TaskOut)
async def read_task_by_id(task_id: int, db: AsyncSession = Depends(get_db_session)):
    """
    Retrieves a single task by its ID.
    :param task_id: The ID of the task.
    :param db: The asynchronous DB session object.
    :return: The task object.
    """
    db_task = await get_task_by_id(db=db, task_id=task_id)
    if db_task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )
    return db_task


@router.get("/", response_model=List[TaskOut])
async def read_all_tasks(
    db: AsyncSession = Depends(get_db_session), completed: Optional[bool] = None
):
    """
    Retrieves a list of all tasks.
    """
    return await get_tasks(db, completed=completed)


@router.put("/{task_id}", response_model=TaskOut)
async def update_existing_task(
    task_id: int, task: TaskUpdate, db: AsyncSession = Depends(get_db_session)
):
    """
    Updates an existing task by its ID.
    """
    db_task = await update_task(task_id=task_id, task_data=task, db=db)
    if db_task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )
    return db_task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_existing_task(
    task_id: int, db: AsyncSession = Depends(get_db_session)
):
    """
    Deletes a task by its ID.
    """
    db_task = await delete_task(task_id=task_id, db=db)
    if db_task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )
    return
