import sqlite3
from datetime import datetime

def process_ocr(ocr_text, file_path):
    db_path = r"C:\Users\Vishak\Documents\UiPath\FlowGuardRPA\data\flowguard.db"

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source_file TEXT,
            extracted_text TEXT,
            processed_at TEXT
        )
    """)

    cur.execute("""
        INSERT INTO records (source_file, extracted_text, processed_at)
        VALUES (?, ?, ?)
    """, (file_path, ocr_text[:500], datetime.now().isoformat()))

    conn.commit()
    conn.close()

    return "SUCCESS"
