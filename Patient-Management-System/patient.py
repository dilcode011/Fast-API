# pyrefly: ignore [missing-import]
from fastapi import FastAPI, Path , Query ,HTTPException
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



#QUERY PARAMETER
@app.get('/sort')
def sort_patients(sort_by:str= Query(...,description='You can sort the records by any one of the following parameters. They are name,age,city,department and consultation fee'),order: str=Query('asc',description='Enter the order in which you want to sort the records. They are asc and desc',enum=['asc','desc'])):

    valid_fields = ['height','weight','bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f'Invalid sort parameter.Please use one of these{valid_fields}')
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail=f'Invalid order parameter.Please use one of these{['asc','desc']}')
    
    data = load_data()
    sort_order = True if order == 'desc' else False
    sorted_Data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)
    return sorted_Data