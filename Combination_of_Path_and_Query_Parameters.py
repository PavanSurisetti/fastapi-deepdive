'''
Create a FastAPI endpoint /student/{student_id} 
where student_id is a mandatory path parameter (int),
 and name (string, optional), age (int, optional), 
 and branch (string, mandatory) are query parameters; 
 the API should return all provided values in a JSON response, 
 showing None for optional fields if not given, and 
 FastAPI should automatically raise an error if branch is missing.
'''
from fastapi import FastAPI
from fastapi import Path#used to handle the advanced concepts like minimum and maximum vaules
from fastapi import Query
app=FastAPI()
#application created succesfully
@app.get('/')
def welcome():
    return{'Hello Welcome Student Details API'}
@app.get('/student/{student_id}')
def details(*,student_id:int=Path(gt=0),name:str=None,age:int =Query(None,lt=30 ,gt=17),branch:str):
      return{
           'Student_id':student_id,
            'Name':name,
            'Age':age,
            'Branch':branch
       }
    