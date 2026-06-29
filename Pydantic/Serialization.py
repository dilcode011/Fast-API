from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str = 'Male'
    age: int
    address: Address

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'dilpreet', 'age': 21, 'address': address1}

patient1 = Patient(**patient_dict)

temp=patient1.model_dump(exclude_unset=True) #exclude unassigned field 

temp=patient1.model_dump(exclude=["address"])  #Exclude fields

temp=patient1.model_dump(include=["name","age"]) #multiple fields can be included

print(temp)
print(type(temp))