ATS SYSTEM DOCUMENTATION 

1. Project Overview

The Applicant Tracking System (ATS) is an AI-powered system designed to automate resume screening by evaluating candidate profiles against job descriptions (JD).

It analyzes resumes, extracts key features, computes matching scores, and ranks candidates to assist recruiters in faster and more accurate decision-making.

Objectives:

Automate resume screening process

Improve hiring efficiency and speed

Ensure consistent and explainable scoring

Support bulk resume processing (scalability)

2. ATS System Architecture

HIGH-LEVEL ARCHITECTURE 

Workflow Pipeline

User Input   (Upload Resume)
   ↓
FastAPI API
   ↓
File Upload Module
   ↓
Resume Parser → JD Parser
   ↓
Feature Extraction (Skills, Experience, Education)
   ↓
Matching Engine (Skill Matching  , Domain Matching  , Semantic Similarity )
   ↓
Scoring Engine  (Skill (30%) ,Experience (25%) ,Education (20%) , Semantic (25%)  )
   ↓
Ranking & Output

 Core Modules

API Layer (FastAPI) – Handles requests and responses
Parsing Layer – Extracts structured data from resumes and JDs
Feature Extraction Layer – Identifies skills, experience, education
Matching Engine – Compares resume with JD
Scoring Engine – Calculates ATS score
Optimization Layer – Improves performance using caching

3. High-Level System Compnents

Component
	Folder
	Responsibility

Data Storage
	data/
	Stores raw, processed, and intermediate datasets
API Layer
	api/
	Exposes endpoints for ATS operations
Business Logic	services/
	Core processing and scoring logic
Data Validation
	schemas/
	Ensures request/response structure
Parsing Layer
	parsers/
	Extracts structured data from resumes & JDs
Document Readers
	readers/
	Reads PDF, DOCX, and other formats

ATS Engine	ranking-engine14/
ats-engine13/	Controls scoring, ranking, and orchestration

Semantic Matching
	Semantic_engine12/
JD_Parser/	Computes similarity between resume & JD

Screening AI
	screening_ai/
	Initial filtering of candidates

Interview AI
	interview_ai/
	Advanced candidate evaluation

Scoring Logic
	Ats-engine13/
	Calculates ATS scores

Utilities	utils/
	Logging, preprocessing, helpers

Testing
	tests/
	Unit and integration testing






 4. Detailed Task Breakdown

 Task 1 – Project Setup

Initialized FastAPI project
Created modular folder structure
Setup virtual environment

Structured folders:

app/
  ├── api/
  ├── services/
  ├── parsers/
  ├── models/



Task 2 – File Upload System

Implemented /process endpoint

Supported formats:

PDF

DOCX


Used UploadFile in FastAPI




Task 3 – File Handling

Stored uploaded files in /uploads

Applied:

a.Unique filenames (UUID/timestamp)

b.Safe file handling



Task 4 – Resume Parsing

Extracted:

Raw text

Structured sections


Libraries used:

PDF parsers

DOCX readers



Task 5 – JD Parsing

Extracted structured fields:

Role

Skills

Responsibilities

Qualifications



Task 6 – Skill Extraction

Extracted:

Technical skills

Soft skills


Used keyword matching + NLP techniques





Task 7 – Experience Extraction

Extracted:

Total years

Role-based experience


Normalized formats (e.g., “2+ years”, “3 yrs”)



Task 8 – Education Extraction

Extracted:

Degree

Institution

Year


Standardized naming (B.Tech → Bachelor of Technology)




Task 9 – Skill Matching Engine

Compared:

Resume skills vs JD skills


Output:

Matched skills

Match percentage




Task 10 – Domain Skill Matching

Used predefined domain database

Example:

Data Science → Python, ML, NLP


Improved contextual relevance



Task 11 – Experience Scoring

Compared:

Candidate experience vs required experience


Logic:

Below range → Low score

Within range → High score

Above range → Moderate normalization




Task 12 – Education Scoring

Compared candidate qualification with JD requirements

Scoring based on:

Degree match

Field relevance




Task 13 – ATS Scoring Engine

Final Formula:

Skill Score → 30%

Experience Score → 25%

Education Score → 20%

Semantic Score → 25%




Task 14 – Semantic Matching

Used NLP similarity techniques

Compared:

Resume text vs JD text


Captures meaning beyond keywords




Task 15 – Batch Processing

Endpoint: /process-batch

Features:

Process multiple resumes

Rank candidates

Return sorted results




Task 16 – Performance Optimization

Implemented:

Caching (JD + Resume processing)

Reduced redundant parsing

Optimized loops and data structures




Task 17 – Error Handling

Handled:

Type mismatches (int vs list)

Missing fields

Empty inputs


Example Fix:

'>=' not supported between int and list
→ Convert all experience values to numeric before comparison




Task 18 – Final Integration

Connected all modules into one pipeline:

Upload → Parse → Extract → Match → Score → Output

Ensured smooth API flow




5. ATS Scoring Formula

The final score is calculated as:

Skill Match = 30%

Experience Match = 25%

Education Match = 20%

Semantic Similarity = 25%


 Interpretation:

80–100 → Strong Match

60–79 → Moderate Match

Below 60 → Weak Match


 6. API Documentation

 Endpoints

 1. /process

Method: POST

Input:

Resume file

JD text


Output:

Score

Breakdown



 2. /process-batch

Method: POST

Input:

Multiple resumes

JD text


Output:

Ranked candidates



7. System Testing

Tested:

Different resume formats

Missing data scenarios

Edge cases


Validated scoring accuracy



8. Fairness & Bias Reduction (Day 15)

Avoided:

Gender bias

Name-based bias


Focused only on:

Skills

Experience

Education




 9. Performance & Optimization

Reduced response time

Used caching layers

Efficient parsing strategies


10. Troubleshooting Guide

Issue                            Cause	                        Fix

int vs list error	            Data type mismatch	            Normalize values
Empty JSON	                Parsing failure          	Validate input
Slow API	               Repeated parsing       	Use caching

 11. Developer Guide

 Run Server

uvicorn main:app --reload

 API Docs

http://127.0.0.1:8000/docs


---

 Folder Structure

app/
 ├── api/
 ├── services/
 │    ├── scoring.py
 │    ├── optimization/
 │    ├── matching/
 ├── parsers/
 ├── models/
 ├── utils/


---

 12. Knowledge Transfer Summary

 Key Learnings

End-to-end ATS pipeline design

NLP-based resume analysis

API development using FastAPI

Scoring system design

Optimization techniques


 How to Extend System

Add ML-based ranking

Integrate database (PostgreSQL)

Add recruiter dashboard

Improve semantic models



 13. Conclusion

The ATS system is:

✔ Scalable

✔ Modular

✔ Explainable

✔ Production-ready


It successfully automates resume screening and provides structured insights for recruitment decisions.

__________________________________________________________________________________________________________