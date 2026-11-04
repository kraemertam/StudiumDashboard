import sqlite3
from contextlib import closing
from pathlib import Path

class BaseRepository:
    """Base class for all repositories. Encapsulates the database connection and provides general read and write methods."""

    DB_PATH = Path(__file__).resolve().parent / "databank.db"
    TABLE: str = ""                     
    ID_COLUMN: str = ""

    # --- HELPER METHODS FOR ALL SUBCLASSES ----------------------------------------------------------------------------------------
    def _connect(self) -> sqlite3.Connection:
            """Open a connection to database with foreign keys switch on."""
            connection = sqlite3.connect(self.DB_PATH)
            connection.execute("PRAGMA foreign_keys = ON") 
            return connection

    # --- GENERAL METHODS FOR ALL SUBCLASSES ----------------------------------------------------------------------------------------

    def get_by_id(self, record_id: str) -> tuple | None:
        """Return the row with the given id or None."""
        with closing(self._connect()) as connection:
            cursor = connection.execute(f"SELECT * FROM {self.TABLE} WHERE {self.ID_COLUMN} = ?", (record_id,))
            return cursor.fetchone()

    def get_all(self) -> list[tuple]:
        """Return all rows of the table."""
        with closing(self._connect()) as connection:
            cursor = connection.execute(f"SELECT * FROM {self.TABLE}")
            return cursor.fetchall()

    def exists(self, record_id: str) -> bool:
         """Check whether a row with the given id exists."""
         return self.get_by_id(record_id) is not None
