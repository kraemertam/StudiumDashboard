# --- Definition of Class "Course" ---

import re
from dataclasses import dataclass, field
from domains.module import Module

@dataclass
class Course:
    id: str
    name: str
    title: str
    etc: int
    modules: list[Module] = field(default_factory=list)

    def __post_init__(self):
        self._validate_id()
        self._validate_etc()

    def _validate_id(self) -> None:
        pattern = r"^[A-Za-z]{2}-[A-Za-z]{1,6}-{0,1}\d{0,4}$"
        if not re.match(pattern, self.id):
            raise ValueError(f"Ungültige Kurs-ID {self.id}. Erwartetes Format, wie z.B. \"FS-BAAKI-01\"")

    def _validate_etc(self) -> None:
        if self.title.startswith("Bachelor"):
            if not (180 <= self.etc <= 240):
                raise ValueError("Die ETCS für einen Bachelorabschluss müssen zwischen 180 - 240 liegen.")
        elif self.title.startswith("Master"):
            if not (60 <= self.etc <= 120):
                raise ValueError("Die ETCS für einen Masterabschluss müssen zwischen 60 - 120 liegen.")

    def current_etc(self) -> int:
        """Calculate the sum of ETCS of all modules currently assigned to this course."""
        return sum(modules.etc for modules in self.modules)

    def remaining_etc(self) -> int:
        """Calculate how many ETCS are still available before the planned ETC of this Course are reached."""
        remaining_etc = self.etc - self.current_etc()
        return remaining_etc

    def add_module(self, module: Module):
        if any(m.id == module.id for m in self.modules):
            raise ValueError(f"Modul {module.name} ist bereits im Kurs {self.name} enthalten.")
        if module.etc > self.remaining_etc():
            raise ValueError (f"Das Modul {module.name} mit {module.etc} passt nicht mehr in den Kurs {self.name}. Es sind lediglich {self.remaining_etc()} ETC übrig.")
        print(f"Module {module.name} wurde {self.name} hinzugefügt.")
        self.modules.append(module)

    def remove_module(self, module: Module):
        self.modules.remove(module)

    def return_modules(self):
        return self.modules

    def return_etc(self):
        return self.etc

