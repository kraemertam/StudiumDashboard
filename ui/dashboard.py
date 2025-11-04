import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.font as font

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass



def start_gui():
    dashboardframe = tk.Tk()
    dashboardframe.title("Dashboard fürs Studium")
    dashboardframe.geometry("1000x900")
    dashboardframe.columnconfigure(0, weight=1)
    font.nametofont("TkDefaultFont").configure(size=10)
    dashboardframe.columnconfigure(0, weight=1)
    dashboardframe.rowconfigure(0, weight=1)

    header = ttk.Label(dashboardframe, text="Dashboard - Übersicht fürs Studium")
    header.config(font=("Arial", 20))
    header.grid(row=1, padx=10, pady=10)

    def start_login():
        loginframe = tk.Toplevel(dashboardframe)
        header = ttk.Label(loginframe, text="Login")
        header.config(font=("Arial", 20))
        header.grid(row=0, sticky="ew", padx=5, pady=5)
        #loginframe.grid(row=0, sticky="ew", padx=5, pady=5)

        student_id = tk.StringVar()

        def login_check():
            print(f"Deine Matrikelnummer {student_id.get()} wird geprüft")


        loginlabel = ttk.Label(loginframe, text="Gib deine Matrikelnummer ein: ")
        loginentry_id = ttk.Entry(loginframe, textvariable = student_id)
        loginbutton = ttk.Button(loginframe, text="Anmelden", command=login_check)
        loginlabel.grid(pady=50, padx=50, sticky="ew")
        loginentry_id.grid(pady=50, padx=50, sticky="ew")
        loginbutton.grid(pady=50, padx=50, sticky="ew")




    def startseite():
        welcomeframe = tk.Frame(dashboardframe)
        welcomeframe.grid(row=2, sticky="ew")

        image = Image.open("Schreibtisch.jpg").resize((250, 200))
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(welcomeframe, text="Schön, dass du da bist!", image=photo, padding=5, compound="top")
        label.grid(pady=50, padx=50, sticky="ew")

        ttk.Separator(dashboardframe, orient="horizontal").grid(sticky="ew")

        moduloverview = ttk.Frame(dashboardframe)

        header = ttk.Label(moduloverview, text="Modulübersicht")
        header.config(font=("Arial", 20))
        header.grid(row=0, sticky="ew", padx=5, pady=5)

        moduloverview.columnconfigure(0, weight=1, uniform="cols", pad=5)
        moduloverview.columnconfigure(1, weight=1, uniform="cols", pad=5)
        moduloverview.rowconfigure(1, weight=1, uniform="rows", pad=5)
        moduloverview.rowconfigure(2, weight=1, uniform="rows", pad=5)
        moduloverview.rowconfigure(3, weight=1, uniform="rows", pad=5)

        moduloverview.grid(sticky="nsew", padx=10, pady=10)


    hello_button = ttk.Button(dashboardframe, text="Los geht's", command=start_login)
    hello_button.grid(pady=50, padx=50, sticky="ew")

    dashboardframe.mainloop()


start_gui()