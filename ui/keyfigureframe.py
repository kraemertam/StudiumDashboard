import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from controller.moduleprogress_controller import ModuleProgressController
from ui.theme import BG_COLOR, STATUS_COLORS, GRADEFRAME_BG, FRAME_BG, FONT_TITLE, FONT_SUBTITLE, FONT_TEXT

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# --- KEYFIGUREFRAME --------------------------------------------------------------------------------------------------

class Keyfigureframe:
    """This class contains the keyfigureframe, including the keyfigures gradetarget and piechart."""
    def __init__(self, student, container, *args, **kwargs):
        self.student = student
        self.container = container
        self.moduleprogress_controller = ModuleProgressController()
        self.metrics = self.moduleprogress_controller.get_dashboard_metrics(self.student)
        self.frame = tk.Frame(self.container, bg=FRAME_BG)
        self.frame.grid(row=1, sticky="nsew", padx=5, pady=5)
        self.frame.columnconfigure(0, weight=0, uniform="keycols", minsize=300)
        self.frame.columnconfigure(1, weight=0, uniform="keycols")
        self.frame.columnconfigure(2, weight=1, uniform="keycols")
        self.frame.rowconfigure(0, weight=1)
        self.frame.grid_propagate(False)
        self.frame.configure(height=300)

    def create_pie_chart(self):
        """Build the pie chart of the module status from the key figures."""
        statuses = list(self.metrics.status_counts.keys())
        sizes = list(self.metrics.status_counts.values())
   
        total = sum(sizes)
        shares = [round(s/total *100, 2) if total else 0 for s in sizes]
        labels = [f"{status}: {share}%" for status, share in zip(statuses, shares)]
        colors = [STATUS_COLORS[s] for s in statuses]

        fig = Figure(figsize=(3,3), dpi=100)
        fig.patch.set_facecolor(BG_COLOR)
        fig.subplots_adjust(right=0.75)
        ax = fig.add_subplot(111)
        ax.set_facecolor(BG_COLOR) 
        wedges, *_ = ax.pie(sizes, colors=colors, startangle=90)
        legend = ax.legend(wedges, labels, title="Modulstatus", loc="center left", bbox_to_anchor=(0.75, 0.5))
        legend.get_frame().set_facecolor(BG_COLOR)
        legend.get_frame().set_edgecolor(BG_COLOR)
        ax.axis("equal")
        ax.set_title("Übersicht über deinen Studienfortschritt")
        return fig

    def get_pie_chart(self):
        self.pieframe = tk.Frame(self.frame, bg=FRAME_BG)
        self.pieframe.grid(row=0, column=1, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.pieframe.grid_propagate(False)
        self.pieframe.rowconfigure(0, weight=1)
        self.pieframe.columnconfigure(0, weight=1)

        self.pie = self.create_pie_chart()
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

    def grade_target_feedback(self):
        """Return text color and feedback text for the grade target."""
        if self.metrics.average_grade is None:
            return "black", "Noch keine Note vorhanden."
        if self.metrics.grade_target is None:
            return "black", "Kein Notenziel festgelegt."
        if self.metrics.grade_difference > 0:
            return "red", f"Achtung! \nDu hast deine Zielnote um {self.metrics.grade_difference} überschritten!"
        return "black", "Super gemacht! \nDu befindest dich innerhalb deines Notenziels. Weiter so!"

    def get_gradeframe(self):
        self.gradeframe = tk.Frame(self.frame, bg=FRAME_BG)
        self.gradeframe.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.gradeframe.columnconfigure(0, weight=1)

        actual_grade_point_average = self.metrics.average_grade if self.metrics.average_grade is not None else "-"
        gradetarget = self.metrics.grade_target
        gradecolor, gradetargettext = self.grade_target_feedback()
        all_ects = self.metrics.ects_total
        achieved_ects = self.metrics.ects_achieved
        course = self.student.course
        infoframe = tk.Frame(self.gradeframe, bg=GRADEFRAME_BG)
        infoframe.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        course_label = tk.Label(infoframe, bg=GRADEFRAME_BG, text=f"Studiengang: {course.name}", font=FONT_SUBTITLE)
        ects_label = tk.Label(infoframe, bg=GRADEFRAME_BG, text=f"Erreichte ECTS-Punkte: {achieved_ects} / {all_ects}", font=FONT_SUBTITLE)
        course_label.grid(row=0, column=0, sticky="w", padx=15, pady=5)
        ects_label.grid(row=1, column=0, sticky="w", padx=15, pady=5)

        gradetargetframe = tk.Frame(self.gradeframe, bg=GRADEFRAME_BG)
        gradetargetframe.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        gradetarget_title_label = tk.Label(gradetargetframe, bg=GRADEFRAME_BG, text="Deine Notenübersicht:",
                                           font=FONT_TITLE)
        gradetargetlabel = tk.Label(gradetargetframe, bg=GRADEFRAME_BG, text=f"Dein Notenziel (durchschnittlich): {gradetarget}",
                                    font=FONT_SUBTITLE)
        grade_point_average_text = tk.Label(gradetargetframe, bg=GRADEFRAME_BG,
                                            text=f"Aktueller Notendurchschnitt: {actual_grade_point_average} ",
                                            font=FONT_SUBTITLE)
        gradetarget_info = tk.Label(gradetargetframe, bg=GRADEFRAME_BG, text=f"Fazit: {gradetargettext}", fg=gradecolor, font=FONT_TEXT, justify="left")

        gradetarget_title_label.grid(row=2, column=0, sticky="w", padx=15, pady=5)
        gradetargetlabel.grid(row=3, column=0, sticky="w", padx=15, pady=5)
        grade_point_average_text.grid(row=4, column=0, sticky="w", padx=15, pady=5)
        gradetarget_info.grid(row=5, column=0, sticky="w", padx=15, pady=5)

    def keyfigureframe_refresh(self):
        for w in self.frame.winfo_children():
            w.destroy()
        self.metrics = self.moduleprogress_controller.get_dashboard_metrics(self.student)
        self.get_gradeframe()
        self.get_pie_chart()

