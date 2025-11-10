# Hier werden die Klassen definiert: Student, Course, Modul
from dataclasses import dataclass, field

from data.enroll_course_db import enroll_course
from data.save_changes_db import save_modules_changes


@dataclass
class Module:
    id: str
    name: str
    etc: int
    status: str = field(default="open", init=True)
    grade: int = field(default=None, init=True)

    def change_status(self, student_id):
        print(self.status)
        if self.status == "offen":
            self.status = "in progress"
        elif self.status == "in progress":
            self.status = "done"
        save_modules_changes(student_id, self.id, self.status)
        print("Modulstatus geändert.")

    def set_grade(self, grade):
        self.grade = grade

    #@staticmethod #nochmal checken: Doch eher classmethod?
    #def create(name: str, etc: int, id = str):
        #if id not in Datenbank:
           # return Module(id=id, name=name, etc=etc)
           # Speicherung des Moduls in Datenbank??
        #else:
           # print("Modul bereits vorhanden")


    #def __delete__(self, instance):
        #print(f"Das Modul {instance} wurde gelöscht.")
        #pass




@dataclass
class Course:
    id: str
    name: str
    etc: int
    students: list[str] = field(default_factory=list)
    modules: list[Module] = field(default_factory=list)

    def add_module(self, module: Module):
        self.modules.append(module)

    def remove_module(self, module: Module):
        self.modules.remove(module)

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def return_modules(self):
        return self.modules

    def return_etc(self):
        return self.etc


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

    def moduls_per_semesters(self) -> int:
        modules_per_semster = self.etcs / self.semester
        return modules_per_semster

    def change_modul_status(self, module_id):
        pass


