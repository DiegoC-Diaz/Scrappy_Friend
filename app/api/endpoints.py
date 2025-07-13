from fastapi import APIRouter
from app.services import canvas_service
from app.models.course import CourseFile, CourseTask, CourseScore,AuthorizationResponse,User
from typing import List


router = APIRouter()

@router.get("/courses/files", response_model=List[CourseFile])
def get_course_files():
    return canvas_service.get_files()

@router.get("/courses/tasks", response_model=List[CourseTask])
def get_course_tasks():
    return canvas_service.get_tasks()

@router.get("/courses/scores", response_model=List[CourseScore])
def get_course_scores():
    return canvas_service.get_scores()

@router.post("/authorize",response_model=AuthorizationResponse)
def post_verify_user(user:User):
    token=user.api_token

    api_url=user.api_url

    return canvas_service.get_authorization(api_key=token,api_url=api_url)
