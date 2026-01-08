"""This file contains the Class for the little Frames for every single Module."""
import tkinter as tk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# --- FRAME FOR EVERY SINGLE MODULE -------------------------------------------------------------------------------------------------

class Moduleview():
    def __init__(self, module, student_id, container, i, keyfigureview, *args, **kwargs):
        self.module = module
        self.moduleid = module.id
        self.modulename = module.name
        self.moduleetc = module.etc
        self.modulestatus = module.status
        self.modulegrade = module.grade
        self.container = container
        self.student_id = student_id
        self.keyfigureview = keyfigureview

        # --- Backgroundcolor configuration ---------------------------------------------------------------------------
        if self.modulestatus == "offen":
            bgc = "lightblue"
        if self.modulestatus == "in Bearbeitung":
            bgc = "orange"
        if self.modulestatus == "abgeschlossen":
            bgc = "lightgreen"
        if self.modulestatus == "nicht bestanden":
            bgc = "red"

        # --- STRUCTURE & ELEMENTS MODULEFRAME --------------------------------------------------------------------

        self.frame = tk.Frame(self.container, bg=bgc, borderwidth=1, relief="solid")
        self.frame.columnconfigure(0, weight=1, uniform="cols", pad=5)
        for r in range(4):
            self.frame.rowconfigure(r, weight=1)

        self.modulename_label = tk.Label(self.frame, text=f"{self.modulename}", wraplength=170, bg=bgc,
                                         font=("arial", 7, "bold"),
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

        if self.modulestatus == "nicht bestanden":
            self.modulestatus_label.destroy()
            self.modulestatus_button.destroy()
            self.gradelabel.grid(sticky="nswe", padx=5, pady=5)

    def set_modulegrade_entry(self):
        modulegrade = tk.StringVar()

        def set_modulegrade():
            try:
                grade = float(modulegrade.get())
                self.module.set_grade(self.student_id, grade)
                modulegradeframe.destroy()
                self.modulestatus_label.destroy()
                self.modulestatus_button.destroy()
                if grade > 4:
                    self.gradelabel = tk.Label(self.frame, bg="red", text=f"Note: {grade}", wraplength=150,
                                               font=("arial", 7, "bold"))
                    self.modulestatus = "nicht bestanden"
                    color = "red"
                    self.frame.configure(bg=color)
                    self.modulename_label.configure(bg=color)
                else:
                    self.gradelabel = tk.Label(self.frame, bg="lightgreen", text=f"Note: {grade}", wraplength=150,
                                               font=("arial", 7, "bold"))
                self.gradelabel.grid(sticky="nswe", padx=5, pady=5)
                self.keyfigureview.keyfigureframe_refresh()
                return grade

            except ValueError:
                modulegradehint = tk.Label(modulegradeframe,
                                           text="Deine Note muss eine Nachstelle haben. Nutze als Komma einen Punkt, z.B. 1.5")
                modulegradehint.grid()

        modulegradeframe = tk.Toplevel(self.container)
        modulegrade_label = tk.Label(modulegradeframe, text=f"Gib deine Note für {self.modulename} ein: ")
        modulegrade_entry = tk.Entry(modulegradeframe, textvariable=modulegrade)
        modulegrade_button = tk.Button(modulegradeframe, text="Note eintragen", command=set_modulegrade)

        modulegradeframe.grid()
        modulegrade_label.grid()
        modulegrade_entry.grid()
        modulegrade_button.grid()

        modulegradeframe.after_idle(lambda: (modulegrade_entry.focus_set(), modulegrade_entry.icursor("end")))

        return modulegrade.get()

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

        self.keyfigureview.pie_chart_frame_refresh()