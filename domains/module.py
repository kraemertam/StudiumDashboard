from dataclasses import dataclass


@dataclass
class Module:
    """A module of a course with id, name and ECTS points."""
    id: str
    name: str
    ects: int

