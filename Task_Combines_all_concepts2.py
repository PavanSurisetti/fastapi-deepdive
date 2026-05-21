# 🧪 FINAL TASK: 📚 Book Management API (CRUD + PATCH + FILTER)
# 🧠 Goal

# Build a complete API using:

# ✅ Path parameters
# ✅ Query parameters
# ✅ POST, GET, PUT, DELETE
# ✅ PATCH (partial update 🔥)
# ✅ Pydantic (request body)
# 🏗️ DATA MODEL
# {
#   "title": "string",
#   "author": "string",
#   "price": float,
#   "in_stock": true
# }

# 👉 Store everything in a list

# 📌 REQUIREMENTS
# 1️⃣ POST → Add Book
# POST /books

# 👉 Add new book
# 👉 Prevent duplicate titles ⚠️
# 👉 Return 201 status

# 2️⃣ GET → All Books
# GET /books

# 👉 Return all books

# 3️⃣ GET → Single Book
# GET /books/{title}

# 👉 Use path parameter
# 👉 If not found → 404

# 4️⃣ GET → Search (Query Params 🔥)
# GET /search?author=xyz&in_stock=true

# 👉 Query params:

# author (optional)
# in_stock (optional)
# 🔹 Rules

# ✔ If both given → match both
# ✔ If one → filter accordingly
# ✔ If none → return all books

# 🔹 Response
# {
#   "count": 2,
#   "data": [ ... ]
# }
# 5️⃣ PUT → Full Update
# PUT /books/{title}

# 👉 Replace entire book
# 👉 If not found → 404

# 6️⃣ PATCH → Partial Update 🔥🔥
# PATCH /books/{title}

# 👉 Update ONLY given fields

# 🔹 Example Body
# {
#   "price": 499
# }
# 🔹 Rules

# ✔ Don’t overwrite missing fields
# ✔ Only update what user sends
# ✔ If not found → 404

# 7️⃣ DELETE → Remove Book
# DELETE /books/{title}

# 👉 Delete book
# 👉 Return confirmation
# 👉 If not found → 404

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from fastapi import Query
app=FastAPI()
#app created successfully
class DataModel(BaseModel):
    title:Optional [str]=None
    author:Optional[str]=None
    price:Optional[float]=None
    stock:Optional[bool]=None
books=[
    {'title':'StockMarket','author':'Ganesha','price':450.56,'stock':True},
    {'title':'IDS','author':'Pavan','price':250.56,'stock':True},
    {'title':'BhagavadGita','author':'Valmiki','price':2450.56,'stock':False}
]
@app.get('/')
def home():
    return'Welcome to Book Management'
#3
@app.get('/books/{title}')
def get_a_book(title:str):
    for i in books:
        if(i['title']==title):
            return i
    return 'Not found bro!'
#2
@app.get('/books')
def get_all_books():
    return books
@app.get('/search')#query parameters
#4
@app.get('/search')
def search(author: str = None, stock: bool = None):
    result = []

    for i in books:
        if author is not None and stock is not None:
            if i['author'] == author and i['stock'] == stock:
                result.append(i)

        elif author is not None:
            if i['author'] == author:
                result.append(i)

        elif stock is not None:
            if i['stock'] == stock:
                result.append(i)

    # if no filters → return all
    if author is None and stock is None:
        return {"count": len(books), "data": books}

    return {"count": len(result), "data": result}
#1
@app.post('/addBooks')
def addBook(data:DataModel):
    titles=[]
    for i in books:
        titles.append(i['title'])
    if(data.title not in titles):
        books.append(data.dict())
        return'Book Added Successfully'
    else:
        return {'message':"Already Exists"}
#5
@app.put('/Update/{title}')
def Fullupdate(title:str,data:DataModel):
    for i in books:
       if( i['title']==title):
          i['author']=data.author
          i['price']=data.price
          i['stock']=data.stock
          return {'Message':"Updated Successfully!"}
    return {'Message':"Record Not Found"}
#6
@app.patch('/partialUpdate/{title}')
def PartialUpdate(title:str,data:DataModel):
    for i in books:
        if(i['title']==title):
            if(data.author is not None):
                i['author']=data.author
            if(data.price is not None):
                i['price']=data.price
            if(data.stock is not None):
                i['stock']=data.stock
            return {"message": "Updated Successfully!"}
    return {"message": "Record Not Found"}
#7
@app.delete('/delete/{title}')
def delete(title:str):
    for i in books:
        if(i['title']==title):
            books.remove(i)
            return 'Successfully deleted'
    return 'Not found babai'
#8
@app.get('/cheap')
def cheap(price:float):
    l=[]
    for i in books:
        if(i['price']<price):
            l.append(i)
    if(len(l)!=0):
        return l
    else:
        return'No cheap Books'