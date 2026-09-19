# --- Definition of Class "Module" ---
from dataclasses import dataclass


@dataclass
class Module:
    id: str
    name: str
    ects: int

