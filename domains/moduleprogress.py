from dataclasses import dataclass
from enum import StrEnum
from domains.module import Module

@dataclass
class ModuleProgress:
    class Status(StrEnum):
        OPEN = "Offen"
        IN_PROGRESS = "In Bearbeitung"
        COMPLETED = "Bestanden"
        FAILED = "Nicht bestanden"

    student_id: str
    module: Module
    status: Status = Status.OPEN
    grade: float | None = None

    def change_status(self, new_status: Status):
        if new_status in (self.Status.OPEN, self.Status.IN_PROGRESS):
            self.grade = None
        self.status = new_status

    def set_grade(self, grade: float):
        if not (1.0 <= grade <= 5.0):
            raise ValueError("Eine Note muss zwischen 1.0 und 5.0 liegen.")
        self.grade = grade
        if self.grade > 4:
            self.change_status(self.Status.FAILED)
        else:
            self.change_status(self.Status.COMPLETED)


        