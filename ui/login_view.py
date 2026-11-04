import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from pathlib import Path
from controller.student_controller import StudentController
from ui.registration_view import RegisterView
from ui.dashboard_view import DashboardView


class LoginView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, padding=40)
        self.controller = controller
        self.student_controller = StudentController()

        # Header 
        header = ttk.Label(self, text="Dashboard - Übersicht fürs Studium")
        header.config(font=("Arial", 20))
        header.grid(row=0, padx=10, pady=10, sticky="nswe")

        # Image & Welcome-Text
        image_path = Path(__file__).resolve().parent / "Schreibtisch.jpg"
        image = Image.open(image_path).resize((250, 200))
        self.photo = ImageTk.PhotoImage(image)
        label = ttk.Label(self, text="Schön, dass du da bist!", image=self.photo, padding=5, compound="top")
        label.configure(anchor="center", justify="center")
        label.grid(row=1,column=0, pady=5, padx=5, sticky="ew")

        # Login
        ttk.Label(self, text="Login", font=("Arial", 25)).grid(row=2, pady=20)
        ttk.Label(self, text="Gib deine Matrikelnummer ein:").grid(row=3, pady=5)

        self.student_id = tk.StringVar()
        entry = ttk.Entry(self, textvariable=self.student_id)
        entry.grid(row=4, pady=5)
        entry.focus()

        ttk.Button(self, text="Anmelden", command=self.on_login).grid(row=5, pady=10)

        # Login-Statuslabel
        self.status = ttk.Label(self, text="", foreground="red")
        self.status.grid(row=6, pady=5)

        ttk.Button(self, text="Noch nicht registriert?",
           command=lambda: self.controller.show(RegisterView)).grid(row=7, pady=5)

    def on_login(self):
        self.status.config(text="")
        student_id = self.student_id.get().strip()

        if not student_id:
            self.status.config(text="Bitte gib deine Matrikelnummer ein.")
            return
        try:
            student = self.student_controller.login(student_id)
        except ValueError as e:
            self.status.config(text=f"Fehler beim Login: {e}")
            return

        self.controller.student = student
        self.status.config(text=f"Willkommen, {student.name}!", foreground="green")
        self.controller.show(DashboardView)
    