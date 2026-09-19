"""This file can be used to initialise the database and import inital data for the database in order to test the application. 
This is useful for using or testing the application without having to enter all the data manually, but not needed.
For this remove the "#" from the corresponding lines."""

from pathlib import Path
from services.module_service import create_new_module
from services.course_service import create_new_course, add_module_to_course
from services.student_service import create_new_student
from services.enrollment_service import enrollment_student_in_course

# --- DEFINITION OF THE FUNCTIONS FOR IMPORTING TESTDATA -------------------------------------------------------------------------------------------------

def insert_moduledata_db():
    """Initial test data for the modules is being loaded."""
    base_path = Path(__file__).parent
    file_path = base_path / "initial_data_csv" / "module.csv"
    with open (file_path, "r", encoding="utf-8") as moduleliste:
        for line in moduleliste:
            line = line.strip().strip('"')
            if not line:
                continue
        
            module_info, _, course_info = line.partition(";")
            print(f"module_info: {module_info}")
            module_info = [m.strip() for m in module_info.split(", ")]
            module_id = module_info[0]
            module_name = module_info[1]
            module_ects = module_info[2]

            create_new_module(module_id, module_name, module_ects)


def insert_coursedata_db():
    """Initial test data for the courses is being loaded."""
    base_path = Path(__file__).parent
    file_path = base_path / "initial_data_csv" / "course.csv"
    with open (file_path, "r", encoding="utf-8") as courselist:
        for line in courselist:
            course = line.strip().strip('"').split(", ")
            course_id = course[0]
            course_name = course[1]
            course_title = course[2]
            course_ects = int(course[3])
            create_new_course(course_id, course_name, course_title, course_ects)

def initialize_course():
    """Initial test data for the course-module relationships is being loaded."""
    base_path = Path(__file__).parent
    file_path = base_path / "initial_data_csv" / "module.csv"
    with open (file_path, "r", encoding="utf-8") as moduleliste:
        for line in moduleliste:
            line = line.strip().strip('"')
            if not line:
                continue

            module_info, _, course_info = line.partition(";")
            print(f"module_info: {module_info}")
            module_info = [m.strip() for m in module_info.split(", ")]

            module_id = module_info[0]
            course_info = [c.strip() for c in course_info.split(",") if c.strip()]

            for course in course_info:
                add_module_to_course(course_id=course, module_id=module_id)
            


# --- START INITIALISING AND IMPORTING TESTDATA -----------------------------------------------------------------------

# --- SET UP DATABASE AND READ IN TEST DATA----------------------------------------------------------------------------
insert_moduledata_db() # => (check: true)
insert_coursedata_db() # => (check: true)
initialize_course() # => (check: true)

# --- CREATE STUDENTS -------------------------------------------------------------------------------------------------
create_new_student("IU1111", "Tim", "Tuer") # => (check:true)
create_new_student("IU123", "Tamara", "Krämer") # => (check:true)
create_new_student("IU3333", "Lisa", "Lotte") # => (check:true)

# --- ENROLL STUDENTS IN COURSE ---------------------------------------------------------------------------------------
enrollment_student_in_course("IU1111", "FS-BAAKI-01", 2.5)
enrollment_student_in_course("IU123","FS-BAAKI-01", 3.1 )
enrollment_student_in_course("IU3333", "FS-BAAKI-01", 1.5)



