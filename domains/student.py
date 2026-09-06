# --- Definition of Class "Student" ---
from dataclasses import dataclass, field
import math, re

@dataclass
class Student:
    id: str
    name: str
    lastname: str
    course_id: str = field(default=False)
    gradetarget: float = field(default=False)

    def __post_init__(self):
        self._validate_id()
    
    def _validate_id(self) -> None:
        pattern = r"^IU\d{3,12}$"
        if not re.match(pattern, self.id):
            raise ValueError("Ungültige Materikelnummer! Eine gültige Matrikelnummer startet mit \"IU\", gefolgt von 3 - 12 Ziffern, z.B. \"IU123456\"")

    def info_student(self):
        return f"Name: {self.name} {self.lastname}, Matrikelnummer: {self.id}, Kurs: {self.course_id}, Notenziel: {self.gradetarget}"

    def enroll_course(self, course_id, gradetarget):
        if self.course_id:
            raise ValueError(f"{self.name} {self.lastname} ist bereits in einem Kurs eingeschrieben.")
        gradetarget = float(gradetarget)
        if not (1.0 <= gradetarget <= 4.0):
            raise ValueError("Das Ziel-Notendurchschnitt muss zwischen 1.0 und 4.0 liegen.")
        self.course_id = course_id
        self.gradetarget =gradetarget
