from fastapi import FastAPI
app=FastAPI()#this is used for the creation of a application
@app.get('/')
def hi():
    return {'Hello World'}