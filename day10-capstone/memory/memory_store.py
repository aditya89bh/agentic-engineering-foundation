import sqlite3


class MemoryStore:
    def __init__(self, path=":memory:"):
        self.conn = sqlite3.connect(path)
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS memories (
                subject TEXT,
                type TEXT,
                content TEXT,
                source TEXT
            )
            """
        )

    def write(self, subject, memory_type, content, source):
        self.conn.execute(
            "INSERT INTO memories VALUES (?, ?, ?, ?)",
            (subject, memory_type, content, source),
        )
        self.conn.commit()

    def get(self, subject):
        rows = self.conn.execute(
            "SELECT subject, type, content, source FROM memories WHERE subject = ?",
            (subject,),
        ).fetchall()
        return [
            {"subject": r[0], "type": r[1], "content": r[2], "source": r[3]}
            for r in rows
        ]
