from pydantic import BaseModel

class CourseFile(BaseModel):
    file_name: str

class CourseTask(BaseModel):
    task_name: str

class CourseScore(BaseModel):
    score: int

class User(BaseModel):
    name: str
    api_token: str
    api_url: str
    status: str

class AuthorizationResponse(BaseModel):
    status:bool