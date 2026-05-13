from fastapi import FastAPI
from fastapi import Path#this is used to add the extra stuff like validation
app=FastAPI()
@app.get('/')
def welcome():
    return {'Welcome Ganesha!'}
@app.get('/fav_lan/{subject}')
def fav_lan(subject:str):
    return {f'Your Favourite Subject is :{subject}'}
@app.get('/search/')
def search(*,name:str=None,age:int=None,city:str):
    return {f'Name:{name},age:{age},city:{city}'}
'''
you can observe the output in the http://127.0.0.1:8000 here you can go through different end points
http://127.0.0.1:8000/search/?age=30 this is how you can give the query parameters 
you can view in the http://127.0.0.1:8000/docs 
here the subject is mandatory parameter-->path parameter but name,age,city are not mandatory you can give or not -->query parameter
'''