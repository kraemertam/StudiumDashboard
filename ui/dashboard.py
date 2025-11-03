import tkinter as tk


def start_gui(studenstenInfo):
    root = tk.Tk()
    root.title("Studenten-Dashboard")
    name = studenstenInfo

    label = tk.Label(root, text=name)
    label.pack()

    root.mainloop()
