"""This file contains the Class for the little Frames for every single Module."""
import tkinter as tk
from tkinter import ttk
from ui.theme import STATUS_OPEN, STATUS_IN_PROGRESS, STATUS_COMPLETED, STATUS_FAILED, STATUS_COLORS, FONT_MODULE

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


# --- FRAME FOR EVERY SINGLE MODULE -------------------------------------------------------------------------------------------------

class Moduleview:
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
        if self.modulestatus == STATUS_OPEN:
            bgc = STATUS_COLORS[STATUS_OPEN]
        if self.modulestatus == STATUS_IN_PROGRESS:
            bgc = STATUS_COLORS[STATUS_IN_PROGRESS]
        if self.modulestatus == STATUS_COMPLETED:
            bgc = STATUS_COLORS[STATUS_COMPLETED]
        if self.modulestatus == STATUS_FAILED:
            bgc = STATUS_COLORS[STATUS_FAILED]

        # --- STRUCTURE & ELEMENTS MODULEFRAME --------------------------------------------------------------------

        self.frame = tk.Frame(self.container, bg=bgc, borderwidth=1, relief="solid")
        self.frame.columnconfigure(0, weight=1, uniform="cols", pad=5)
        for r in range(4):
            self.frame.rowconfigure(r, weight=1)

        self.modulename_label = tk.Label(self.frame, text=f"{self.modulename}", wraplength=170, bg=bgc,
                                         font=FONT_MODULE, anchor="center")
        self.modulestatus_label = tk.Label(self.frame, text=f"{self.modulestatus}", bg=bgc,
                                           font=FONT_MODULE)
        self.modulestatus_button = tk.Button(self.frame, text="Status ändern", bg=bgc, font=FONT_MODULE,
                                             command=self.change_modulestatus)
        self.gradelabel = tk.Label(self.frame, bg=bgc, text=f"Note: {self.modulegrade}", wraplength=170,
                                   font=FONT_MODULE)

        self.modulename_label.grid(sticky="nswe", padx=1, pady=2)
        self.modulestatus_label.grid(sticky="nswe", padx=1, pady=1)
        self.modulestatus_button.grid(sticky="s", padx=1, pady=1)
        self.frame.grid(row=1, column=i, sticky="nswe", padx=1, pady=1)

        if self.modulestatus == STATUS_COMPLETED:
            self.modulestatus_label.destroy()
            self.modulestatus_button.destroy()
            self.gradelabel.grid(sticky="nswe", padx=5, pady=5)

        if self.modulestatus == STATUS_FAILED:
            self.modulestatus_label.destroy()
            self.gradelabel.grid(sticky="nswe", padx=5, pady=5)


    def change_modulestatus(self):
        new_modulestatus = tk.StringVar(value = self.modulestatus)
        new_modulegrade = tk.StringVar(value = self.modulegrade)

        def set_modulegrade():
            try:
                grade = float(modulegrade.get())
                self.module.set_grade(self.student_id, grade)
                change_status_frame.destroy()
                self.modulestatus_label.destroy()
                self.modulestatus_button.destroy()
                if grade > 4:
                    self.gradelabel = tk.Label(self.frame, bg=STATUS_COLORS[STATUS_FAILED], text=f"Note: {grade}", wraplength=150,
                                                font=FONT_MODULE)
                    self.modulestatus = STATUS_FAILED
                    color = STATUS_COLORS[STATUS_FAILED]
                    self.frame.configure(bg=color)
                    self.modulename_label.configure(bg=color)
                else:
                    self.gradelabel = tk.Label(self.frame, bg=STATUS_COLORS[STATUS_COMPLETED], text=f"Note: {grade}", wraplength=150,
                                                font=FONT_MODULE)
                self.gradelabel.grid(sticky="nswe", padx=5, pady=5)
                self.keyfigureview.keyfigureframe_refresh()
                return grade

            except ValueError:
                modulegradehint = tk.Label(change_status_frame,
                                            text="Deine Note muss eine Nachstelle haben. Nutze als Komma einen Punkt, z.B. 1.5")
                modulegradehint.grid()

        def check_new_status(event):
            new_status = new_modulestatus.get()
            if new_status == STATUS_COMPLETED:
                modulegrade_label = tk.Label(change_status_frame, text=f"Gib deine Note für {self.modulename} ein: ")
                modulegrade_entry = tk.Entry(change_status_frame, textvariable=new_modulegrade)
                modulegrade_label.grid(row=2, column=0, padx=5, pady=5)
                modulegrade_entry.grid(row=3, column=0, padx=5, pady=5)
                change_status_frame.after_idle(lambda: (modulegrade_entry.focus_set(), modulegrade_entry.icursor("end")))


        def save_new_status():
            new_status = new_modulestatus.get()
            modulegrade = new_modulegrade.get()
            if modulegrade == "NONE":
                self.module.change_status(self.student_id, new_status)
            else:
                self.module.set_grade(self.student_id, modulegrade.get())
                self.module.change_status(self.student_id, new_status)
            print(f"Neuer Status {new_status} wurde gespeichert.")


        change_status_frame = tk.Toplevel(self.container)
        change_status_label = tk.Label(change_status_frame, text=f"Ändere den Status für {self.modulename}:")
        modulestatus_combobox = ttk.Combobox(change_status_frame, textvariable=new_modulestatus, 
                                             values=[STATUS_OPEN, STATUS_IN_PROGRESS, STATUS_COMPLETED, STATUS_FAILED],
                                             state="readonly")
        save_button = tk.Button(change_status_frame, text="speichern", command=save_new_status)

        modulestatus_combobox.bind("<<ComboboxSelected>>", check_new_status)
        check_new_status(None)
        

        #modulegrade_button = tk.Button(change_status_frame, text="Note eintragen", command= lambda: (set_modulegrade()))

        change_status_label.grid(row=0, column=0, padx=5, pady=5)
        modulestatus_combobox.grid(row=1, column=0, padx=5, pady=5)
        save_button.grid(row=5, column=0, padx=5, pady=5)


        def set_modulegrade():
            if new_modulestatus.get() == STATUS_COMPLETED:
                modulegrade_label.grid(row=2, column=0, padx=5, pady=5)
                modulegrade_entry.grid(row=3, column=0, padx=5, pady=5)
                change_status_frame.after_idle(lambda: (modulegrade_entry.focus_set(), modulegrade_entry.icursor("end")))

            return modulegrade.get()

        

    #def change_modulestatus(self):
    #    self.modulestatus = self.module.change_status(self.student_id)
    #    self.modulestatus_label.configure(text=f"{self.modulestatus}")

    #    if self.modulestatus == STATUS_OPEN:
    #        color = STATUS_COLORS[STATUS_OPEN]
    #        self.frame.configure(bg=color)
    #        self.modulename_label.configure(bg=color)
    #        self.modulestatus_label.configure(bg=color)
    #        self.modulestatus_button.configure(bg=color)

     #   if self.modulestatus == STATUS_IN_PROGRESS:
     #       color = STATUS_COLORS[STATUS_IN_PROGRESS]
     #       self.frame.configure(bg=color)
     #       self.modulename_label.configure(bg=color)
     #       self.modulestatus_label.configure(bg=color)
     #       self.modulestatus_button.configure(bg=color)

    #    if self.modulestatus == STATUS_COMPLETED:
    #       color = STATUS_COLORS[STATUS_COMPLETED]
    #       self.frame.configure(bg=color)
    #       self.modulename_label.configure(bg=color)
    #       self.modulestatus_label.configure(bg=color)
    #       self.modulestatus_button.configure(bg=color)
    #       self.modulegrade = self.set_modulegrade_entry()

        self.keyfigureview.pie_chart_frame_refresh()
