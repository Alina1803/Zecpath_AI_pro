import psycopg2
import json  # ✅ ADD THIS

def get_connection():
    return psycopg2.connect(
        host="127.0.0.1",  # ✅ better than localhost
        database="zecpath_ai_pro",
        user="postgres",
        password="your_password"
    )


def save_to_db(data):
    conn = get_connection()
    cursor = conn.cursor()

    # ✅ Convert to proper JSON
    topics_json = json.dumps(data.get("detected_topics", []))

    # Insert transcript
    cursor.execute("""
        INSERT INTO ca_transcripts
        (candidate_id, job_id, question_id, domain, full_text, detected_topics, answer_score)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        RETURNING transcript_id
    """, (
        data["metadata"]["candidate_id"],
        data["metadata"]["job_id"],
        data["metadata"]["question_id"],
        "ca",
        data["full_text"],
        topics_json,  # ✅ FIXED
        data.get("answer_score", 0)
    ))

    transcript_id = cursor.fetchone()[0]

    # Insert segments
    for seg in data["segments"]:
        cursor.execute("""
            INSERT INTO ca_transcript_segments
            (transcript_id, speaker, text, timestamp, confidence)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            transcript_id,
            seg["speaker"],
            seg["text"],
            seg["timestamp"],
            seg["confidence"]
        ))

    conn.commit()
    cursor.close()
    conn.close()