from fastapi import FastAPI
from celery import Celery
from celery.result import AsyncResult


app = FastAPI()

# Initialize Celery
celery_app = Celery('tasks',
                    broker='redis://localhost:6379/0',  # broker URL
                    backend='redis://localhost:6379/1',  # backend URL
)
celery_app.conf.task_routes = {'tasks.add': 'main-queue'}


# Define a Celery task
@celery_app.task
def add(x, y):
    return x + y


# Define a FastAPI route that sends a task to Celery
@app.get("/add/{x}/{y}")
async def read_item(x: int, y: int):
    result = add.delay(x, y)
    return {"task_id": result.id, "status": result.status}


# Define a FastAPI route that checks the status of a task
@app.get("/status/{task_id}")
async def read_item(task_id: str):
    result = AsyncResult(task_id, app=celery_app)
    return {"status": result.status}