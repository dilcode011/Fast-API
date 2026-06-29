from pydantic import BaseModel


class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address:Address
address_dict={
    "city":"Bangalore",
    "state":"Karnataka",
    "pin":"560001"
}
patient_dict={
    "name":"dil",
    "gender":"male",
    "age":21,
    "address":address_dict
}

address1=Address(**address_dict)
print(address1)

patient1=Patient(**patient_dict)
print(patient1)