from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50,min_length=2,title="Name of the patient",description="Enter name here")]
    email:EmailStr
    linkedin_url:AnyUrl
    age:int=Field(gt=0,lt=100)
    weight:Annotated[float,Field(gt=0,strict=True)]
    married:Annotated[bool,Field(default=False)]
    allergies:Optional[List[str]]=None
    contact_details:Dict[str,str]

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.contact_details)
    print(patient.weight)
    print(patient.married)
    print('Inserted into DB ')

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.contact_details)
    print(patient.weight)
    print(patient.married)
    print('Updated into DB ')

patient_info = {"name":"dilcode","age":21,"weight":65.5,"married":True,"allergies":["dust","food"],"contact_details":{"phone":"1234567890","email":"mann@gmail.com"}}

patient1=Patient(**patient_info)
print(patient1)

insert_patient_data(patient1)
update_patient_data(patient1)
