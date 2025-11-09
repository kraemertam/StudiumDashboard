import tkinter as tk
import Class_Module
from Class_Module import Module

class ModuleView():

    def __init__(self, modules, container, index, *args, **kwargs):
        self.modulname = modules["Modulname"]
        self.modulstatus = modules["Status"]
        self.moduletc = modules["ETC"]
        self.container = container
        self.index = index

        self.frame = tk.Frame(self.container, bg="lightblue", borderwidth=1, relief="solid")


        self.frame.columnconfigure(index=self.index, weight=1, uniform="cols", pad=5)
        self.frame.grid(row=0, column=self.index, sticky="nsew", padx=5, pady=5)

        self.modulname_label = tk.Label(self.frame, text=f"{self.modulname}", bg="lightblue", font=("arial", 15, "bold"))
        self.modulname_label.grid(sticky="ew", padx=5, pady=5)

        self.modulstatus_label= tk.Label(self.frame, text=f"Status: {self.modulstatus}", bg="lightblue", font=("arial", 10))
        self.modulstatus_label.grid(sticky="ew", padx=5, pady=5)

        self.status_button = tk.Button(self.frame, font=("Arial",8), text="Status ändern", command=self.change_status)
        self.status_button.grid(padx=20, pady=20, sticky="ew")

        # --- Weite des Frames je nach ETCs ----
        if self.moduletc == 5:
            print(self.moduletc)
            self.frame.configure(width=130, height= 140, relief="solid")
            self.frame.grid_propagate(False)

        if self.moduletc == 10:
            self.frame.configure(width=260, height = 140, relief="solid")
            self.frame.grid_propagate(False)

        # --- Farben für Status ----
        if self.modulstatus == "open":
            color = "lightblue"
            self.frame.configure(bg=color)
            self.modulname_label.configure(bg=color)
            self.modulstatus_label.configure(bg=color)

        if self.modulstatus == "activ":
            color = "orange"
            self.frame.configure(bg=color)
            self.modulname_label.configure(bg=color)
            self.modulstatus_label.configure(bg=color)
        if self.modulstatus == "done":
            color = "lightgreen"
            self.frame.configure(bg=color)
            self.modulname_label.configure(bg=color)
            self.modulstatus_label.configure(bg=color)
        if self.modulstatus == "failed":
            color = "red"
            self.frame.configure(bg=color)
            self.modulname_label.configure(bg=color)
            self.modulstatus_label.configure(bg=color)

    def change_status(self):
        Class_Module.Module.change_status(self)
        self.modulstatus_label.configure(text=f"{self.modulstatus}")
        if self.modulstatus == "open":
            color = "lightblue"
            self.frame.configure(bg=color)
            self.modulname_label.configure(bg=color)
            self.modulstatus_label.configure(bg=color)

        if self.modulstatus == "activ":
            color = "orange"
            self.frame.configure(bg=color)
            self.modulname_label.configure(bg=color)
            self.modulstatus_label.configure(bg=color)
        if self.modulstatus == "done":
            color = "lightgreen"
            self.frame.configure(bg=color)
            self.modulname_label.configure(bg=color)
            self.modulstatus_label.configure(bg=color)
        if self.modulstatus == "failed":
            color = "red"
            self.frame.configure(bg=color)
            self.modulname_label.configure(bg=color)
            self.modulstatus_label.configure(bg=color)



