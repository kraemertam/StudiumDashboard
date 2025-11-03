
import delete_from_database
from create_database import start_databank
from add_to_database import new_modul_db, new_course_db, new_student_db, add_modules_to_course
from print_database import print_databank


#start_databank()
#new_modul_db("m572", "Kommunikation", "5", "offen")
#new_student_db("s1280","Lisa", "Maier")
#new_course_db("c122", "Data Eng", "180")
add_modules_to_course("c123", "m571")
add_modules_to_course("c123", "m572")


print_databank()


