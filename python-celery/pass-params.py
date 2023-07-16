from celery import Celery, chain
from kombu import Queue


celery_app = Celery('tasks',
                    broker='redis://localhost:6379/0',  # broker URL
                    backend='redis://localhost:6379/1',  # backend URL
)

celery_app.conf.task_routes = {
    'celery_app.task1': {'queue': 'task1-queue'},
    'celery_app.task2': {'queue': 'task2-queue'},
    'celery_app.task3': {'queue': 'task3-queue'},
}

celery_app.conf.task_queues = (
    Queue('task1-queue', routing_key='task1-queue'),
    Queue('task2-queue', routing_key='task2-queue'),
    Queue('task3-queue', routing_key='task3-queue'),
)


@celery_app.task(name='task1')
def task1(name):
    return f'Hello {name}'


@celery_app.task(name='task2')
def task2(message):
    return message, f'Previous message is: {message}'


@celery_app.task(name='task3')
def task3(name, message):
    return f'{name} Previous message is: {message}'


t1 = celery_app.signature('task1', args=["Ehsan", ]).set(queue="task1-queue")
t2 = celery_app.signature('task2').set(queue="task2-queue")
t3 = celery_app.signature('task3').set(queue="task3-queue")
chain_of_tasks = chain(t1, t2, t3)
result = chain_of_tasks.apply_async()






# from fastapi import FastAPI
# from celery import Celery, chain
# from kombu import Queue
#
# app = FastAPI()
#
# celery_app = Celery('tasks',
#                     broker='redis://localhost:6379/0',  # broker URL
#                     backend='redis://localhost:6379/1',  # backend URL
# )
#
# celery_app.conf.task_routes = {
#     'tasks.task1': {'queue': 'task1-queue'},
#     'tasks.task2': {'queue': 'task2-queue'},
#     'tasks.task3': {'queue': 'task3-queue'},
# }
#
# celery_app.conf.task_queues = (
#     Queue('task1-queue', routing_key='task1-queue'),
#     Queue('task2-queue', routing_key='task2-queue'),
#     Queue('task3-queue', routing_key='task3-queue'),
# )
#
#
# @celery_app.task(name='tasks.task1')
# def task1(name):
#     return f'Hello {name}'
#
#
# @celery_app.task(name='tasks.task2')
# def task2(message):
#     return f'Previous message is: {message}', f'This is task2 result'
#
#
# @celery_app.task(name='tasks.task3')
# def task3(previous_message, task2_result):
#     return f'{previous_message} Task2 result: {task2_result}'
#
#
# t1 = celery_app.signature('tasks.task1', args=["Ehsan"]).set(queue="task1-queue")
# t2 = celery_app.signature('tasks.task2').set(queue="task2-queue")
# t3 = celery_app.signature('tasks.task3').set(queue="task3-queue")
#
# # Define the callback function for task2 result
# def callback_task2_result(task2_result):
#     previous_message, _ = task2_result.get()  # Get the result of task2
#     t3_with_args = t3.clone(args=[previous_message, 'Task3 argument'])  # Create a new signature of task3 with the result
#     t3_with_args.apply_async()
#
# # Chain the tasks and set the callback
# chain_of_tasks = chain(t1, t2, link=callback_task2_result)
# result = chain_of_tasks.apply_async()
