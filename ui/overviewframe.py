"""This file creates the GUI for the dashboard for the course overview."""
import tkinter as tk
from tkinter import ttk

import services.semesterassigment
from services.create_objects import create_modulliste, create_student
from ui.keyfigureframe import Keyfigureframe
from ui.moduleframe import Moduleview

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# --- DASHBOARD FRAME -------------------------------------------------------------------------------------------------

def overview_frame(student_id, dashboardframe):
    modulliste = create_modulliste(student_id)
    student = create_student(student_id)

    overview = tk.Toplevel(dashboardframe)
    overview.geometry("1500x900")
    overview.columnconfigure(0, weight=1)
    overview.rowconfigure(0, weight=0)
    overview.rowconfigure(1, weight=0)
    overview.rowconfigure(2, weight=0)
    overview.rowconfigure(3, weight=0)

    header = ttk.Label(overview, text=f"{student.name}'s Studiendashboard!", anchor="center")
    header.config(font=("Arial", 20, "bold"))
    header.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
    overview.lift()

# --- KEYFIGURE FRAME -------------------------------------------------------------------------------------------------
    keyfigureview = Keyfigureframe(student, overview)
    keyfigureview.get_pie_chart()
    keyfigureview.get_gradeframe()

    ttk.Separator(overview, orient="horizontal").grid(row=2, sticky="ew")

# ----- MODULE OVERVIEW FRAME -----------------------------------------------------------------------------------------------------
    moduloverview = tk.Frame(overview)
    moduloverview.config(width=900, height=750)
    moduloverview.grid_propagate(False)

    moduleheader = tk.Label(moduloverview, text="Modulübersicht", anchor="center")
    moduleheader.config(font=("Arial", 15, "bold"))
    moduleheader.grid(row=0, columnspan=2, sticky="ew", padx=5, pady=5)

    moduloverview.columnconfigure(0, weight=1, uniform="cols", pad=5)
    moduloverview.columnconfigure(1, weight=1, uniform="cols", pad=5)
    moduloverview.grid(row=3, sticky="nsew", padx=10, pady=10)

    def change_moduleinformation():
        pass

    change_moduleinformation_button = tk.Button(moduloverview, text="Modulinfo anpassen", font=("arial", 8))
    change_moduleinformation_button.grid(row=0, column=1, sticky="e", padx=5, pady=5)

    semesters = []
    for x, semester in enumerate(range((student.semester +1 ))):
        reihe = x // 2 + 1
        spalte = x % 2
        semester = tk.Frame(moduloverview)
        semester.grid(row=reihe, column=spalte, sticky="nsew", padx=10, pady=10)
        semesters.append(semester)

    modules_per_semster = services.semesterassigment.semester_assign(student, modulliste)
    semester_divide = dict(zip(semesters, modules_per_semster))

    for s in semester_divide:
        m = semester_divide[s]
        i=0
        for module in m:
            s.columnconfigure(i, weight=1, uniform="modules")
            Moduleview(module, student_id, s, i, keyfigureview)
            i += 1