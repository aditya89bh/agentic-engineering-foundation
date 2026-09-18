import importlib.util
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path


BASE = Path(__file__).resolve().parents[1] / "solution"


def load(name, file):
    spec = importlib.util.spec_from_file_location(name, BASE / file)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


schema = load("memory_schema", "memory_schema.py")
store_mod = load("memory_store", "memory_store.py")


class MemoryStoreTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
        self.temp.close()
        self.store = store_mod.MemoryStore(self.temp.name)

    def tearDown(self):
        self.store.close()
        Path(self.temp.name).unlink(missing_ok=True)

    def make_record(self, record_id="MEM-001", expires_at=None):
        return schema.MemoryRecord(
            id=record_id,
            type="episodic",
            subject="SUP-017",
            content="missed delivery twice",
            source="supplier_evaluation",
            confidence=1.0,
            created_at=datetime.now(timezone.utc).isoformat(),
            expires_at=expires_at,
        )

    def test_write_and_get_by_subject(self):
        self.assertTrue(self.store.write(self.make_record()))
        records = self.store.get_by_subject("SUP-017")
        self.assertEqual(len(records), 1)

    def test_duplicate_id_rejected(self):
        record = self.make_record()
        self.assertTrue(self.store.write(record))
        self.assertFalse(self.store.write(record))

    def test_search(self):
        self.store.write(self.make_record())
        results = self.store.search("delivery")
        self.assertEqual(len(results), 1)

    def test_confidence_filter(self):
        low = schema.MemoryRecord(
            id="LOW",
            type="semantic",
            subject="SUP-002",
            content="possibly unreliable",
            source="model_inference",
            confidence=0.3,
            created_at=datetime.now(timezone.utc).isoformat(),
        )
        self.store.write(low)
        self.assertEqual(self.store.search("unreliable", min_confidence=0.5), [])

    def test_expiry(self):
        expiry = (datetime.now(timezone.utc) - timedelta(days=1)).isoformat()
        record = self.make_record(expires_at=expiry)
        self.assertTrue(self.store.is_expired(record))


if __name__ == "__main__":
    unittest.main()
