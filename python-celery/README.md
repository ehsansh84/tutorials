# Hello python celery!

```
$ docker-compose build
$ docker-compose up -d --build
$ docker-compose exec worker python

>> from app import add
>> task = add.delay(5, 5)
>>>
>>> task.status
'SUCCESS'
>>> task.result
10
```
### How to config Celery?
Define in app:
```python
app = Celery(
    'tasks', # app name
    broker='redis://localhost:6379/0', # broker URL
    backend='redis://localhost:6379/1', # backend URL
    include=['tasks'] # list of task modules
)
```
Update app directly:
```python
app.conf.update(
    result_expires=3600,
    task_serializer='json',
    result_serializer='json',
    accept_content=['json'],
    timezone='UTC'
)
```
Update from object. Create a file named `config.py` like this:
```python
broker_url = 'redis://localhost:6379/0'
result_backend = 'redis://localhost:6379/1'
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Europe/London'
enable_utc = True
task_routes = {'tasks.add': 'main-queue'}
```
and update app this way:
```python
app.config_from_object('config')
```
### References:
- [Running Flower in Production](https://testdriven.io/blog/flower-nginx/)
- []()