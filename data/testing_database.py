from create_database import start_databank
from add_to_database import new_modul_db, new_course_db, new_student_db, add_modules_to_course
from data.create_database import insert_moduledata_db, insert_coursedata_db, initialize_course
from enroll_course_db import enroll_course
from print_database import print_databank

# --------------- TRYING TESTDATA ------------------------------------------------------------------------------------

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


# -- PRINT DATABASE ---
print_databank()


