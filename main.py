from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from database import database
from models import tasks

app = FastAPI(title="msn")

class TaskIn(BaseModel):
    title: str
    description: str = ""
    done: bool = False

class Task(TaskIn):
    id: int

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/tasks/", response_model=Task)
async def create_task(task: TaskIn):
    query = tasks.insert().values(
        title=task.title,
        description=task.description,
        done=task.done
    )
    last_record_id = await database.execute(query)
    return {**task.dict(), "id": last_record_id}

@app.get("/tasks/", response_model=List[Task])
async def read_tasks():
    query = tasks.select()
    return await database.fetch_all(query)

@app.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: int):
    query = tasks.select().where(tasks.c.id == task_id)
    task = await database.fetch_one(query)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task: TaskIn):
    query = tasks.update().where(tasks.c.id == task_id).values(
        title=task.title,
        description=task.description,
        done=task.done
    )
    await database.execute(query)
    return {**task.dict(), "id": task_id}

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    query = tasks.delete().where(tasks.c.id == task_id)
    await database.execute(query)
    return {"message": f"Task {task_id} deleted"}
