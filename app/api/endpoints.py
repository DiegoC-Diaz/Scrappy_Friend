from fastapi import APIRouter,Header
from app.services import canvas_service
from app.models.course import CourseFile, CourseTask,FileRequest, CourseScore,AuthorizationResponse,User,Course
from typing import List


router = APIRouter()

@router.post("/courses/files/silabo", response_model=List[CourseFile])
def get_course_files_silabo(file_request:FileRequest):
    token=file_request.api_token
    api_url=file_request.api_url
    course_id=file_request.course_id
    return canvas_service.get_files_silabo(api_key=token,api_url=api_url,course_id=course_id)

@router.get("/courses/tasks", response_model=List[CourseTask])
def get_course_tasks():
    return canvas_service.get_tasks()

@router.get("/courses/scores", response_model=List[CourseScore])
def get_course_scores():
    return canvas_service.get_scores()

@router.post("/get/courses",response_model=List[Course])
def get_courses(user:User):
    return canvas_service.get_courses(api_key=user.api_token,api_url=user.api_url)


@router.post("/authorize",response_model=AuthorizationResponse)
def post_verify_user(user:User):
    token=user.api_token
    api_url=user.api_url
    return canvas_service.get_authorization(api_key=token,api_url=api_url)
