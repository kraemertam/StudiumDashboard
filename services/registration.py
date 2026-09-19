from data.student import check_student_db, get_student_db, check_course_db
from data.moduleprogress import get_grade_data_db
from data.course import get_all_courses_db

def login_student(student_id: str) -> tuple[bool, bool]:
    student_status = check_student_db(student_id)
    course_status = check_course_db(student_id)
    return student_status, course_status

def get_available_courses() -> list:
    all_available_courses = get_all_courses_db()
    return all_available_courses