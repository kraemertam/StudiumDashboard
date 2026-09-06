# --- Definition of Class "Module" ---
from dataclasses import dataclass


@dataclass
class Module:
    id: str
    name: str
    etc: int

