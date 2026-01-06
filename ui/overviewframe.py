"""This file creates the GUI for the dashboard for the course overview."""
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import services.semesterassigment
from services.create_objects import create_modulliste, create_student
from services.key_figures import pie_chart, grade_point_average

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# --- Dashboard Frame -------------------------------------------------------------------------------------------------

def overview_frame(student_id, dashboardframe):
    modulliste = create_modulliste(student_id)
    student = create_student(student_id)

    overview = tk.Toplevel(dashboardframe)
    overview.geometry("1500x900")
    overview.columnconfigure(0, weight=1)
    overview.rowconfigure(0, weight=1)

    header = ttk.Label(overview, text=f"Dashboard für dein Studium {student.name}", anchor="center")
    header.config(font=("Arial", 20))
    header.grid(row=0, padx=0, pady=0)



# --- KEYFRAME --------------------------------------------------------------------------------------------------------
    keyframe = tk.Frame(overview)
    keyframe.grid(row=1, sticky="nsew", padx=5, pady=5)
    keyframe.columnconfigure(0, weight=1)
    keyframe.columnconfigure(1, weight=1)
# --- PIECHART --------------------------------------------------------------------------------------------------------
    pie = pie_chart(student_id)
    pie_canvas = FigureCanvasTkAgg(pie, master=keyframe)
    pie_canvas.draw()
    pie_canvas.get_tk_widget().grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

# --- WELCOME & GRADES ----------------------------------------------------------------------------------------------------------

    gradeframe = tk.Frame(keyframe)
    gradeframe.grid(row=0, column=0,  sticky="nsew", padx=5, pady=5)
    gradeframe.rowconfigure(0, weight=1)
    gradeframe.rowconfigure(1, weight=1)
    gradeframe.rowconfigure(2, weight=1)
    gradeframe.columnconfigure(0, weight=1)

    welcome_label = tk.Label(gradeframe, text=f"Willkommen {student.name}!",font=("arial", 20, "bold"))
    welcome_label.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    grade_info = grade_point_average(student_id)
    actual_grade_point_average = grade_info[0]
    gradecolor = grade_info[1]
    gradetargettext = grade_info[2]
    grade_point_average_text = tk.Label(gradeframe, text=f"Dein aktueller Notendurchschnitt:\n{actual_grade_point_average} ",
                                        fg=gradecolor, justify="center", anchor="center", font=("arial", 12, "bold"))
    gradetarget_info = tk.Label(gradeframe, text=gradetargettext, font=("arial", 10))
    grade_point_average_text.grid(row=1, column=0, sticky="nsew", padx=5, pady=0)
    gradetarget_info.grid(row=2, column=0, sticky="nsew", padx=5, pady=0)

    ttk.Separator(overview, orient="horizontal").grid(row=3, sticky="ew")


# ----- MODULEFRAME -----------------------------------------------------------------------------------------------------
    moduloverview = tk.Frame(overview)
    moduloverview.config(width=900, height=750)
    moduloverview.grid_propagate(False)
    header = tk.Label(moduloverview, text="Modulübersicht", anchor="center")
    header.config(font=("Arial", 20))
    header.grid(row=0, columnspan=2, sticky="ew", padx=5, pady=5)

    moduloverview.columnconfigure(0, weight=1, uniform="cols", pad=5)
    moduloverview.columnconfigure(1, weight=1, uniform="cols", pad=5)
    for x in range(int(student.semester/2+2)):
        moduloverview.rowconfigure(x, weight=1, uniform="rows", pad=5)

    moduloverview.grid(sticky="nsew", padx=10, pady=10)

    # --- SEMESTERFRAME -----------------------------------------------------------------------------------------------
    semesters = []
    for x, semester in enumerate(range((student.semester +1 ))):
        reihe = x // 2 + 1
        spalte = x % 2
        semester = tk.Frame(moduloverview)
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

            # --- Backgroundcolor configuration -----------------------------------------------------------------------
            if self.modulestatus == "offen":
                bgc = "lightblue"
            if self.modulestatus == "in Bearbeitung":
                bgc = "orange"
            if self.modulestatus == "abgeschlossen":
                bgc = "lightgreen"

            # --- STRUCTURE & ELEMENTS MODULEFRAME --------------------------------------------------------------------

            self.frame = tk.Frame(self.container, bg=bgc, borderwidth=1, relief="solid")
            self.frame.columnconfigure(0, weight=1, uniform="cols", pad=5)
            for r in range(4):
                self.frame.rowconfigure(r, weight=1)

            self.modulename_label = tk.Label(self.frame, text=f"{self.modulename}", wraplength=170, bg=bgc, font=("arial", 7, "bold"),
                                             anchor="center")
            self.modulestatus_label = tk.Label(self.frame, text=f"{self.modulestatus}", bg=bgc,
                                               font=("arial", 6, "bold"))
            self.modulestatus_button = tk.Button(self.frame, text="Status ändern", bg=bgc, font=("arial", 6, "bold"),
                                                 command=self.change_modulestatus)
            self.gradelabel = tk.Label(self.frame, bg=bgc, text=f"Note: {self.modulegrade}", wraplength=170,
                                       font=("arial", 7, "bold"))

            self.modulename_label.grid(sticky="nswe", padx=1, pady=2)
            self.modulestatus_label.grid(sticky="nswe", padx=1, pady=1)
            self.modulestatus_button.grid(sticky="s", padx=1, pady=1)
            self.frame.grid(row=1, column=i, sticky="nswe", padx=1, pady=1)

            if self.modulestatus == "abgeschlossen":
                self.modulestatus_label.destroy()
                self.modulestatus_button.destroy()
                self.gradelabel.grid(sticky="nswe", padx=5, pady=5)


        def set_modulegrade_entry(self):
            modulegrade = tk.StringVar()

            def set_modulegrade():
                print(type(modulegrade.get()))
                try:
                    grade = float(modulegrade.get())
                    print(type(grade))
                    self.module.set_grade(self.student_id, grade)
                    modulegradeframe.destroy()
                    self.modulestatus_label.destroy()
                    self.modulestatus_button.destroy()
                    self.gradelabel = tk.Label(self.frame, bg= "lightgreen", text=f"Note: {grade}", wraplength=150, font=("arial", 7, "bold"))
                    self.gradelabel.grid(sticky="nswe", padx=5, pady=5)

                    return grade
                except ValueError:
                    modulegradehint = tk.Label(modulegradeframe, text="Deine Note muss eine Nachstelle haben. Nutze als Komma einen Punkt, z.B. 1.5")
                    modulegradehint.grid()

            modulegradeframe = tk.Toplevel(moduloverview)
            modulegrade_label = tk.Label(modulegradeframe, text=f"Gib deine Note für {self.modulename} ein: ")
            modulegrade_entry = tk.Entry(modulegradeframe, textvariable=modulegrade)
            modulegrade_entry.focus()
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

    modules_per_semster = services.semesterassigment.semester_assign(student, modulliste)
    semester_divide = dict(zip(semesters, modules_per_semster))

    for s in semester_divide:
        m = semester_divide[s]
        i=0
        for module in m:
            s.columnconfigure(i, weight=1, uniform="modules")
            Moduleview(module, student_id, s, i)
            i += 1