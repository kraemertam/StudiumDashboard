"""This file is for the GUI of the registration to come to the Overview."""
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.font as font
from pathlib import Path

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

from services.create_objects import create_student, create_new_student
from services.registration import login_student
from ui.overviewframe import overview_frame



def start_gui():
    dashboardframe = tk.Tk()
    dashboardframe.title("Dashboard fürs Studium")
    dashboardframe.geometry("800x1000")
    font.nametofont("TkDefaultFont").configure(size=10)
    dashboardframe.columnconfigure(0, weight=1, uniform="cols", pad=5)

    header = ttk.Label(dashboardframe, text="Dashboard - Übersicht fürs Studium")
    header.config(font=("Arial", 20))
    header.grid(padx=10, pady=10, sticky="n")

# ---WELCOMEFRAME-------------------------------------------------------------------------------------------------
    welcomeframe = tk.Frame(dashboardframe, bg="lightblue", borderwidth=1, relief="solid")

    image_path = Path(__file__).resolve().parent / "Schreibtisch.jpg"
    image = Image.open(image_path).resize((250, 200))
    photo = ImageTk.PhotoImage(image)
    label = ttk.Label(welcomeframe, text="Schön, dass du da bist!", image=photo, padding=5, compound="top")
    label.configure(anchor="center", justify="center")
    label.grid(row=0,column=0, pady=5, padx=5, sticky="ew")
    welcomeframe.grid(row=1, pady=50, padx=50, sticky="n")

# ---LOGINFRAME---------------------------------------------------------------------------------------------------
    loginframe = ttk.Frame(dashboardframe)

    loginframe.columnconfigure(0, weight=1)
    loginframe.rowconfigure(0, weight=1)
    header = ttk.Label(loginframe, text="Login")
    header.config(font=("Arial", 25))
    header.grid(row=0, padx=5, pady=5, sticky="n")
    loginframe.grid(row=2, sticky="n", padx=5, pady=5)

    student_id = tk.StringVar()

    def login_check():
        if student_id.get() == "":
            hint_label = tk.Label(loginframe, text="Gib zuerst deine Matrikelnummer ein. \n Falls du noch keine besitzt, wende dich ans Studiensekretäriat.", fg="red")
            hint_label.grid()
        else:
            print(f"Deine Matrikelnummer {student_id.get()} wird geprüft")
            check_student = login_student(student_id.get())
            if check_student[0] == True:
                if check_student[1] == True:
                    overview_frame(student_id.get(), dashboardframe)
                    loginframe.destroy()

                else:
                    enroll_course_frame(student_id.get())
                    loginframe.destroy()
            else:
                enroll_student_frame()
                loginframe.destroy()


    loginlabel = ttk.Label(loginframe, text="Gib deine Matrikelnummer ein: ")
    loginentry_id = ttk.Entry(loginframe, textvariable=student_id)
    loginentry_id.focus()
    loginbutton = ttk.Button(loginframe, text="Anmelden", command=login_check)
    loginlabel.grid(pady=5, padx=5, sticky="")
    loginentry_id.grid(pady=5, padx=5, sticky="")
    loginbutton.grid(pady=5, padx=5, sticky="")

# ---ENROLL COURSE FRAME----------------------------------------------------------------------------------------------
    def enroll_course_frame(student_id):
        student = create_student(student_id)

        enrollment_course = tk.Frame(dashboardframe)

        font.nametofont("TkDefaultFont").configure(size=10)
        header = ttk.Label(enrollment_course, text=f"Schön das du da bist {student.name}!", anchor="center")
        header.configure(font=("Arial", 20))
        header.grid(padx=50, pady=10, sticky="ew")
        enrollment_course.grid(pady=5, padx=5, sticky="")

        course_id = tk.StringVar()
        semester = tk.StringVar()

        def start_enrollment():
            student.enroll_course(course_id.get(), semester.get())
            done_label = tk.Label(enrollment_course, text="Du wurdest erfolgreich eingeschrieben.")
            done_label.grid(row=8, padx=50, pady=5, sticky="ew")
            print("Du wurdest erfolgreich angemeldet")

            overview_frame(student_id, dashboardframe)
            enrollment_course.destroy()
            dashboardframe.withdraw()

        explain_label = ttk.Label(enrollment_course, text="Aktuell liegen uns zu deinem Account noch keine Kursdaten vor. \nStarten wir also damit, dich in einen Kurs einzuschreiben.")
        enrollment_label = ttk.Label(enrollment_course, text="In welchen Kurs möchtest du dich einschreiben?", font=("Arial", (12), "bold"))
        enrollment_hint = tk.Label(enrollment_course, text="(Hinweis: Gib hier die Kurs-ID ein.)", font=("Arial", (8)))
        enrollment_entry = tk.Entry(enrollment_course, textvariable=course_id)
        enrollment_entry.focus()
        entrollment_semester = tk.Label(enrollment_course, text="Wieviele Semester studierst du?", font=("Arial", (12), "bold"),anchor="center")
        semester_entry = tk.Entry(enrollment_course, textvariable=semester)
        enrollment_button = tk.Button(enrollment_course, text="In Kurs einschreiben!", anchor="center", command=start_enrollment)

        explain_label.grid(row=1, padx=50, pady=5, sticky="w")
        enrollment_label.grid(row=2, padx=50, pady=5, sticky="w")
        enrollment_hint.grid(row=3, padx=50, sticky="w")
        enrollment_entry.grid(row=4, padx=50, pady=10, sticky="ew")
        entrollment_semester.grid(row=5, padx=50, pady=5, sticky="w")
        semester_entry.grid(row=6, padx=50, pady=5, sticky="ew")
        enrollment_button.grid(row=7, padx=50, pady=5, sticky="ew")

