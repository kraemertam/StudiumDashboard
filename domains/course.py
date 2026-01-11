# --- Definition of Class "Course" ---

from dataclasses import dataclass, field

@dataclass
class Course:
    id: str
    name: str
    etc: int
    modules: list[Module] = field(default_factory=list)
    students: list[str] = field(default_factory=list)


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

