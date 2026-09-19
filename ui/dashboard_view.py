# ui/register_view.py
import tkinter as tk
from tkinter import ttk

from services.student_service import create_new_student
from services.moduleprogress_service import get_all_moduleprogress
from services.registration import get_available_courses
from services.enrollment_service import enrollment_student_in_course
from services.metrics_service import DashboardMetrics
from ui.keyfigureframe import Keyfigureframe
from ui.moduleframe import Moduleview


class DashboardView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, padding=40)
        self.controller = controller

        self.moduleprogress = get_all_moduleprogress(self.controller.student.id)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=0)

        header = ttk.Label(self, text=f"{self.controller.student.name}'s Studiendashboard!", anchor="center")
        header.config(font=("Arial", 20, "bold"))
        header.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

        # --- KEYFIGURE FRAME -------------------------------------------------------------------------------------------------
        self.keyfigureview = Keyfigureframe(self.controller.student, self)
        self.keyfigureview.get_pie_chart()
        self.keyfigureview.get_gradeframe()

        ttk.Separator(self, orient="horizontal").grid(row=2, sticky="ew")

        # --- MODULE FRAME-----------------------------------------------------------------------------------------------------
        MODULE_COLUMNS = 10

        moduloverview = tk.Frame(self)
        moduloverview.config(width=900, height=750)
        moduloverview.grid_propagate(False)
        moduloverview.grid(row=3, sticky="nsew", padx=10, pady=10)
        
        moduleheader = tk.Label(moduloverview, text="Modulübersicht", anchor="center")
        moduleheader.config(font=("Arial", 15, "bold"))
        moduleheader.grid(row=0, sticky="ew", padx=5, pady=5)
        
        moduloverview.columnconfigure(0, weight=1, uniform="cols", pad=5)
        moduloverview.grid(row=3, sticky="nsew", padx=10, pady=10)

        # For every Module from Student => eigenes Moduleframe 
        modulegrid = tk.Frame(moduloverview)
        modulegrid.grid(row=1, column=0, sticky="nsew")
        for c in range(MODULE_COLUMNS):
            modulegrid.columnconfigure(c, weight=1, uniform="modulecols")

        self.moduleviews = []
        for i, progress in enumerate(self.moduleprogress):
            row, col = divmod(i, MODULE_COLUMNS)
            view = Moduleview(progress, modulegrid, on_change=self.keyfigureview.keyfigureframe_refresh)
            view.frame.grid(row=row, column=col, sticky="nswe", padx=3, pady=3)
            self.moduleviews.append(view)
