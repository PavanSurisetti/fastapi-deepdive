from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

#  Store data globally
shares_details = [
    {'folio_id': 1, 'Name': 'Ganesha', 'Shares': 10, 'Value': 100},
    {'folio_id': 2, 'Name': 'Satya', 'Shares': 15, 'Value': 150}
]

#  Pydantic model for PATCH
class ShareUpdate(BaseModel):
    Name: Optional[str] = None
    Shares: Optional[int] = None
    Value: Optional[int] = None


@app.get("/")
def home():
    return {"message": "Welcome to Stock Market"}


@app.get('/user/{folio_id}')
def get_user(folio_id: int):
    for user in shares_details:
        if user['folio_id'] == folio_id:
            return user
    return {"error": "User not found"}


@app.patch('/user/{folio_id}')
def update_user(folio_id: int, data: ShareUpdate):
    for user in shares_details:
        if user['folio_id'] == folio_id:
            if data.Name is not None:
                user['Name'] = data.Name
            if data.Shares is not None:
                user['Shares'] = data.Shares
            if data.Value is not None:
                user['Value'] = data.Value
            return {"message": "Updated successfully", "data": user}

    return {"error": "User not found"}