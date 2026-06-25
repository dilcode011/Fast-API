# pyrefly: ignore [missing-import]
from fastapi import FastAPI

app= FastAPI()

@app.get('/')
def hello():
    return{"message": "hello world"}

@app.get("/about")
def about():
    return {"about":"I am fast api learner"}