# --- ENROLL STUDENT FRAME ---------------------------------------------------------------------------------------------
    def enroll_student_frame():
        enrollment_student = tk.Frame(dashboardframe)
        font.nametofont("TkDefaultFont").configure(size=10)
        header = ttk.Label(enrollment_student, text="Lass uns deine Daten erfassen!", anchor="center")
        header.configure(font=("Arial", 20))
        header.grid(padx=50, columnspan=3, pady=10, sticky="ew")
        enrollment_student.grid(pady=5, padx=5, sticky="")

        for i in enumerate(range(10)):
            enrollment_student.columnconfigure(i, weight=1)
            enrollment_student.rowconfigure(i, weight=1)

        student_id = tk.StringVar()
        student_name = tk.StringVar()
        student_lastname = tk.StringVar()
        course_id = tk.StringVar()
        semester = tk.StringVar()

        def start_enrollment():
            print("Wir legen dich als Student an.")
            student = create_new_student(student_id.get(), student_name.get(), student_lastname.get())
            print("Du wurdest im Kurs eingeschrieben.")
            student.enroll_course(course_id.get(), semester.get())
            done_label = tk.Label(enrollment_student, text="Du wurdest erfolgreich eingeschrieben.")
            done_label.grid(row=11, padx=50, pady=5, sticky="ew")

            overview_frame(student_id.get(), dashboardframe)
            enrollment_student.destroy()
            dashboardframe.withdraw()


        explain_label = tk.Label(enrollment_student,
                                 text="Lass uns damit starten ein Profil für dich anzulegen. Hierfür benötigen wir deine Matrikelnummer. Falls du noch keine Matrikelnummer hast, wende dich bitte an das Studiensekretäriat.",
                                 wraplength=400, justify="left", anchor="w")
        student_id_label = ttk.Label(enrollment_student, text="Matrikelnummer: ", font=("Arial", (12), "bold"))
        student_id_entry = ttk.Entry(enrollment_student, textvariable=student_id)
        student_id_entry.focus()
        student_name_label = ttk.Label(enrollment_student, text="Vorname: ",font=("Arial", (12), "bold") )
        student_name_entry = ttk.Entry(enrollment_student, textvariable=student_name)
        student_lastname_label = ttk.Label(enrollment_student, text="Nachname: ", font=("Arial", (12), "bold"))
        student_lastname_entry = ttk.Entry(enrollment_student, textvariable=student_lastname)
        enrollment_label = ttk.Label(enrollment_student, text="In welchen Kurs möchtest du dich einschreiben?",
                                     font=("Arial", (12), "bold"))
        enrollment_hint = tk.Label(enrollment_student, text="(Hinweis: Gib hier die Kurs-ID ein.)", font=("Arial", (8)))
        enrollment_entry = tk.Entry(enrollment_student, textvariable=course_id)
        entrollment_semester = tk.Label(enrollment_student,
                                        text="Wieviele Semester studierst du?",
                                        font=("Arial", (12), "bold"))
        semester_entry = tk.Entry(enrollment_student, textvariable=semester)
        enrollment_button = tk.Button(enrollment_student, text="In Kurs einschreiben!", anchor="center",
                                      command=start_enrollment)

        explain_label.grid(row=1, columnspan=4,  padx=50, pady=5, sticky="ew")
        student_id_label.grid(row=2, column= 0, padx=(50,0), pady=5, sticky="ew")
        student_id_entry.grid(row=2, column= 1, padx=(5), pady=5, sticky="ew")
        student_name_label.grid(row=3, column= 0, padx=(50,0), pady=5, sticky="ew")
        student_name_entry.grid(row=3, column= 1, padx=5, pady=5, sticky="ew")
        student_lastname_label.grid(row=4, column= 0, padx=(50,0), pady=5, sticky="ew")
        student_lastname_entry.grid(row=4, column= 1, padx=5, pady=5, sticky="ew")
        enrollment_label.grid(row=5, columnspan=4, padx=50, pady=5, sticky="w")
        enrollment_hint.grid(row=6, columnspan=4, padx=50, sticky="w")
        enrollment_entry.grid(row=7, columnspan=4, padx=50, pady=10, sticky="ew")
        entrollment_semester.grid(row=8, columnspan=4, padx=50, pady=5, sticky="w")
        semester_entry.grid(row=9, columnspan=4, padx=50, pady=5, sticky="ew")
        enrollment_button.grid(row=10, columnspan=4, padx=50, pady=5, sticky="ew")

    dashboardframe.mainloop()