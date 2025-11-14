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

    # --- MODULFRAME ALL ---------------------------------------------------------------------------------------------------
    class Moduleview():
        def __init__(self, module, student_id, container, i, *args, **kwargs):
            self.module = module
            self.moduleid = module.id
            self.modulename = module.name
            self.moduleetc = module.etc
            self.modulestatus = module.status
            self.modulegrade = module.grade
            self.container = container
            self.student_id = student_id

            # --- Backgroundcolor configuration -------------------------------------------------------------------
            if module.status == "offen":
                bgc = "lightblue"
            if module.status == "in Bearbeitung":
                bgc = "orange"
            if module.status == "abgeschlossen":
                bgc = "lightgreen"

            # --- Modulframe --------------------------------------------------------------------------------------

            self.frame = tk.Frame(self.container, bg=bgc, borderwidth=1, relief="solid")
            self.frame.columnconfigure(index=i, weight=1, uniform="cols", pad=5)
            self.modulename_label = tk.Label(self.frame, text=f"{self.modulename}", bg=bgc, font=("arial", 6, "bold"),
                                             anchor="center")
            self.modulestatus_label = tk.Label(self.frame, text=f"{self.modulestatus}", bg=bgc,
                                               font=("arial", 5, "bold"))
            self.modulestatus_button = tk.Button(self.frame, text="Status ändern", bg=bgc, font=("arial", 5, "bold"),
                                                 command=self.change_modulestatus)
            self.modulename_label.grid(sticky="ew", padx=5, pady=5)
            self.modulestatus_label.grid(sticky="ew", padx=5, pady=5)
            self.modulestatus_button.grid(sticky="ew", padx=5, pady=5)
            self.frame.grid(row=1, column=i, sticky="ew", padx=5, pady=5)

        def set_modulegrade_entry(self):
            modulegrade = tk.StringVar()

            def set_modulegrade():
                grade = self.module.set_grade(self.student_id, modulegrade.get())
                modulegradeframe.destroy()
                return grade

            modulegradeframe = tk.Toplevel(moduloverview)
            modulegrade_label = tk.Label(modulegradeframe, text=f"Gib deine Note für {self.modulename} ein: ")
            modulegrade_entry = tk.Entry(modulegradeframe, textvariable=modulegrade)
            modulegrade_button = tk.Button(modulegradeframe, text="Note eintragen", command=set_modulegrade)

            modulegradeframe.grid()
            modulegrade_label.grid()
            modulegrade_entry.grid()
            modulegrade_button.grid()

        def change_modulestatus(self):
            self.modulestatus = self.module.change_status(self.student_id)
            self.modulestatus_label.configure(text=f"{self.modulestatus}")

            if self.modulestatus == "offen":
                color = "lightblue"
                self.frame.configure(bg=color)
                self.modulename_label.configure(bg=color)
                self.modulestatus_label.configure(bg=color)
                self.modulestatus_button.configure(bg=color)

            if self.modulestatus == "in Bearbeitung":
                color = "orange"
                self.frame.configure(bg=color)
                self.modulename_label.configure(bg=color)
                self.modulestatus_label.configure(bg=color)
                self.modulestatus_button.configure(bg=color)

            if self.modulestatus == "abgeschlossen":
                color = "lightgreen"
                self.frame.configure(bg=color)
                self.modulename_label.configure(bg=color)
                self.modulestatus_label.configure(bg=color)
                self.modulestatus_button.configure(bg=color)

                self.modulegrade = self.set_modulegrade_entry()

            if self.modulestatus == "failed":
                color = "red"
                self.frame.configure(bg=color)
                self.modulename_label.configure(bg=color)
                self.modulestatus_label.configure(bg=color)
                self.modulestatus_button.configure(bg=color)

    # --- Assignment Modules to Semesters -----------------------------------------------------------------------------

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
            module = Moduleview(module, student_id, s, i)
            i += 1