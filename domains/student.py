import re
from dataclasses import dataclass
from domains.course import Course


@dataclass
class Student:
    """A student with matriculation number, name, enrolled course and grade target."""
    id: str
    name: str
    lastname: str
    course: Course | None = None
    gradetarget: float | None = None

    def __post_init__(self):
        self._validate_id()
    
    def _validate_id(self) -> None:
        """Check that the matriculation number matches the expected format."""
        pattern = r"^IU\d{3,12}$"
        if not re.match(pattern, self.id):
            raise ValueError("Ungültige Matrikelnummer! Eine gültige Matrikelnummer startet mit \"IU\", gefolgt von 3 - 12 Ziffern, z.B. \"IU123456\"")

    def enroll_student_in_course(self, course: Course, gradetarget: float):
        """Enroll the student in a course. Raises ValueError if already enrolled or the grade target is invalid."""
        if self.course is not None:
            raise ValueError(f"{self.name} {self.lastname} ist bereits in einem Kurs eingeschrieben.")
        gradetarget = float(gradetarget)
        if not (1.0 <= gradetarget <= 4.0):
            raise ValueError("Das Notenziel muss zwischen 1.0 und 4.0 liegen.")
        self.course = course
        self.gradetarget = gradetarget
