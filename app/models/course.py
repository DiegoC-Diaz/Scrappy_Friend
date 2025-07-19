from pydantic import BaseModel

class CourseFile(BaseModel):
    file_name: str
    file_url:str

class CourseTask(BaseModel):
    task_name: str

class CourseScore(BaseModel):
    score: int


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
    api_url: str
    status: str

class AuthorizationResponse(BaseModel):
    status:bool
    courses:list
