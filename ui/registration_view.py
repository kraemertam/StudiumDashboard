# ui/register_view.py
import tkinter as tk
from tkinter import ttk
from controller.student_controller import StudentController
from controller.course_controller import CourseController
from ui.dashboard_view import DashboardView


class RegisterView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, padding=40)
        self.controller = controller
        self.student_controller = StudentController()
        self.course_controller = CourseController()

        # Header
        ttk.Label(self, text="Registrierung", font=("Arial", 20)).grid(row=0, padx= 10, pady=10, sticky="nswe")

        # Entry-Fields
        self.student_id = tk.StringVar()
        self.student_name = tk.StringVar()
        self.student_lastname = tk.StringVar()
        self.course = tk.StringVar()
        self.gradetarget = tk.StringVar()

        self.step1 = ttk.Frame(self)
        explain_label = tk.Label(self.step1,
            text="Lass uns damit starten ein Profil für dich anzulegen. Hierfür benötigen wir deine Matrikelnummer. Falls du noch keine Matrikelnummer hast, wende dich bitte an das Studiensekretäriat.",
            wraplength=400, justify="left", anchor="w")
        student_id_label = ttk.Label(self.step1, text="Matrikelnummer: ", font=("Arial", (12), "bold"))
        student_id_entry = ttk.Entry(self.step1, textvariable=self.student_id)
        student_id_entry.focus()
        student_name_label = ttk.Label(self.step1, text="Vorname: ",font=("Arial", (12), "bold") )
        student_name_entry = ttk.Entry(self.step1, textvariable=self.student_name)
        student_lastname_label = ttk.Label(self.step1, text="Nachname: ", font=("Arial", (12), "bold"))
        student_lastname_entry = ttk.Entry(self.step1, textvariable=self.student_lastname)
        student_check_button = tk.Button(self.step1, text="Student einschreiben!", anchor="center", command=self.registration_check)


        self.step2 = ttk.Frame(self)

        course_list = self.course_controller.get_all_courses()
        course_selection = [f"{course.id} - {course.name} ({course.ects})" for course in course_list]

        enrollment_label = ttk.Label(self.step2, text="In welchen Kurs möchtest du dich einschreiben?",
             font=("Arial", (12), "bold"))
        enrollment_hint = tk.Label(self.step2, text="(Hinweis: Wähle einen Kurs aus.)", font=("Arial", (8)))
        course_dropdown = ttk.Combobox(self.step2, textvariable=self.course, values=course_selection, state="readonly")
        gradetarget_label = tk.Label(self.step2, text="Welches Notenziel (Durchschnittsnote) möchtest du erreichen?",
            font=("Arial", (12), "bold"))
        gradetarget_entry = tk.Entry(self.step2, textvariable=self.gradetarget)
        enrollment_button = tk.Button(self.step2, text="In Kurs einschreiben!", anchor="center", command=self.course_enrollment_check)

        explain_label.grid(row=1, columnspan=4,  padx=10, pady=5, sticky="ew")
        student_id_label.grid(row=2, column= 0, padx=(10,0), pady=5, sticky="ew")
        student_id_entry.grid(row=2, column= 1, padx=(5), pady=5, sticky="ew")
        student_name_label.grid(row=3, column= 0, padx=(10,0), pady=5, sticky="ew")
        student_name_entry.grid(row=3, column= 1, padx=5, pady=5, sticky="ew")
        student_lastname_label.grid(row=4, column= 0, padx=(10,0), pady=5, sticky="ew")
        student_lastname_entry.grid(row=4, column= 1, padx=5, pady=5, sticky="ew")
        student_check_button.grid(row=5, column= 1, padx=5, pady=5, sticky="ew")

        enrollment_label.grid(row=1, columnspan=4, padx=10, pady=5, sticky="w")
        enrollment_hint.grid(row=2, columnspan=4, padx=10, sticky="w")
        course_dropdown.grid(row=3, columnspan=4,padx=10, pady=10, sticky="ew")
        gradetarget_label.grid(row=4, columnspan=4, padx=10, pady=5, sticky="w")
        gradetarget_entry.grid(row=5, columnspan=4, padx=10, pady=5, sticky="ew")
        enrollment_button.grid(row=6, columnspan=4, padx=10, pady=5, sticky="ew")

        self.status = ttk.Label(self, text="", foreground="red", wraplength=400)
        self.status.grid(row=8, columnspan=4, padx=10, pady=5, sticky="w")

        self.step1.grid(row=1, column=0, sticky="ew")
        self.step2.grid(row=1, column=0, sticky="ew")
        self.step2.grid_remove()

        

    def registration_check(self):
        self.status.config(text="", foreground="red")

        student_id = self.student_id.get().strip()
        student_name = self.student_name.get().strip()
        student_lastname = self.student_lastname.get().strip()

        # Check: Are all Variables filled. 
        missing = []
        if not student_id:
            missing.append("Matrikelnummer")
        if not student_name:
            missing.append("Vorname")
        if not student_lastname:
            missing.append("Nachname")

        if missing:
            self.status.config(text="Bitte fülle noch aus: " + ", ".join(missing))
            return

        # Student-Check
        try:
            student = self.student_controller.create_new_student(student_id, student_name, student_lastname)
        except ValueError as e:
            self.status.config(text=str(e))
            return
        
        self.controller.student = student
        self.status.config(text="Profil angelegt! Jetzt noch den Kurs wählen.", foreground="green")
        self.step1.grid_remove()
        self.step2.grid()

    def course_enrollment_check(self):
        self.status.config(text="", foreground="red")

        gradetarget = self.gradetarget.get().strip().replace(",", ".")
        course = self.course.get().strip()

        # Check: Are all Variables filled. 
        missing = []
        if not course:
            missing.append("Kurs")
        if not gradetarget:
            missing.append("Notenziel")       

        if missing:
            self.status.config(text="Bitte fülle noch aus: " + ", ".join(missing))
            return

        # Extracting Course-ID
        course_id = course.split(" -")[0].strip()

        # Enrollment Student in Course
        try:
            student = self.student_controller.enroll_student_in_course(self.controller.student.id, course_id, gradetarget)
        except ValueError as e:
            self.status.config(text=str(e))
            return
        self.controller.student = student
        self.status.config(text="In Kurs eingeschrieben!", foreground="green")
        self.controller.show(DashboardView)
