from data.add_to_database import new_student_db
from data.query_db import get_student, get_overview_data
from domains.models import Student, Module

def create_modulliste(student_id:str) ->list:
    modulliste = get_overview_data(student_id)
    print(f"Hier ist die Modulliste: \n {modulliste}")
    module_liste = []
    for m in modulliste:
        id = m[0]
        name = m[1]
        etc = m[2]
        status = m[3]
        grade = m[4]
        module = Module(id, name, etc, status, grade)
        module_liste.append(module)
    return module_liste

def create_student(student_id: str) -> Student:
    new_student = get_student(student_id)
    print(new_student)
    student = Student(id= new_student[0], name = new_student[1], lastname=new_student[2], course_id = new_student[3], course_name=new_student[4], etcs = new_student[5], semester = new_student[6])
    return student

def create_new_student(student_id, student_name, student_lastname):
    new_student = new_student_db(student_id, student_name, student_lastname)
    student = Student(id=student_id, name=student_name, lastname=student_lastname)
    return student