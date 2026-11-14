import sqlite3
from contextlib import closing
from pathlib import Path

class BaseRepository:
    """Base class for all repositories. Encapsulates the database connection and provides general read and write methods."""

    DB_PATH = Path(__file__).resolve().parent / "databank.db"
    TABLE: str = ""                     
    ID_COLUMNS: tuple[str, ...] = ()

    # --- HELPER METHODS FOR ALL SUBCLASSES ----------------------------------------------------------------------------------------
    def _connect(self) -> sqlite3.Connection:
            """Open a connection to database with foreign keys switch on."""
            connection = sqlite3.connect(self.DB_PATH)
            connection.execute("PRAGMA foreign_keys = ON") 
            return connection

    # --- GENERAL METHODS FOR ALL SUBCLASSES ----------------------------------------------------------------------------------------

    def get_by_id(self, *record_id: str) -> tuple | None:
        """Return the row with the given key or None. Expects one value per key column."""
        if len(record_id) != len(self.ID_COLUMNS):
            raise ValueError(f"{self.TABLE} erwartet {len(self.ID_COLUMNS)} Schlüsselwert(e).")
        condition = " AND ".join(f"{column} = ?" for column in self.ID_COLUMNS)
        with closing(self._connect()) as connection:
            cursor = connection.execute(f"SELECT * FROM {self.TABLE} WHERE {condition}", record_id)
            return cursor.fetchone()

    def get_all(self) -> list[tuple]:
        """Return all rows of the table."""
        with closing(self._connect()) as connection:
            cursor = connection.execute(f"SELECT * FROM {self.TABLE}")
            return cursor.fetchall()

    def exists(self, *record_id: str) -> bool:
         """Check whether a row with the given key exists."""
         return self.get_by_id(*record_id) is not None
