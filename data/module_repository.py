import sqlite3
from contextlib import closing

from data.base_repository import BaseRepository


class ModuleRepository(BaseRepository):
    """Database access for modules. Inherits get_by_id(), get_all() and exists() from BaseRepository."""

    TABLE = "modules"
    ID_COLUMNS = ("module_id",)

    def create(self, module_id: str, module_name: str, module_ects: int) -> None:
        """Insert a new module. Raises ValueError if id already exists."""
        try:
            with closing (self._connect()) as connection:
                with connection:
                    connection.execute("INSERT INTO modules (module_id, module_name, module_ects) VALUES (?,?,?)", (module_id, module_name, module_ects))
        except sqlite3.IntegrityError:
            raise ValueError(f"Das Modul mit der ID {module_id} existiert bereits unter dem Namen {module_name}.")

