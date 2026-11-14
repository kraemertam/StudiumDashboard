"""This file contains the Class for the little Frames for every single Module."""
import tkinter as tk
from tkinter import ttk
from domains.moduleprogress import ModuleProgress
from controller.moduleprogress_controller import ModuleProgressController
from ui.theme import STATUS_COLORS, FONT_MODULE

Status = ModuleProgress.Status

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


# --- FRAME FOR EVERY SINGLE MODULEPROGRESS --------------------------------------------------------------------------------------

class Moduleview:
    def __init__(self, progress, container, on_change = None):
        self.moduleprogress = progress
        self.container = container
        self.on_change = on_change
        self.moduleprogress_controller = ModuleProgressController()


        # --- STRUCTURE & ELEMENTS OF MODULEFRAME --------------------------------------------------------------------

        self.frame = tk.Frame(self.container, borderwidth=1, relief="solid")
        self.frame.columnconfigure(0, weight=1, uniform="cols", pad=5)
        for r in range(5):
            self.frame.rowconfigure(r, weight=1)


        self.modulename_label = tk.Label(self.frame, text=f"{self.moduleprogress.module.name}", wraplength=170,
                                         font=FONT_MODULE, anchor="center")
        self.ects_label = tk.Label(self.frame, text=f"{self.moduleprogress.module.ects} ECTS-Punkte", font=FONT_MODULE)
        self.status_label = tk.Label(self.frame, text=f"{self.moduleprogress.status}",
                                           font=FONT_MODULE)
        self.status_button = tk.Button(self.frame, text="Status ändern", font=FONT_MODULE,
                                             command=self.open_status_dialog)
        self.gradelabel = tk.Label(self.frame, text=f"Note: {self.moduleprogress.grade}", wraplength=170,
                                   font=FONT_MODULE)

        self.modulename_label.grid(row=0, sticky="nswe", padx=1, pady=2)
        self.ects_label.grid(row=1,sticky="nswe", padx=1, pady=2 )
        self.status_label.grid(row=2, sticky="nswe", padx=1, pady=1)
        self.gradelabel.grid(row=3, sticky="nswe", padx=5, pady=5)
        self.status_button.grid(row=4, sticky="s", padx=1, pady=1)

        self.render()
    # --- DRAWS THE TILE ACCORDING TO THE CURRENT PROGRESS --------------------------------------------------------------------
    def render(self):
        """Updates colors, labels and visibility to match the current module progress."""
        color = STATUS_COLORS[self.moduleprogress.status]
        for widget in (self.frame, self.modulename_label, self.ects_label, self.status_label, self.gradelabel, self.status_button):
            widget.configure(bg=color)

        self.modulename_label.configure(text=self.moduleprogress.module.name)
        self.status_label.configure(text=self.moduleprogress.status)

        if self.moduleprogress.grade is None:
            self.gradelabel.grid_remove()
            self.status_label.grid()
        else:
            self.gradelabel.configure(text=f"Note: {self.moduleprogress.grade}")
            self.gradelabel.grid()
            self.status_label.grid_remove()


# --- CHANGE THE STATUS OF A MODULE -------------------------------------------------------------------
    def open_status_dialog(self):
        dialog_status_change = tk.Toplevel(self.container)
        dialog_status_change.title(self.moduleprogress.module.name)

        new_moduleprogress = tk.StringVar(value = self.moduleprogress.status)
        new_modulegrade = tk.StringVar(value = self.moduleprogress.grade)

        dialog_label = tk.Label(dialog_status_change, text=f"Ändere den Status für {self.moduleprogress.module.name}:")
        moduleprogress_combobox = ttk.Combobox(dialog_status_change, textvariable=new_moduleprogress, 
                                             values=[Status.OPEN, Status.IN_PROGRESS, Status.COMPLETED, Status.FAILED],
                                             state="readonly")
        grade_label = tk.Label(dialog_status_change, text="Note (z.B. 1.5):")
        grade_entry = tk.Entry(dialog_status_change, textvariable=new_modulegrade)
        hint = tk.Label(dialog_status_change, fg="red", wraplength=250)
        
        dialog_label.grid(row=0, column=0, padx=5, pady=5)
        moduleprogress_combobox.grid(row=1, column=0, padx=5, pady=5)


        def toggle_grade_field(event=None):
            if new_moduleprogress.get() in (Status.COMPLETED, Status.FAILED):
                grade_label.grid(row=2, column=0, padx=5, pady=5)
                grade_entry.grid(row=3, column=0, padx=5, pady=5)
                grade_entry.focus_set()
            else:
                grade_label.grid_remove()
                grade_entry.grid_remove()

        def save():
            status = Status(new_moduleprogress.get())
            grade = None
            if status in (Status.COMPLETED, Status.FAILED):
                try:
                    grade = float(new_modulegrade.get().strip().replace(",", "."))
                except ValueError:
                    hint.configure(text="Nutze als Komma einen Punkt, z.B. 1.5")
                    hint.grid(row=4, column=0, padx=5, pady=5)
                    return
            try:
                self.moduleprogress_controller.update_moduleprogress(self.moduleprogress, status, grade)
            except ValueError as e:
                hint.configure(text=str(e))
                hint.grid(row=4, column=0, padx=5, pady=5)
                return

            self.render()
            if self.on_change is not None:
                self.on_change()
            dialog_status_change.destroy()

        save_button = tk.Button(dialog_status_change, text="speichern", command=save
                  )
        save_button.grid(row=5, column=0, padx=5, pady=5)

        moduleprogress_combobox.bind("<<ComboboxSelected>>", toggle_grade_field)
        toggle_grade_field()
                
