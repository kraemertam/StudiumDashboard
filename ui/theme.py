"""Centrale color and font definitions for the entire app."""

# --- COLORS -----------------------------------------------------

BG_COLOR = "#f0eeee"
FRAME_BG = "#f0eeee"
LABEL_BG = "#f0eeee"
GRADEFRAME_BG = "#e0dbdb"

# --- STATUS NAMES & COLORS ------------------------------------------

STATUS_OPEN = "offen"
STATUS_IN_PROGRESS = "in Bearbeitung"
STATUS_COMPLETED = "abgeschlossen"
STATUS_FAILED = "nicht bestanden"

STATUS_COLORS = {
    STATUS_OPEN: "#c4e8f1",
    STATUS_IN_PROGRESS: "#f8f690",
    STATUS_COMPLETED: "#9af7b6",
    STATUS_FAILED: "#EB6274",
}

# --- Fonts ----------------------------------------------------
FONT_TITLE = ("arial", 15, "bold")
FONT_SUBTITLE = ("arial", 11, "bold")
FONT_TEXT = ("arial", 11)
FONT_MODULE = ("arial", 7, "bold")
