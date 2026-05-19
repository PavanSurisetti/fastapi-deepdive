from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

#  Main Model (for POST & PUT)
class Book(BaseModel):
    title: str
    author: str
    price: float

#  Update Model (for PATCH)
class UpdateBook(BaseModel):
    author: Optional[str] = None
    price: Optional[float] = None

#  Temporary storage
books = []

#  Home
@app.get("/")
def home():
    return {"message": "Book API Running"}

# 1 POST → Create Book (201)
@app.post("/books", status_code=201)
def create_book(book: Book):
    for b in books:
        if b["title"] == book.title:
            raise HTTPException(status_code=400, detail="Book already exists")

    books.append(book.dict())
    return {"message": "Book created", "data": book}

# 2 GET → All Books (200)
@app.get("/books")
def get_books():
    return {"count": len(books), "data": books}

# 3 GET → One Book (404 if not found)
@app.get("/books/{title}")
def get_book(title: str):
    for b in books:
        if b["title"] == title:
            return b
    raise HTTPException(status_code=404, detail="Book not found")

# 4 PUT → Full Update
@app.put("/books/{title}")
def update_book(title: str, book: Book):
    for i in books:
        if i["title"] == title:
            i["title"] = book.title
            i["author"] = book.author
            i["price"] = book.price
            return {"message": "Updated successfully", "data": i}

    raise HTTPException(status_code=404, detail="Book not found")

# 5 PATCH → Partial Update
@app.patch("/books/{title}")
def partial_update(title: str, book: UpdateBook):
    for i in books:
        if i["title"] == title:
            if book.author is not None:
                i["author"] = book.author
            if book.price is not None:
                i["price"] = book.price
            return {"message": "Partially updated", "data": i}

    raise HTTPException(status_code=404, detail="Book not found")

# 6 DELETE → Remove Book (204)
@app.delete("/books/{title}", status_code=204)
def delete_book(title: str):
    for i in books:
        if i["title"] == title:
            books.remove(i)
            return

    raise HTTPException(status_code=404, detail="Book not found")