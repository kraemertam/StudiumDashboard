"""Main window of the application. Navigates between different pages."""

import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    """Main window of the application. Holds the logged-in student and switches between views."""
    def __init__(self):
        super().__init__() # Calls the constructor of tk.Tk
        self.title("Dashboard fürs Studium")
        self.geometry("700x900")

        # Container in which all views are stacked on top of each other.
        self.container = ttk.Frame(self)
        self.container.pack(fill="both", expand=True)
        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)

        self.current_frame = None    # currently displayed frame
        self.student = None          # currently logged-in student

    def show(self, frame_class, **kwargs) -> None:
        """Replace the current view with a new one."""
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = frame_class(self.container, self, **kwargs)
        self.current_frame.grid(row=0, column=0, sticky="nsew")