from __future__ import annotations

import os
import tempfile
from datetime import datetime, timezone

from memory_policy import should_retrieve, should_write
from memory_schema import MemoryRecord
from memory_store import MemoryStore


def build_memory_context(store: MemoryStore, supplier_id: str):
    records = store.get_by_subject(supplier_id)
    return [
        record.as_dict()
        for record in records
        if should_retrieve(record, subject=supplier_id)
    ]


def remember_rejection(store: MemoryStore, supplier_id: str, reason: str):
    record = MemoryRecord(
        id=f"decision-{supplier_id}",
        type="decision",
        subject=supplier_id,
        content=f"Rejected supplier: {reason}",
        source="supplier_evaluation",
        confidence=1.0,
        created_at=datetime.now(timezone.utc).isoformat(),
    )

    if should_write(record):
        return store.write(record)
    return False


def main():
    db_path = os.path.join(tempfile.gettempdir(), "day06_supplier_memory.db")
    store = MemoryStore(db_path)

    remember_rejection(store, "SUP-017", "repeated delivery delays")

    context = build_memory_context(store, "SUP-017")

    print("Retrieved memory context:")
    for record in context:
        print(f"  {record}")

    print("\nDecision:")
    if any("Rejected supplier" in item["content"] for item in context):
        print("  Avoid recommending SUP-017 unless new verified evidence justifies reconsideration.")
    else:
        print("  No relevant prior rejection found.")

    store.close()


if __name__ == "__main__":
    main()
