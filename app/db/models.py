from sqlalchemy import Column, String, Integer, Float, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()


class Candidate(Base):
    __tablename__ = "candidates"

    candidate_id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    parsed_data = Column(JSON)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


class ATSScore(Base):
    __tablename__ = "ats_scores"

    id = Column(Integer, primary_key=True, index=True)
    candidate_id = Column(String, nullable=False)
    job_id = Column(String, nullable=False)
    score = Column(Float)
    model_version = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)


class ScreeningReport(Base):
    __tablename__ = "screening_reports"

    id = Column(Integer, primary_key=True, index=True)
    candidate_id = Column(String)
    report = Column(JSON)
    model_version = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)


class InterviewResult(Base):
    __tablename__ = "interview_results"

    id = Column(Integer, primary_key=True, index=True)
    candidate_id = Column(String)
    transcript = Column(String)
    scores = Column(JSON)
    model_version = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)