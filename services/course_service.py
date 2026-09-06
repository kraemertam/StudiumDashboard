from data.course import new_course_db, get_course_db, add_modules_to_course_db, get_all_courses_db
from domains.course import Course
from services.module_service import get_module

# ---- COURSE -------------------------------------------------------------------------------------------------------------------------------
def get_course(course_id) -> Course | None:
    coursedata, moduledata = get_course_db(course_id)
    if coursedata is None:
        print("Der Kurs ist nicht in der Datenbank vorhanden.")
        return None
    
    course =Course(coursedata[0], coursedata[1], coursedata[2], coursedata[3])

    for m in moduledata:
        module_id = m[1]
        module = get_module(module_id)
        if module is not None:
            course.modules.append(module)
    print(f"{course.name} wurde mit {len(course.modules)} Modulen geladen.")
    print(course)
    return course
            
def create_new_course(course_id, course_name, course_title, course_etc) -> Course | None:
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

