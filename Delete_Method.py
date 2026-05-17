from fastapi import FastAPI
app=FastAPI()
#application created successfully
students=[
    {'id':1,'name':'Ganesha','Age':18},
    {'id':2,'name':'Pavan','Age':19}
]
@app.get('/')
def welcome():
    return {'Welcome to the DELETE Method Concept'}
@app.get('/student/{id}')
def data(id:int):
    for i in students:
        if(i['id']==id):
            return i
    return{'Not Found'}
@app.delete('/delete/{id}')
def deleting(id:int):
    for i in students:
        if(i['id']==id):
            students.remove(i)
            return {'Message':'Deleted successfully'}
    return{'Not Found'}