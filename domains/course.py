import re
from dataclasses import dataclass, field
from domains.module import Module


@dataclass
class Course:
    id: str
    name: str
    degree: str
    ects: int
    modules: list[Module] = field(default_factory=list)

    def __post_init__(self):
        self._validate_id()
        self._validate_ects()

    def _validate_id(self) -> None:
        pattern = r"^[A-Za-z]{2}-[A-Za-z]{1,6}-{0,1}\d{0,4}$"
        if not re.match(pattern, self.id):
            raise ValueError(f"Ungültige Kurs-ID {self.id}. Erwartetes Format, wie z.B. \"FS-BAAKI-01\"")

    def _validate_ects(self) -> None:
        if self.degree.startswith("Bachelor"):
            if not (180 <= self.ects <= 240):
                raise ValueError("Die ECTS-Punkte für einen Bachelorabschluss müssen zwischen 180 - 240 liegen.")
        elif self.degree.startswith("Master"):
            if not (60 <= self.ects <= 120):
                raise ValueError("Die ECTS-Punkte für einen Masterabschluss müssen zwischen 60 - 120 liegen.")

    def current_ects(self) -> int:
        """Calculate the sum of ECTS-Points of all modules currently assigned to this course."""
        return sum(modules.ects for modules in self.modules)

    def remaining_ects(self) -> int:
        """Calculate how many ECTS-Points are still available before the planned ECTS-Points of this Course are reached."""
        remaining_ects = self.ects - self.current_ects()
        return remaining_ects

    def add_module(self, module: Module) -> None:
        if any(m.id == module.id for m in self.modules):
            raise ValueError(f"Modul {module.name} ist bereits im Kurs {self.name} enthalten.")
        if module.ects > self.remaining_ects():
            raise ValueError (f"Das Modul {module.name} mit {module.ects} passt nicht mehr in den Kurs {self.name}. Es sind lediglich {self.remaining_ects()} ECTS-Punkte übrig.")
        print(f"Module {module.name} wurde {self.name} hinzugefügt.")
        self.modules.append(module)

    def remove_module(self, module: Module) -> None:
        self.modules.remove(module)

    def return_modules(self) -> list[Module]:
        return self.modules

    def return_ects(self) -> int:
        return self.ects

