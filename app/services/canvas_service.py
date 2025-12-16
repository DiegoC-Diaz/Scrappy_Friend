from canvasapi import Canvas
from app.services.tools.file_finder import extrac_file_id
from app.models.course import Assignment
url="https://unitechonduras.instructure.com"
def get_files_silabo(api_key,course_id):
    silabus_files=[]
    canvas=Canvas(url,api_key)

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

def get_tasks(api_key,course_id=None):
    canvas=Canvas(url, api_key)
    course=canvas.get_course(course_id)
    assignments= course.get_assignments()
    assigmentsResponse=[]
    for assignment in assignments:
        assigmentsResponse.append(Assignment(
            id=assignment.id,
            name=assignment.name,
            due_at=assignment.due_at,
            points_possible=assignment.points_possible,
            submission_types=assignment.submission_types))
    
    
    
    
    
    
    return assigmentsResponse

def get_scores(api_key,user_id,course_id):
    # Logic to get scores from Canvas
    canvas=Canvas(url, api_key)
    course=canvas.get_course(course_id)
    
    enrollments=course.get_enrollments(type=['StudentEnrollment'])
    for enrollment in enrollments:
        if enrollment.user['id'] == canvas.get_current_user().id:
            return [{"score": enrollment.grades['current_score']}]
    
    
    
    
    return [{"score": 95}]

def get_courses(api_key):
    userCourses=[]
    user=get_user(api_key=api_key)
    courses = user.get_courses(enrollment_state='active')
    for course in courses:
        userCourses.append({"course_id":course.id,"course_name":course.name})
    return userCourses





def get_user( api_key):
    canvas = Canvas(url, api_key)
    try:
        user = canvas.get_current_user()
        return user
    except Exception as e:
        print(f"Authentication Failed: {str(e)}")
        return None


