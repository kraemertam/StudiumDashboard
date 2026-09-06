import sqlite3
from data.student import new_student_db, get_student_db
from data.course import new_course_db, add_modules_to_course_db, get_all_courses_db
from domains.student import Student
from domains.course import Course
from domains.module import Module

# ---- STUDENT -----------------------------------------------------------------------------------------------------------------------------
def get_student(student_id: str) -> Student:
    """Load an already existing student and create as an Instanz of the object Student."""
    this_student = get_student_db(student_id)
    student = Student(id= this_student[0], name = this_student[1], lastname=this_student[2], course_id = this_student[3], gradetarget = this_student[4])
    print(f"Student {student.name}, {student.lastname}, {student.id} wurde geladen.")
    return student

def create_new_student(student_id, student_name, student_lastname) -> Student:
    """Create an new Student in database & as objekt."""
    try:
        new_student = Student(id=student_id, name=student_name, lastname=student_lastname)
    except ValueError as e:
        print(f"Student konnte nicht anlegt werden: {e}")
        return None
    try: 
        new_student_db(student_id, student_name, student_lastname)
    except ValueError as e:
        print(f"Student konnte nicht anlegt werden: {e}")
        return None
    print(f"{new_student.name} {new_student.lastname} wurde als neuer Student angelegt.")
    return new_student

# ---- COURSE -------------------------------------------------------------------------------------------------------------------------------
def get_course():
    pass

def create_new_course(course_id, course_name, course_title, course_etc) -> Course:
    try:
        new_course = Course(course_id, course_name, course_title, course_etc)
    except ValueError as e:
        print(f"Kurs konnte nicht anlegt werden: {e}")
        return None
    try:
        new_course_db(course_id, course_name, course_title, course_etc)
    except ValueError as e:
        print(f"Kurs konnte nicht anlegt werden: {e}")
        return None
    print(f"Der Kurs {course_name} wurde anlegt.")
    return new_course
    

# ---- MODULE --------------------------------------------------------------------------------------------------------------------------------

#def create_modulliste(student_id:str) ->list:
#    modulliste = get_overview_data(student_id)
#    print(f"Hier ist die Modulliste: \n {modulliste}")
#    module_liste = []
#    for m in modulliste:
#        id = m[0]
#        name = m[1]
#        etc = m[2]
#        status = m[3]
#        grade = m[4]
#        module = Module(id, name, etc, status, grade)
#        module_liste.append(module)
#
#    status_order = {"abgeschlossen": 0, "in Bearbeitung": 1, "nicht bestanden": 2, "offen": 3}
#    module_liste.sort(key=lambda m: status_order.get(m.status, 99))
#
#    return module_liste

# ---- TESTING -------------------------------------------------------------------------------

create_new_student("S123", "Tamara", "Krämer") #falsche Matrikelnummer
create_new_student("IU123", "Tamara", "Krämer")

#create_new_course("FS-BAAKI-01", "Angewandte Künstliche Intelligenz", "Bachelor of Science", 180) #correct
#create_new_course("FS-BAAKI-02", "Angewandte Programmierung", "Bachelor of Science", 180) #correct
#create_new_course("FkkkS-KI-2", "Angewandte Programmierung", "Bachelor of Science", 180) #false