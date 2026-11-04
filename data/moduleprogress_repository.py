import sqlite3
from contextlib import closing

from data.base_repository import BaseRepository


class ModuleProgressRepository(BaseRepository):
    """Database access for the progress of a student in his modules. 

    The table has a composite primary key (student_id, module_id).
    Therefore ID_COLUMN stays empty and get_by_id()/exists() are not used here;
    this class only uses the helper method of BaseRepository."""

    TABLE = "moduleprogress"
    
    def create_entries(self, moduleprogress_rows: list[tuple]) -> None:
        """Insert several progress entries at once.
        Expects per row: (student_id, module_id, module_status)"""
        try:
            with closing(self._connect()) as connection:
                with connection:
                    connection.executemany("INSERT INTO moduleprogress (student_id, module_id, module_status) VALUES (?,?,?)", moduleprogress_rows)
        except sqlite3.IntegrityError:
            raise ValueError("Die Modulfortschritte konnten nicht angelegt werden.")

    def get_for_student(self, student_id: str) -> list[tuple]:
        """Return all modules from student including status and grade, sorted by module_id.
        Returns in tuple per module, sorted by module_id: 
        (module_id, module_name, module_ects, module_status, module_grade)
        module_grade is None as long as no grade has been set."""
        with closing(self._connect()) as connection:
            cursor = connection.execute("""
                SELECT m.module_id, m.module_name, m.module_ects, mp.module_status, mp.module_grade 
                FROM moduleprogress mp
                JOIN modules m ON m.module_id = mp.module_id
                WHERE mp.student_id = ?
                ORDER BY m.module_id""", (student_id,))
            return cursor.fetchall()

    def get_grades(self, student_id: str) -> list[float]:
        """Return all grades a student has received so far."""
        with closing(self._connect()) as connection:
            cursor = connection.execute("SELECT module_grade FROM moduleprogress WHERE student_id = ? AND module_grade IS NOT NULL", (student_id, ))
            return [row[0] for row in cursor.fetchall()]

    def save(self, student_id: str, module_id: str, module_status: str, module_grade: float | None) -> None:
        """Save status and grade of one module in one step."""
        with closing(self._connect()) as connection:
            with connection:
                connection.execute(
                    "UPDATE moduleprogress SET module_status = ?, module_grade = ? WHERE student_id = ? AND module_id = ?",
                    (module_status, module_grade, student_id, module_id))
