import sqlite3
from pathlib import Path

# --- DB: Save changes while session -----------------------------------------------------------------------------------
def save_modules_changes(student_id: str, module_id: str, module_status: str):
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("UPDATE studentoverview SET module_status = ? WHERE student_id = ? AND module_id = ?", (module_status, student_id, module_id))
    connection.commit()
    connection.close()
    print(f"Status wurde aktualisiert: {module_id}: {module_status}")


def save_grade_changes(student_id: str, module_id: str, module_grade: float):
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("UPDATE studentoverview SET module_grade = ? WHERE student_id = ? AND module_id = ?", (module_grade, student_id, module_id))
    connection.commit()
    connection.close()
    print(f"Status wurde aktualisiert: {module_id}: {module_grade}")
