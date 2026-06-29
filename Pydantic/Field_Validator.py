from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
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

@field_validator('email',mode='after')
@classmethod
def email_validator(cls,value):
    valid_domains=["hdfc.com",'icici.com']

    domain_name=value.split('@')[-1]

    if domain_name not in valid_domains:
        raise ValueError('Not a valid domain')

    return value

#Transformation
    @field_validator('name')
    @classmethod
    def name_validator(cls,value):
        return value.upper() 
