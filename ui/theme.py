"""Centrale color and font definitions for the entire app."""
from domains.moduleprogress import ModuleProgress

# --- COLORS -----------------------------------------------------

BG_COLOR = "#f0eeee"
FRAME_BG = "#f0eeee"
LABEL_BG = "#f0eeee"
GRADEFRAME_BG = "#e0dbdb"

# --- STATUS NAMES & COLORS ------------------------------------------
Status = ModuleProgress.Status

STATUS_COLORS = {
    Status.OPEN: "#c4e8f1",
    Status.IN_PROGRESS: "#f8f690",
    Status.COMPLETED: "#9af7b6",
    Status.FAILED: "#EB6274",
}

# --- Fonts ----------------------------------------------------
FONT_TITLE = ("arial", 15, "bold")
FONT_SUBTITLE = ("arial", 11, "bold")
FONT_TEXT = ("arial", 11)
FONT_MODULE = ("arial", 7, "bold")
