from sqlalchemy import Column, Integer, String, Text, Float, JSON, TIMESTAMP
from datetime import datetime
from app.db.connection import Base


class CATranscript(Base):
    __tablename__ = "ca_transcripts"

    transcript_id = Column(Integer, primary_key=True, index=True)
    candidate_id = Column(String(50))
    job_id = Column(String(50))
    question_id = Column(String(50))
    domain = Column(String(50), default="ca")
    full_text = Column(Text)
    detected_topics = Column(JSON)
    answer_score = Column(Float)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)


class CATranscriptSegment(Base):
    __tablename__ = "ca_transcript_segments"

    segment_id = Column(Integer, primary_key=True, index=True)
    transcript_id = Column(Integer)
    speaker = Column(String(20))
    text = Column(Text)
    timestamp = Column(Float)
    confidence = Column(Float)