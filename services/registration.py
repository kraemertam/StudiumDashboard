from data.student import check_student, get_overview_data, get_student, check_course
from data.course import get_all_courses

def login_student(student_id: str) -> bool:
    student_status = check_student(student_id)
    course_status = check_course(student_id)
    return student_status, course_status

def get_available_courses() -> list:
    all_available_courses = get_all_courses()
    return all_available_courses
