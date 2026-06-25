# pyrefly: ignore [missing-import]
from fastapi import FastAPI
import json

app= FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data= json.load(f)
        return data

@app.get('/')
def patient():
    return{"message": "Patient Management System"}

@app.get("/about")
def about():
    return {"about":"A functional API to manage your patient records"}

@app.get('/view')
def view():
    data = load_data()
    return data

@app.get('/view/{id}')
def view_by_id(id: int):
    data = load_data()
    for patient in data:
        if patient['id'] == id:
            return patient
    return {"message": "Patient not found"}


