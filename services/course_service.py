from data.course import new_course_db, get_course_db, add_modules_to_course_db, get_all_courses_db
from domains.course import Course
from services.module_service import get_module

# ---- COURSE -------------------------------------------------------------------------------------------------------------------------------
def get_course(course_id) -> Course | None:
    coursedata = get_course_db(course_id)
    if coursedata is None:
        print("Der Kurs ist nicht in der Datenbank vorhanden.")
        return None
    course =Course(coursedata[0], coursedata[1], coursedata[2], coursedata[3])
    return course
            
def create_new_course(course_id, course_name, course_title, course_ects) -> Course | None:
    try:
        new_course = Course(course_id, course_name, course_title, course_ects)
    except ValueError as e:
        print(f"Kurs konnte nicht anlegt werden: {e}")
        raise
    try:
        new_course_db(course_id, course_name, course_title, course_ects)
    except ValueError as e:
        print(f"Kurs konnte nicht anlegt werden: {e}")
        raise
    print(f"Der Kurs {course_name} wurde anlegt.")
    return new_course


def add_module_to_course(course_id, module_id):
    course = get_course(course_id) # Check, if Course in DB. If yes, return Course as Instance.
    if course is None:
        print(f"Der Kurs {course_id} ist nicht in der Datenbank enthalten.")
        return False
    
    module = get_module(module_id) # Check, if Module in DB. If yes create Instanz.
    if module is None:
        print(f"Das Module {module_id} ist nicht in der Datenbank enthalten.")
        return False
    
    try:
        course.add_module(module) # Check, if Module can add to Course. If yes, add Module to Moduleliste in Instance Course.
        add_modules_to_course_db(course.id, module.id) # Add Module to Course in DB.
    except ValueError as e:
        print(f"{e}")
        return False

    return True

