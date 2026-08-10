# --- Definition of Class "Module" ---
from dataclasses import dataclass, field
from data.student import save_modules_changes, save_grade_changes


@dataclass
class Module:
    id: str
    name: str
    etc: int
    status: str = field(default="open", init=True)
    grade: int = field(default=None, init=True)

    def change_status(self, student_id, new_status):
        self.status = new_status
        save_modules_changes(student_id, self.id, self.status)
        print(f"Modulstatus {self.name} in {self.status} geändert.")
        return self.status

    def set_grade(self, student_id, grade):
        self.grade = grade
        save_grade_changes(student_id, self.id, self.grade)
        if self.grade > 4:
            self.status = "nicht bestanden"
        else:
            self.status = "abgeschlossen"
        save_modules_changes(student_id, self.id, self.status)
        print(f"Note {self.grade} für {self.name} wurde eingetragen.")



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