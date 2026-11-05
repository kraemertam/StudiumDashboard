import sqlite3
from contextlib import closing

from data.base_repository import BaseRepository


class CourseRepository(BaseRepository):
    """Database access for courses and the assignment of modules to courses.
    Inherits get_by_id(), get_all() and exists() from BaseRepository."""

    TABLE = "course"
    ID_COLUMN = "course_id"

    def create(self, course_id: str, course_name: str, course_degree: str, course_ects: int) -> None:
        """Insert a new course. Raises ValueError if id already exists."""
        try: 
            with closing(self._connect()) as connection:
                with connection:
                    connection.execute("INSERT INTO course (course_id, course_name, course_degree, course_ects) VALUES (?,?,?,?)", (course_id, course_name, course_degree, course_ects))
        except sqlite3.IntegrityError:
            raise ValueError(f"Der Kurs {course_id}: {course_name} existiert in der Datenbank bereits.")

    def add_module(self, course_id: str, module_id: str) -> None:
        """Add a module to a course."""
        try:
            with closing(self._connect()) as connection:
                with connection:
                    connection.execute("INSERT INTO course_modules (course_id, module_id) VALUES (?,?)", (course_id, module_id))
        except sqlite3.IntegrityError:
            raise ValueError(f"Das Modul {module_id} konnte dem Kurs {course_id} nicht zugeordnet werden.")

    def get_modules(self, course_id: str) -> list[tuple]:
        """All modules of a course, sorted by position.
        Returns per module: (module_id, module_name, module_ects)"""
        with closing(self._connect()) as connection:
            cursor = connection.execute("""
                SELECT m.module_id, m.module_name, m.module_ects
                FROM course_modules cm
                JOIN modules m ON m.module_id = cm.module_id
                WHERE cm.course_id = ?
                ORDER BY cm.position""", (course_id,))
            return cursor.fetchall()