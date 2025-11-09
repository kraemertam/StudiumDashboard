import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.font as font

from services.create_objects import create_modulliste, create_student
from services.registration import login_student

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


def start_gui():
    dashboardframe = tk.Tk()
    dashboardframe.title("Dashboard fürs Studium")
    dashboardframe.geometry("1000x900")
    font.nametofont("TkDefaultFont").configure(size=10)
    dashboardframe.columnconfigure(0, weight=1)
    dashboardframe.rowconfigure(0, weight=1)

    header = ttk.Label(dashboardframe, text="Dashboard - Übersicht fürs Studium")
    header.config(font=("Arial", 20))
    header.grid(padx=10, pady=10)

    image = Image.open("Schreibtisch.jpg").resize((250, 200))
    photo = ImageTk.PhotoImage(image)
    label = ttk.Label(dashboardframe, text="Schön, dass du da bist!", image=photo, padding=5, compound="top")
    label.configure(anchor="center", justify="center")
    label.grid(row =1, column=0, pady=50, padx=50, sticky="nsew")

    def start_login():
        loginframe = tk.Toplevel(dashboardframe)
        header = ttk.Label(loginframe, text="Login")
        header.config(font=("Arial", 20))
        header.grid(row=0, sticky="ew", padx=5, pady=5)

        student_id = tk.StringVar()

        def login_check():
            print(f"Deine Matrikelnummer {student_id.get()} wird geprüft")
            check = login_student(student_id.get())
            print(check)
            if check == True:
                startseite(student_id.get())
                loginframe.destroy()
            else:
                pass

        loginlabel = ttk.Label(loginframe, text="Gib deine Matrikelnummer ein: ")
        loginentry_id = ttk.Entry(loginframe, textvariable = student_id)
        loginbutton = ttk.Button(loginframe, text="Anmelden", command=login_check)
        loginlabel.grid(pady=50, padx=50, sticky="ew")
        loginentry_id.grid(pady=50, padx=50, sticky="ew")
        loginbutton.grid(pady=50, padx=50, sticky="ew")



    def startseite(student_id):

        modulliste = create_modulliste(student_id)
        print("Hi:", modulliste)
        student = create_student(student_id)
        print("Hi:", student)
        print(student.name)

        overview = tk.Toplevel(dashboardframe)
        overview.geometry("1000x900")
        overview.columnconfigure(0, weight=1)
        overview.rowconfigure(0, weight=1)

        header = ttk.Label(overview, text=f"Dashboard für dein Studium {student.name}", anchor="center")
        header.config(font=("Arial", 20))
        header.grid(sticky="ew", padx=5, pady=5)

        image = Image.open("Schreibtisch.jpg").resize((250, 200))
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(overview, text="Schön, dass du da bist!", image=photo, padding=5, compound="top", anchor="center")
        label.image = photo
        label.grid(row=3, pady=5, padx=5, sticky="ew")

        ttk.Separator(overview, orient="horizontal").grid(sticky="ew")

        moduloverview = ttk.Frame(overview)
        moduloverview.config(width=900, height=500)
        moduloverview.grid_propagate(False)
        header = ttk.Label(moduloverview, text="Modulübersicht", anchor="center")
        header.config(font=("Arial", 20))
        header.grid(row=0, columnspan=2, sticky="ew", padx=5, pady=5)

        moduloverview.columnconfigure(0, weight=1, uniform="cols", pad=5)
        moduloverview.columnconfigure(1, weight=1, uniform="cols", pad=5)
        moduloverview.columnconfigure(2, weight=1, uniform="cols", pad=5)
        moduloverview.columnconfigure(3, weight=1, uniform="cols", pad=5)
        moduloverview.columnconfigure(4, weight=1, uniform="cols", pad=5)
        moduloverview.rowconfigure(1, weight=1, uniform="rows", pad=5)
        moduloverview.rowconfigure(2, weight=1, uniform="rows", pad=5)
        moduloverview.rowconfigure(3, weight=1, uniform="rows", pad=5)

        moduloverview.grid(sticky="nsew", padx=10, pady=10)

        #for semester in range(5):
            #semesterframe = tk.Frame(moduloverview, bg="lightgrey", borderwidth=1, relief="solid")
            #semesterframe.columnconfigure(index=1, weight=1, uniform="cols", pad=5)

            #semesterframe.grid(row=s, sticky="nsew", padx=5, pady=5)
            #semestername_label = tk.Label(semesterframe, text=f"semester{s}", bg="lightblue", font=("arial", 6, "bold"))
            #semestername_label.grid(sticky="ew", padx=5, pady=5)


        for i, module in enumerate(modulliste):
            modulframe = tk.Frame(moduloverview, bg="lightblue", borderwidth=1, relief="solid")
            modulframe.columnconfigure(index = 1, weight=1, uniform="cols", pad=5)
            modulframe.grid(row=i, sticky="nsew", padx=5, pady=5)
            modulname_label = tk.Label(modulframe, text=f"{module.name}", bg="lightblue", font=("arial", 6, "bold"))
            modulstatus_label = tk.Label(modulframe, text=f"{module.status}", bg="lightblue", font=("arial", 5, "bold"))
            modulstatus_button = tk.Button(modulframe, text="Status ändern", bg="lightblue", font=("arial", 5, "bold"))

            modulname_label.grid(sticky="ew", padx=5, pady=5)
            modulstatus_label.grid(sticky="ew", padx=5, pady=5)
            modulstatus_button.grid(sticky="ew", padx=5, pady=5)




    start_button = ttk.Button(dashboardframe, text="Los geht's", command=start_login)
    start_button.grid(pady=50, padx=50, sticky="n")

    dashboardframe.mainloop()


start_gui()