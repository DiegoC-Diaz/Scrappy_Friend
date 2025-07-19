from canvasapi import Canvas
from app.services.tools.file_finder import extrac_file_id

cached_api_url = None

def get_files_silabo(api_key,api_url,course_id):
    silabus_files=[]
    canvas=Canvas(api_url,api_key)

    if canvas:
        course=canvas.get_course(course_id)
        page=course.get_page("silabo")
        full_page = course.get_page(page.url)
        files_ids=extrac_file_id(full_page.body)
        for id in files_ids:
            file=course.get_file(id)
            silabus_files.append({"file_name":file.filename,"file_url":file.url})
            
        
        return silabus_files
    
    return [{"file_name": "file1.pdf","file_url": "empty"}]

def get_tasks():
    # Logic to get tasks from Canvßas
    return [{"task_name": "task1"}]

def get_scores():
    # Logic to get scores from Canvas
    return [{"score": 95}]

def get_courses(api_key,api_url):
    global cached_api_url
    if cached_api_url is None:
        cached_api_url = api_url
    elif cached_api_url != api_url:
        print("Warning: API URL changed. Using cached URL.")

    userCourses=[]
    user=get_user(api_key=api_key,api_url=cached_api_url)
    courses = user.get_courses(enrollment_state='active')
    for course in courses:
        userCourses.append({"course_id":course.id,"course_name":course.name})
    return userCourses





def get_user(api_url, api_key):
    canvas = Canvas(api_url, api_key)
    try:
        user = canvas.get_current_user()
        return user
    except Exception as e:
        print(f"Authentication Failed: {str(e)}")
        return False


def get_authorization(api_key,api_url):
    global cached_api_url
    if cached_api_url is None:
        cached_api_url = api_url
    elif cached_api_url != api_url:
        print("Warning: API URL changed. Using cached URL.")

    try:
        courses=get_courses(api_key,cached_api_url)
    except Exception as e:
        print(f"Authentication Failed: {str(e)}")
        return {"courses":[],"status":False}
    return {"courses":courses,"status":True}