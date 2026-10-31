from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models, schemas


def create_task(db: Session, task_data: schemas.TaskCreate) -> models.Task:

    task = models.Task(**task_data.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)

    return task

def get_task(db: Session, task_id: int) -> models.Task:
    task = db.get(models.Task, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

def get_all_tasks(db: Session) -> list[models.Task]:

    tasks = db.query(models.Task).all()

    return tasks 



