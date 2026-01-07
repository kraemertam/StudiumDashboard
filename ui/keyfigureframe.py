import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import services.semesterassigment
from services.create_objects import create_modulliste, create_student
from services.keyfigures import pie_chart, grade_point_average

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# --- KEYFIGUREFRAME --------------------------------------------------------------------------------------------------

class keyfigureframe():
    def __init__(self, student_id, container, *args, **kwargs):
        self.student_id = student_id
        self.container = container

        self.frame = tk.Frame(self.container, bg="white")
        self.frame.grid(row=1, sticky="nsew", padx=5, pady=5)
        self.frame.columnconfigure(0, weight=0, uniform="keycols", minsize=300)
        self.frame.columnconfigure(1, weight=0, uniform="keycols")
        self.frame.columnconfigure(2, weight=1, uniform="keycols")
        self.frame.rowconfigure(0, weight=1)
        self.frame.grid_propagate(False)
        self.frame.configure(height=300)


    def get_pie_chart(self):
        self.pieframe = tk.Frame(self.frame, bg="white")
        self.pieframe.grid(row=0, column=1, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.pieframe.grid_propagate(False)
        self.pieframe.rowconfigure(0, weight=1)
        self.pieframe.columnconfigure(0, weight=1)

        self.pie = pie_chart(self.student_id)
        self.pie_canvas = FigureCanvasTkAgg(self.pie, master=self.pieframe)
        w = self.pie_canvas.get_tk_widget()
        w.grid(row=0, column=0, sticky="nsew",padx=15, pady=5)
        self.pieframe.update_idletasks()
        self.pie_canvas.draw_idle()

        def _resize_to_frame(event=None):
            width = self.pieframe.winfo_width()
            height = self.pieframe.winfo_height()
            if width < 10 or height < 10:
                return
            dpi = self.pie.get_dpi()
            self.pie.set_size_inches(width / dpi, height / dpi, forward=True)
            try:
                self.pie.tight_layout()
            except Exception:
                pass
            self.pie_canvas.draw_idle()

        self.pieframe.bind("<Configure>", lambda e: _resize_to_frame())
        self.pieframe.after_idle(_resize_to_frame)


    def get_gradeframe(self):
        self.gradeframe = tk.Frame(self.frame, bg="white")
        self.gradeframe.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        for r in range(4):
            self.gradeframe.rowconfigure(r, weight=0)
        self.gradeframe.columnconfigure(0, weight=1)

        grade_info = grade_point_average(self.student_id)
        actual_grade_point_average = grade_info[0]
        gradetarget = grade_info[1]
        gradecolor = grade_info[2]
        gradetargettext = grade_info[3]

        gradetarget_title_label = tk.Label(self.gradeframe, bg="white", text="Deine Notenübersicht:",
                                           font=("arial", 15, "bold"))
        gradetargetlabel = tk.Label(self.gradeframe, bg="white", text=f"Ziel für den Notendurschnitt: {gradetarget}",
                                    font=("arial", 11, "bold"))
        grade_point_average_text = tk.Label(self.gradeframe, bg="white",
                                            text=f"Aktueller Notendurchschnitt: {actual_grade_point_average} ",
                                            font=("arial", 11, "bold"))
        gradetarget_info = tk.Label(self.gradeframe, bg="white", text=f"Fazit: {gradetargettext}", fg=gradecolor, font=("arial", 11))

        gradetarget_title_label.grid(row=0, column=0, sticky="w", padx=30, pady=15)
        gradetargetlabel.grid(row=1, column=0, sticky="w", padx=30, pady=15)
        grade_point_average_text.grid(row=2, column=0, sticky="w", padx=30, pady=15)
        gradetarget_info.grid(row=3, column=0, sticky="nswe", padx=30, pady=15)


    def keyfigureframe_refresh(self):
        for w in self.frame.winfo_children():
            w.destroy()
        self.get_gradeframe()
        self.get_pie_chart()

    def pie_chart_frame_refresh(self):
        for w in self.pieframe.winfo_children():
            w.destroy()
        self.get_pie_chart()

