CREATE TABLE IF NOT EXISTS ca_transcripts (
    transcript_id INTEGER PRIMARY KEY AUTOINCREMENT,
    candidate_id VARCHAR(50),
    job_id VARCHAR(50),
    question_id VARCHAR(50),
    domain VARCHAR(50),
    full_text TEXT,
    detected_topics TEXT,
    answer_score DECIMAL(5,2),
    compliance_accuracy DECIMAL(5,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ca_transcript_segments (
    segment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    transcript_id INT,
    speaker VARCHAR(20),
    text TEXT,
    timestamp FLOAT,
    confidence FLOAT,
    finance_skill_tags TEXT,
    FOREIGN KEY (transcript_id) REFERENCES ca_transcripts(transcript_id)
);