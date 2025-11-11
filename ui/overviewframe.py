import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.font as font
from pathlib import Path

from services.create_objects import create_modulliste, create_student
from services.registration import login_student
from domain.models import Module

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# --- Dashboard Frame -------------------------------------------------------------------------------------------------

def overview_frame(student_id, dashboardframe):
    modulliste = create_modulliste(student_id)
    print("Hi:", modulliste)
    student = create_student(student_id)
    print("Hi:", student)
    print(student.name)

    overview = tk.Toplevel(dashboardframe)
    overview.geometry("1000x900")
    overview.columnconfigure(0, weight=1)
    overview.rowconfigure(0, weight=1)

    header = ttk.Label(overview, text=f"Dashboard für dein Studium {student.name}", anchor="center")
    header.config(font=("Arial", 20))
    header.grid(sticky="ew", padx=5, pady=5)

    image_path = Path(__file__).resolve().parent / "Schreibtisch.jpg"
    image = Image.open(image_path).resize((250, 200))
    photo = ImageTk.PhotoImage(image)
    label = ttk.Label(overview, text="Schön, dass du da bist!", image=photo, padding=5, compound="top", anchor="center")
    label.image = photo
    label.grid(row=3, pady=5, padx=5, sticky="ew")

    ttk.Separator(overview, orient="horizontal").grid(sticky="ew")

    moduloverview = ttk.Frame(overview)
    moduloverview.config(width=900, height=700)
    moduloverview.grid_propagate(False)
    header = ttk.Label(moduloverview, text="Modulübersicht", anchor="center")
    header.config(font=("Arial", 20))
    header.grid(row=0, columnspan=2, sticky="ew", padx=5, pady=5)

    moduloverview.columnconfigure(0, weight=1, uniform="cols", pad=5)
    moduloverview.columnconfigure(1, weight=1, uniform="cols", pad=5)
    for x in range(int(student.semester/2+2)):
        moduloverview.rowconfigure(x, weight=1, uniform="rows", pad=5)

    moduloverview.grid(sticky="nsew", padx=10, pady=10)

    # --- SEMESTERFRAME -----------------------------------------------------------------------------------------------
    semesters = []
    for x, semester in enumerate(range((student.semester))):
        reihe = x // 2 + 1
        spalte = x % 2
        semester = tk.Frame(moduloverview, bg="lightgrey")
        semester.grid(row=reihe, column=spalte, sticky="nsew", padx=10, pady=10)
        semesters.append(semester)

    # --- MODULFRAME ---------------------------------------------------------------------------------------------------

    modules_per_semester = int(len(modulliste)/student.semester)
    print("Module pro Semester: ", modules_per_semester)

    module_divide = [modulliste[i:i+modules_per_semester] for i in range(0, len(modulliste), modules_per_semester)]
    print("Zuordnung der Module: ", module_divide)

    semester_divide = dict(zip(semesters, module_divide))
    print(semester_divide)

    for s in semester_divide:
        m = semester_divide[s]
        i=0
        for module in m:
            s.columnconfigure(i, weight=1)
            modulframe = tk.Frame(s, bg="lightblue", borderwidth=1, relief="solid")
            modulframe.columnconfigure(index=1, weight=1, uniform="cols", pad=5)
            modulname_label = tk.Label(modulframe, text=f"{module.name}", bg="lightblue", font=("arial", 6, "bold"))
            modulstatus_label = tk.Label(modulframe, text=f"{module.status}", bg="lightblue", font=("arial", 5, "bold"))
            modulstatus_button = tk.Button(modulframe, text="Status ändern", bg="lightblue", font=("arial", 5, "bold"))
            modulname_label.grid(sticky="ew", padx=5, pady=5)
            modulstatus_label.grid(sticky="ew", padx=5, pady=5)
            modulstatus_button.grid(sticky="ew", padx=5, pady=5)
            modulframe.grid(row= 1, column=i, sticky="ew", padx=5, pady=5)
            i += 1
            print(i, ":", module)


# --- CHANGE STATUS VERSUCH -------------------------------------------------------------------------------------------
    #module1 = modulliste[0]
    #print(module1)
    #print(type(module1))
    #module1.change_status(student_id)





