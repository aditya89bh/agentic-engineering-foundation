import sqlite3
from memory_schema import MemoryRecord


class MemoryStore:
    def __init__(self, db_path="memory.db"):
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path)
        self._create_table()

    def _create_table(self):
        # TODO: create the memories table
        pass

    def write(self, record: MemoryRecord):
        # TODO: prevent duplicate IDs and persist the record
        pass

    def get_by_subject(self, subject: str):
        # TODO: return memories for one subject
        return []

    def search(self, query: str):
        # TODO: perform a simple keyword search over content
        return []

    def close(self):
        self.connection.close()
