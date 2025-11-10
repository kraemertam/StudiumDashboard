from data.query_db import check_student, get_overview_data, get_student, check_course
from services.create_objects import create_student, create_modulliste

# ---Login zum Dashboard: login student -> False: student_registration | True: get_to_overview ---


def student_registrastion(student_id):
    pass


def login_student(student_id: str) -> bool:
    student_status = check_student(student_id)
    course_status = check_course(student_id)
    return student_status, course_status


