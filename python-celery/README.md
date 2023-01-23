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
### References:
- [Running Flower in Production](https://testdriven.io/blog/flower-nginx/)
- []()