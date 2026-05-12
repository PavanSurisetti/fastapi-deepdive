from fastapi import FastAPI
from fastapi import Path# if u want to deal with the advanced concept like description,validation
app=FastAPI()#application created here
@app.get('/')
def Welcome():
    return {'Hey Welcome to FastAPI'}
fruits=['Apple','Banana','Orange']
@app.get('/info/{val}')#if the name here and function parameter does not match FastAPI does not work
def info(val:int=Path(...,description='order fruits which u want',ge=0,le=2)):#here val and endpoint val should be same name
    return{f'Your Selected fruit is:{fruits[val]}'}