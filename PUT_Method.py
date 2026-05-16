from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Pydantic model
class Student(BaseModel):
    name: str
    age: int
    branch: str
    email: Optional[str] = None

# In-memory storage
students_list = [
    {"id": 1, "name": "Alice", "age": 20, "branch": "CSE", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "age": 21, "branch": "ECE"}
]

# GET all students
@app.get("/students")
def get_all_students():
    return {"students": students_list}

# GET single student by ID
@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students_list:
        if student["id"] == student_id:
            return {"student": student}
    return{'Not Found'}

# PUT endpoint to update a student by ID
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for student in students_list:
        if student["id"] == student_id:
            student["name"] = updated_student.name
            student["age"] = updated_student.age
            student["branch"] = updated_student.branch
            student["email"] = updated_student.email
            return {"message": "Student updated successfully", "student": student}
    return{'Not Found'}