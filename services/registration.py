from data.student import check_student, get_overview_data, get_student, check_course

def login_student(student_id: str) -> bool:
    student_status = check_student(student_id)
    course_status = check_course(student_id)
    return student_status, course_status


