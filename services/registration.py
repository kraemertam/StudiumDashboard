from IPython.core.completerlib import module_list

from data.query_db import check_student, get_overview_data
from domain.models import Module


def get_to_overview(student_id):
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



def student_registrastion(student_id):
    pass


def login_student(student_id):
    login_query = check_student(student_id)
    print(f"Du bist bereits registriert: {login_query}")

    if login_query == True:
        a = get_to_overview(student_id)
        print(a)
        return a

    if login_query == False:
        student_registrastion(student_id)

login_student("f")
