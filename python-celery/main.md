Run docker-compose to create redis:
```commandline
docker-compose up -d
```
Run FastAPI app:
```python
uvicorn main:app --reload
```
In case needed, install celery:
```commandline
pip install fastapi celery[redis]
```
Run celery:
```commandline
celery -A main.celery_app worker --loglevel=info
```
