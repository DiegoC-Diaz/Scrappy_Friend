from pydantic import BaseModel
from typing import Optional, List

class CourseFile(BaseModel):
    file_name: str
    file_url:str

class CourseTask(BaseModel):
    task_name: str

class CourseScore(BaseModel):
    score: Optional[float]

class Assignment(BaseModel):
    id: int
    name: str
    due_at: Optional[str]
    points_possible: Optional[float]
    submission_types: list

class Course(BaseModel):
    course_id: int 
    course_name: str

class FileRequest(BaseModel):    
    file_name: str
    course_id: int
    api_url:str
    api_token:str


class User(BaseModel):
    name: str
    api_token: str
    user_id: int = None


class AuthorizationResponse(BaseModel):
    status:bool
    courses:list
