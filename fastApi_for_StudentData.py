# Create a FastAPI project with the following specifications:
# A Student resource. Each student will have:
# Id (int)
# Name(str)
# Age (int)
# Sex (str)
# Height (float)
# For data storage, use an in-memory storage (Python dictionary)
# Create endpoints to do the following:
# Create a Student resource
# Retrieve a Student resource (one Student and many Students)
# Update a Student resource
# Delete a Student resource

from fastapi import FastAPI

app = FastAPI()
students = {}

class Student:
    def __init__(self, id: int, name:str, age:int, sex:str, height: float):
        self.id = id
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height


@app.post("/students/")
def create_student(id: int, name: str, age: int, sex: str, height: float):
    student = Student(id=id, name=name, age=age, sex=sex, height=height)
    students[id] = student
    return student

@app.get("/students/")
def read_students(): #returns all student data.
    
    return students

@app.get("/students/{id}")
def read_a_student(id: int): #return a student data
    if id not in students:
        return "Student not Found"
    return students[id]

@app.put("/students/{id}")
def update_a_student_resource(id: int, name:str,age:str, sex: str, height: float): #update student resource
    if id not in students:
        return "{Student does not exist for any update}"
    else:
        students[id].name = name
        students[id].age = age
        students[id].sex = sex
        students[id].height = height

    return {students[id], "Student resource sucessfully updated"}


@app.delete('/students/{id}') #I have not yet place the id on the endpoint, now testing something
def delete_a_student(id:int):
   if id not in students:
      return "Student does not exit for deletion"
   else:
       del students[id]
 
   return {"Student deleted sucessfully"}
       
         
