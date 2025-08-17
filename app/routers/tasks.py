from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from sqlalchemy.orm import Session

from app.crud.tasks import (
    create_task,
    get_task_by_id,
    get_tasks,
    update_task,
    delete_task,
)
from app.db.database import get_db
from app.schemas.taskbase import TaskCreate, TaskOut, TaskUpdate

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def create_new_task(task: TaskCreate, db: Session = Depends(get_db)):
    """
    Creates a new task.
    """
    return create_task(db=db, task=task)


@router.get("/{task_id}", response_model=TaskOut)
def read_task_by_id(task_id: int, db: Session = Depends(get_db)):
    """
    Retrieves a single task by its ID.
    :param task_id: The ID of the task.
    :param db: The DB session object.
    :return: The task object.
    """
    db_task = get_task_by_id(db=db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


@router.get("/", response_model=List[TaskOut])
def read_all_tasks(db: Session = Depends(get_db)):
    """
    Retrieves a list of all tasks.
    """
    return get_tasks(db)


@router.put("/{task_id}", response_model=TaskOut)
def update_existing_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    """
    Updates an existing task by its ID.
    """
    db_task = update_task(task_id=task_id, task_data=task, db=db)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_task(task_id: int, db: Session = Depends(get_db)):
    """
    Deletes a task by its ID.
    """
    db_task = delete_task(task_id=task_id, db=db)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return
