import sqlite3

def init_db():
    conn = sqlite3.connect("data/transcripts/transcript_db.sqlite")
    cursor = conn.cursor()

    with open("app/services/transcript_engine_23/db_schema.sql", "r") as f:
        cursor.executescript(f.read())

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()