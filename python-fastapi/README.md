# How to work with FastAPI?
This is the script to begins:
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```
To run the script:
```commandline
$ uvicorn main:app --reload
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
In case you may need to install `uvicorn`
```commandline
sudo apt install uvicorn
```
You can run your project using python instead of unicorn using this code:
```python
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8100)
```
You can also change default port using above command.

### References:
- [First Steps¶](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [How to run FastAPI app on multiple ports?](https://stackoverflow.com/questions/69641363/how-to-run-fastapi-app-on-multiple-ports)
- []()
- []()
- []()
- []()