# pyrefly: ignore [missing-import]
from fastapi import FastAPI, Path
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

@app.get('/patients/{id}')
def view_by_id(id: str = Path(...,description="Enter the ID of the patient you want to view",example="P001")):
    data = load_data()
    for patient in data:
        if patient['id'] == id:
            return patient
    return {"message": "Patient not found"}