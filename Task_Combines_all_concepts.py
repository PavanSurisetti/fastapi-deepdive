'''
🎯 FINAL TASK: Student Management API (CRUD)
🧠 Goal

👉 Use ALL concepts together:

Path parameters ✅
Query parameters ✅
POST, GET, PUT, DELETE ✅
Request body (Pydantic) ✅
🏗️ Requirements
1️⃣ POST → Create Student
POST /students

👉 Body:

{
  "name": "string",
  "age": int,
  "branch": "string",
  "email": "optional"
}

👉 Store in list

2️⃣ GET → Get All Students
GET /students

👉 Return all students

3️⃣ GET → Get One Student
GET /students/{name}

👉 Use path parameter
👉 Return that student
👉 If not found → error message

4️⃣ GET with Query Parameter 🔥
GET /search?branch=CSE

👉 Use query parameter
👉 Return all students in that branch

5️⃣ PUT → Update Student
PUT /students/{name}

👉 Update student details
👉 If not found → error

6️⃣ DELETE → Remove Student
DELETE /students/{name}

👉 Remove student
👉 Return confirmation
'''
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = []

class Student(BaseModel):
    name: str
    age: int
    branch: str
    email: Optional[str] = None

@app.get('/')
def home():
    return {'message': 'Welcome Student Management!'}

@app.post('/students')
def create_student(student: Student):
    for s in students:
        if student.name == s['name']:
            return {'message': 'Name already exists'}
    
    students.append(student.dict())
    #student.dict() = convert FastAPI/Pydantic object into normal Python
    return {'message': 'Created successfully', 'data': student}

@app.get('/students')
def get_all_students():
    return {'data': students}

@app.get('/students/{name}')
def get_student(name: str):
    for s in students:
        if name == s['name']:
            return s
    return {'message': 'Student not found'}

@app.get('/search')
def search(branch: str):
    result = []
    for s in students:
        if branch == s['branch']:
            result.append(s)
    
    if not result:
        return {'message': 'No students found'}
    
    return {'data': result}

@app.put('/students/{name}')
def update(name: str, stu: Student):
    for s in students:
        if name == s['name']:
            s['name'] = stu.name
            s['age'] = stu.age
            s['branch'] = stu.branch
            s['email'] = stu.email
            return {'message': 'Updated successfully', 'data': s}
    
    return {'message': 'Student not found'}

@app.delete('/students/{name}')
def delete(name: str):
    for s in students:
        if s['name'] == name:
            students.remove(s)
            return {'message': 'Deleted successfully'}
    
    return {'message': 'Student not found'}
#hey we use stu:Student or student:Student when we are dealing with the POST AND PUT