# --- Definition of Class "Student" ---
from dataclasses import dataclass, field
import math
from data.enroll_course_db import enroll_course

@ dataclass
class Student:
    id: str
    name: str
    lastname: str
    course_id: str = field(default=False)
    course_name: str = field(default=False)
    etcs: int = field(default=False)
    semester: int = field(default=False)
    modules: list[list] = field(default_factory=list)

    def info_student(self):
        return f"{self.name} {self.lastname} studiert {self.course}"

    def enroll_course(self, course_id, semester):
        self.course = course_id
        self.semester = int(semester)
        enroll_course(self.id, self.course, self.semester)

    def calc_etc_per_semesters(self) -> int:
        etc_per_semester = self.etcs / self.semester
        if etc_per_semester % 5 !=0:
            round_up = math.ceil(etc_per_semester / 5) * 5
            return round_up
        else:
            return etc_per_semester


    def change_modul_status(self, module_id):
        pass


