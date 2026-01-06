"""This file can be used to initialise and import testdata for the database in order to test the application.
For this remove the "#" from the corresponding lines."""

from data.create_database import start_databank
from data.student import new_student_db, enroll_course
from data.module import new_modul_db
from data.course import new_course_db, add_modules_to_course



# --- DEFINITION OF THE FUNCTIONS FOR IMPORTING TESTDATA -------------------------------------------------------------------------------------------------

def insert_moduledata_db():
    """ Initiale Daten für Module werden eingelesen."""
    with open ("module.csv", "r", encoding="utf-8") as moduleliste:
        for line in moduleliste:
            module = line.strip().strip('"').split(", ")
            module_id = module[0]
            module_name = module[1]
            module_etc = module[2]
            print(module_id, module_name, module_etc)

            new_modul_db(module_id, module_name, module_etc)

def insert_coursedata_db():
    """Initiale Daten für Course werden eingelesen."""
    with open ("course.csv", "r", encoding="utf-8") as courselist:
        for line in courselist:
            course = line.strip().strip('"').split(", ")
            course_id = course[0]
            course_name = course[1]
            course_title = course[2]
            course_etc = course[3]
            print(course_id, course_name, course_title, course_etc)

            new_course_db(course_id, course_name, course_title, course_etc)

def initialize_course():
    """Initial wird ein Kurs mit Modulen verbunden"""
    with open ("module.csv", "r", encoding="utf-8") as moduleliste:
        for line in moduleliste:
            module = line.strip().strip('"').split(", ")
            module_id = module[0]

            add_modules_to_course("FS-BAAKI-01", module_id)

# --- START INITIALISING AND IMPORTING TESTDATA -----------------------------------------------------------------------

# --- SET UP DATABASE AND READ IN TEST DATA----------------------------------------------------------------------------
#start_databank()
#insert_moduledata_db()
#insert_coursedata_db()
#initialize_course()

# --- CREATE STUDENTS -------------------------------------------------------------------------------------------------
#new_student_db("S11", "Tim", "Tuer")
#new_student_db("S123", "Tamara", "Krämer")
#new_student_db("S3", "Lisa", "Lotte")

# --- ENROLL STUDENTS IN COURSE ---------------------------------------------------------------------------------------
#enroll_course("S123", "FS-BAAKI-01", 8)
#enroll_course("S11","FS-BAAKI-01", 6 )


# --- PRINT DATABASE --------------------------------------------------------------------------------------------------
#print_databank()


