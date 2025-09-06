import sqlite3
import datetime

def create_database_and_table(db_name="logs.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS raw_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            log_entry TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_log_entry(db_name, timestamp, log_entry):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO raw_logs (timestamp, log_entry) VALUES (?, ?)", (timestamp, log_entry))
    conn.commit()
    conn.close()

def ingest_logs_from_file(filepath, db_name="logs.db"):
    create_database_and_table(db_name)
    try:
        with open(filepath, 'r') as f:
            for line in f:
                log_entry = line.strip()
                timestamp = datetime.datetime.now().isoformat() # Using current time for simplicity
                insert_log_entry(db_name, timestamp, log_entry)
                yield log_entry
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return

if __name__ == "__main__":
    log_file = "access.log"
    db_name = "logs.db"
    
    print(f"Ingesting logs from {log_file} and storing in {db_name}...")
    for log_entry in ingest_logs_from_file(log_file, db_name):
        # For now, just print to confirm ingestion
        print(f"Ingested: {log_entry[:70]}...")
