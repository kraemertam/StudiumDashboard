from data.student import new_student_db, get_student_db
from domains.student import Student


# ---- STUDENT -----------------------------------------------------------------------------------------------------------------------------
def get_student(student_id: str) -> Student | None:
    """Load an already existing student and create as an Instanz of the object Student."""
    this_student = get_student_db(student_id)
    if not this_student:
        return None
    student = Student(id= this_student[0], name = this_student[1], lastname=this_student[2], course_id = this_student[3], gradetarget = this_student[4])
    print(f"Student {student.name}, {student.lastname}, {student.id} wurde geladen.")
    return student

def create_new_student(student_id, student_name, student_lastname) -> Student | None:
    """Create an new Student in database & as objekt."""
    try:
        new_student = Student(id=student_id, name=student_name, lastname=student_lastname)
    except ValueError as e:
        print(f"Student konnte nicht anlegt werden: {e}")
        raise
    try: 
        new_student_db(student_id, student_name, student_lastname)
    except ValueError as e:
        print(f"Student konnte nicht anlegt werden: {e}")
        raise
    print(f"{new_student.name} {new_student.lastname} wurde als neuer Student angelegt.")
    return new_student
