from dataclasses import dataclass
from data.moduleprogress import save_modules_changes, save_grade_changes
from domains.module import Module
from ui.theme import STATUS_OPEN, STATUS_IN_PROGRESS, STATUS_COMPLETED, STATUS_FAILED, STATUS_COLORS

@dataclass
class ModuleProgress:
    student_id: str
    module: Module
    status: str = STATUS_OPEN
    grade: float = None

    def change_status(self, student_id: str, new_status: str):
        self.status = new_status
        save_modules_changes(student_id, self.module.id, new_status)
        print(f"Status für Modul {self.module.name} wurde auf {new_status} geändert.")

    def set_grade(self, student_id: str, grade: float):
        self.grade = grade
        save_grade_changes(student_id, self.module.id, grade)
        print(f"Note für Modul {self.module.name} wurde auf {grade} gesetzt.")
        if self.grade > 4:
            self.change_status(student_id, STATUS_FAILED)
        else:
            self.change_status(student_id, STATUS_COMPLETED)


