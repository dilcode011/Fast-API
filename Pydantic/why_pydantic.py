def insert_patient_data(name:str,age:int):
    print(name)
    print(age)
    print('Inserted into DB ')

insert_patient_data('dilcode',21)

#We need to implement type checking and validation at the time of function call
#Then we use pydantic 

#Why Need pydantic
#1.Type checking at runtime 
#2.Data Serialization and Deserialization 
#3.Data Validation 
#4.Auto-documentation 
#5.Field Customization
