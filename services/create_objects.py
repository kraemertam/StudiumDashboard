from data.query_db import get_student, get_overview_data
from domain.models import Student, Module

def create_modulliste(student_id):
    modulliste = get_overview_data(student_id)
    print(f"Hier ist die Modulliste: \n {modulliste}")
    module_liste = []
    for modul in modulliste:
        id = modul[1]
        name = modul[2]
        etc = 5
        status = modul[3]
        grade = modul[4]
        module = Module(id, name, etc, status, grade)
        module_liste.append(module)
    return module_liste

def create_student(student_id):
    new_student = get_student(student_id)
    print(new_student)
    student = Student(id= new_student[0], name = new_student[1], lastname=new_student[2], course = new_student[3], etc = new_student[4], semester = new_student[5])
    print(student)
    return student

create_student("S123")