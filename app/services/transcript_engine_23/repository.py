import sqlite3
import json

DB_PATH = "data/transcripts/transcript_db.sqlite"


def save_to_db(data):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    metadata = data["metadata"]

    cursor.execute("""
        INSERT INTO ca_transcripts (
            candidate_id,
            job_id,
            question_id,
            domain,
            full_text,
            detected_topics,
            answer_score,
            compliance_accuracy
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        metadata["candidate_id"],
        metadata["job_id"],
        metadata["question_id"],
        metadata.get("domain", "chartered_accountant"),
        data.get("full_text", ""),
        json.dumps(data.get("detected_topics", [])),
        data.get("answer_score", 0),
        data.get("compliance_accuracy", 0)
    ))

    conn.commit()
    conn.close()