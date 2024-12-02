from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query, Response
from pydantic import BaseModel , Field, model_validator
from bson import ObjectId
from starlette.responses import JSONResponse
from bson import ObjectId
from fastapi import HTTPException, Response, status
from fastapi.responses import JSONResponse


# Database collection placeholder
from app.db import collection




# Schemas 
class AddressBase(BaseModel):
    city: str
    country: str

class StudentCreate(BaseModel):
    name: str
    age: int
    address: AddressBase

class StudentResponse(BaseModel):
    id: str
    name: str
    age: int
    address: AddressBase

class StudentBase(BaseModel):
    name: str
    age: int

class StudentListResponse(BaseModel):
    data: List[StudentBase]

class Address(BaseModel):
    city: str = Field(..., min_length=1, description="City name must not be empty")
    country: str = Field(..., min_length=1, description="Country name must not be empty")

class StudentCreate(BaseModel):
    name: str = Field(..., min_length=1, description="Name must not be empty")
    age: int = Field(..., gt=0, description="Age must be greater than zero")
    address: Address

    @model_validator(mode="after")
    def check_non_empty(cls, model):
        if not all(value for value in model.__dict__.values()):
            raise ValueError("All fields must be non-empty")
        return model

# Router

router = APIRouter()


#Create a student
@router.post(
    "/students",
    response_model=dict,
    status_code=201
)
async def add_student(student: StudentCreate):
    student_dict = student.dict()
    student_id = str(collection.insert_one(student_dict).inserted_id)
    return {"id": student_id}


#List students
@router.get(
    "/students",
    response_model=StudentListResponse
)
async def list_students(
    country: Optional[str] = Query(None, description="Filter by country"),
    age: Optional[int] = Query(None, description="Filter by age (greater or equal)"),
):
    
    query = {}

    if country:
        query["address.country"] = country
    if age:
        query["age"] = {"$gte": age}

    students = collection.find(query, {"_id": 0, "name": 1, "age": 1})

    return {"data": list(students)}


#Fetch a student
@router.get(
    "/students/{id}",
    response_model=StudentResponse
)
async def get_student(id: str):

    student = collection.find_one({"_id": ObjectId(id)})

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    
    student["id"] = str(student["_id"])


    return student



# Utility function to check if the ObjectId is valid
def is_valid_objectid(oid: str) -> bool:
    """Utility function to check if the ObjectId is valid"""
    try:
        # If this raises an exception, it's an invalid ObjectId
        ObjectId(oid)  
        return True
    except Exception:
        return False
    

#Update a student
@router.patch(
    "/students/{id}",
    response_model=None,
    status_code=204
)
async def update_student(id: str, student: StudentCreate):

    if not is_valid_objectid(id):
        raise HTTPException(status_code=400, detail="Invalid ObjectId format")

    #update operation if the ID is valid
    update_result = collection.update_one(
        {"_id": ObjectId(id)}, {"$set": student.dict()}
    )
    if update_result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    
    return Response(status_code=204)


#Delete a student
@router.delete(
    "/students/{id}",
    response_model=None
)
async def delete_student(id: str):


    if not is_valid_objectid(id):
        raise HTTPException(status_code=400, detail="Invalid ObjectId format")


    delete_result = collection.delete_one({"_id": ObjectId(id)})
    

    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")


    return JSONResponse(status_code=status.HTTP_200_OK, content={})

