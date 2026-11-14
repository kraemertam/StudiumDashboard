from enum import StrEnum
from domains.module import Module


class ModuleProgress:
    class Status(StrEnum):
        OPEN = "Offen"
        IN_PROGRESS = "In Bearbeitung"
        COMPLETED = "Bestanden"
        FAILED = "Nicht bestanden"

    def __init__(self, student_id: str, module: Module, status: Status = Status.OPEN, grade: float | None = None):
        self.student_id = student_id
        self.module = module
        self._status = ModuleProgress.Status.OPEN
        self._grade = None
        if grade is not None:
            self.grade = grade
        else:
            self.change_status(status)

    @property
    def status(self) -> Status:
        return self._status

    @property
    def grade(self) -> float | None:
        return self._grade

    @grade.setter
    def grade(self, grade: float) -> None:
        if not (1.0 <= grade <= 5.0):
            raise ValueError("Eine Note muss zwischen 1.0 und 5.0 liegen.")
        self._grade = grade
        if self._grade > 4:
            self._status = ModuleProgress.Status.FAILED
        else:
            self._status = ModuleProgress.Status.COMPLETED

    def change_status(self, new_status: Status) -> None:
        if new_status not in (ModuleProgress.Status.OPEN, ModuleProgress.Status.IN_PROGRESS):
            raise ValueError("Bestanden oder nicht bestanden ergibt sich aus der Note. Bitte trage eine Note ein.")
        self._grade = None
        self._status = new_status
