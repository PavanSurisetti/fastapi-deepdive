from pydantic import BaseModel#this is used to convert the JSON->Python object
from fastapi import FastAPI
from fastapi import Path
from typing import Optional
app=FastAPI()
#application created successfully 
class Details(BaseModel):
    name:str
    age:int
    branch:str
    email:Optional[str]=None#this is an optional parameter
students_list=[]#this is  a temporary storage to view 
@app.get('/')
def welcome():
    return{'Hello Welcome to POST Method Concept'}
@app.post('/Regsiter')
def registration(info:Details):
    '''
                What it means:
                Details = Pydantic class (structure)
                info = variable (object)
                🧠 Internally FastAPI does this:

                If user sends:

                {
                "name": "chinnu",
                "age": 20,
                "branch": "CSE"
                }

                👉 FastAPI converts it to:

                info = Details(name="chinnu", age=20, branch="CSE")
    '''
    students_list.append(info)
    return{
        'Message':'Registration done Successfully',
        'data':info,
    }
@app.get('/fecth')
def fetch():
    return{f'There is a User :{students_list}'}