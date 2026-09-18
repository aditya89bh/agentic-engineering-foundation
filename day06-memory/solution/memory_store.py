from __future__ import annotations

import sqlite3
from datetime import datetime, timezone
from pathlib import Path

from memory_schema import MemoryRecord


class MemoryStore:
    def __init__(self, db_path="memory.db"):
        self.db_path = str(Path(db_path))
        self.connection = sqlite3.connect(self.db_path)
        self.connection.row_factory = sqlite3.Row
        self._create_table()

    def _create_table(self):
        self.connection.execute(
            """
            CREATE TABLE IF NOT EXISTS memories (
                id TEXT PRIMARY KEY,
                type TEXT NOT NULL,
                subject TEXT NOT NULL,
                content TEXT NOT NULL,
                source TEXT NOT NULL,
                confidence REAL NOT NULL,
                created_at TEXT NOT NULL,
                expires_at TEXT
            )
            """
        )
        self.connection.commit()

    def write(self, record: MemoryRecord) -> bool:
        try:
            self.connection.execute(
                """
                INSERT INTO memories
                (id, type, subject, content, source, confidence, created_at, expires_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    record.id,
                    record.type,
                    record.subject,
                    record.content,
                    record.source,
                    record.confidence,
                    record.created_at,
                    record.expires_at,
                ),
            )
            self.connection.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def _row_to_record(self, row):
        return MemoryRecord(
            id=row["id"],
            type=row["type"],
            subject=row["subject"],
            content=row["content"],
            source=row["source"],
            confidence=row["confidence"],
            created_at=row["created_at"],
            expires_at=row["expires_at"],
        )

    def get_by_subject(self, subject: str):
        rows = self.connection.execute(
            "SELECT * FROM memories WHERE subject = ? ORDER BY created_at DESC",
            (subject,),
        ).fetchall()
        return [self._row_to_record(row) for row in rows]

    def search(self, query: str, memory_type: str | None = None, min_confidence: float = 0.0):
        pattern = f"%{query}%"
        params = [pattern, pattern, min_confidence]
        sql = """
            SELECT * FROM memories
            WHERE (content LIKE ? OR subject LIKE ?)
              AND confidence >= ?
        """
        if memory_type:
            sql += " AND type = ?"
            params.append(memory_type)

        sql += " ORDER BY created_at DESC"
        rows = self.connection.execute(sql, params).fetchall()
        return [self._row_to_record(row) for row in rows]

    def is_expired(self, record: MemoryRecord, now: datetime | None = None) -> bool:
        if not record.expires_at:
            return False
        now = now or datetime.now(timezone.utc)
        expiry = datetime.fromisoformat(record.expires_at)
        return expiry <= now

    def delete(self, memory_id: str) -> bool:
        cursor = self.connection.execute(
            "DELETE FROM memories WHERE id = ?",
            (memory_id,),
        )
        self.connection.commit()
        return cursor.rowcount > 0

    def close(self):
        self.connection.close()
