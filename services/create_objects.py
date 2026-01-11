from data.student import new_student_db, get_student, get_overview_data
from domains.student import Student
from domains.module import Module


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

    status_order = {"abgeschlossen": 0, "in Bearbeitung": 1, "nicht bestanden": 2, "offen": 3}
    module_liste.sort(key=lambda m: status_order.get(m.status, 99))

    return module_liste

def create_student(student_id: str) -> Student:
    new_student = get_student(student_id)
    print(new_student)
    student = Student(id= new_student[0], name = new_student[1], lastname=new_student[2], course_id = new_student[3], course_name=new_student[4], etcs = new_student[5], semester = new_student[6], gradetarget = new_student[7])
    return student

def create_new_student(student_id, student_name, student_lastname):
    new_student = new_student_db(student_id, student_name, student_lastname)
    student = Student(id=student_id, name=student_name, lastname=student_lastname)
    return student