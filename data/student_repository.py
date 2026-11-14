import sqlite3
from contextlib import closing

from data.base_repository import BaseRepository


class StudentRepository(BaseRepository):
    """Database access for students. Inherits get_by_id(), get_all() and exists() from BaseRepository."""

    TABLE = "student"
    ID_COLUMNS = ("student_id",)

    def create(self, student_id: str, student_name: str, student_lastname: str) -> None:
        """Insert a new student. Raises ValueError if the id already exists."""
        try:
            with closing(self._connect()) as connection:
                with connection:
                    connection.execute("INSERT INTO student (student_id, student_name, student_lastname) VALUES (?,?,?)", (student_id, student_name, student_lastname))
        except sqlite3.IntegrityError:
            raise ValueError(f"Die Matrikelnummer {student_id} existiert bereits.")

    def enroll(self, student_id: str, course_id: str, gradetarget: float) -> None:
        """Enroll student in course. Raises ValueError if the course does not exist."""
        try:
            with closing(self._connect()) as connection:
                with connection:
                    connection.execute("UPDATE student SET student_course = ?, student_gradetarget = ? WHERE student_id = ?", (course_id, gradetarget, student_id))
        except sqlite3.IntegrityError:
            raise ValueError(f"Der Kurs {course_id} existiert nicht.")
