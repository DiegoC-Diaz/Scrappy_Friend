from fastapi import APIRouter,Header,Depends,Query,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from app.services import canvas_service
from app.models.course import CourseFile,Assignment,FileRequest, CourseScore,AuthorizationResponse,User,Course

from typing import List


oauth2_scheme=OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter()

def get_user_data(token: str =Depends(oauth2_scheme)):
    user= canvas_service.get_user(api_key=token)
    if  not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid authentication credentials",)
    return User(api_token=token,user_id=user.id,name=user.name)

@router.get("/get/courses/files/silabo", response_model=List[CourseFile])
def get_course_files_silabo(user:User=Depends(get_user_data),course_id:Annotated[int,Query()]=None):
    return canvas_service.get_files_silabo(user.api_token,course_id=course_id)

@router.get("/get/courses/tasks", response_model=List[Assignment])
def get_course_tasks(user:User=Depends(get_user_data),course_id:Annotated[int,Query()]=None):
    return canvas_service.get_tasks(user.api_token,course_id=course_id)

@router.get("/get/courses/scores", response_model=List[CourseScore])
def get_course_scores(user:User=Depends(get_user_data),course_id:Annotated[int,Query()]=None):
    return canvas_service.get_scores(user.api_token,user_id=user.user_id,course_id=course_id)

@router.get("/get/courses",response_model=List[Course])
def get_courses(user:User=Depends(get_user_data)):
    return canvas_service.get_courses(user.api_token)

