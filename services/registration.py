from data.query_db import check_student, get_overview_data, get_student
from services.create_objects import create_student, create_modulliste

# ---Login zum Dashboard: login student -> False: student_registration | True: get_to_overview ---


def student_registrastion(student_id):
    pass


def login_student(student_id: str) -> bool:
    login_query = check_student(student_id)
    print(f"Dein Loginstatus: {login_query}")
    return login_query
