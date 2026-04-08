DAY-1 Zecpath Product & AI Overview
🎯 Objective
The goal of this assignment is to develop a complete understanding of the Zecpath platform, its vision, and how Artificial Intelligence (AI) powers each stage of the hiring lifecycle.
🔄 Hiring Lifecycle Overview
The Zecpath platform automates the end-to-end recruitment process using AI-driven modules:

Job Posting 
   ↓
Resume Submission 
   ↓
AI Resume Parsing 
   ↓
AI ATS Screening 
   ↓
AI Voice Screening 
   ↓
HR Interview AI 
   ↓
Technical Interview AI 
   ↓
Machine Test AI 
   ↓
Behavioral & Culture Fit Analysis 
   ↓
Final Decision AI 
   ↓
Offer Automation

AI Modules & Responsibilities
1. Resume Parser AI
Extracts structured data from resumes (skills, experience, education)
Handles multiple formats (PDF, DOCX)
Normalizes candidate data

2. ATS Scoring Engine
Matches candidate profiles with job descriptions
Calculates relevance scores
Ranks candidates automatically

3. Screening AI (Voice/Chat)
Conducts initial screening interviews
Evaluates communication and basic qualifications
Filters unqualified candidates early

4. HR Interview AI
Simulates HR interviews
Assesses soft skills and communication
Generates candidate summaries

5. Technical Interview AI
Evaluates domain-specific knowledge
Adapts questions dynamically
Scores technical competency

6. Machine Test AI
Assigns coding or task-based assessments
Auto-evaluates submissions
Detects plagiarism or cheating

7. Behavioral AI
Analyzes personality traits
Predicts culture fit
Uses response patterns and sentiment analysis

8. Decision AI
Aggregates scores from all stages
Applies hiring rules and thresholds
Generates final recommendations

9. Offer Automation AI
Generates offer letters
Automates communication workflows
Integrates with HR systems


Day 2 – AI System Architecture

Objective
Design a scalable AI microservices architecture for Zecpath and define how AI systems interact with backend services, frontend applications, and storage layers.
🧱 High-Level Architecture
Zecpath follows a microservices-based AI architecture, where each AI capability is isolated, scalable, and independently deployable.

AI Microservices Breakdown
1. ATS AI Service
Purpose: Resume parsing & candidate-job matching
Input from Backend:
Resume (PDF/DOCX)
Job Description
Candidate metadata
Processing:
Resume parsing (NER, NLP)
Skill extraction
Semantic matching
Score calculation
Output to Backend:
Structured resume JSON
ATS score
Skill match breakdown
2. Screening AI Service
Purpose: Initial candidate screening (voice/chat)
Input:
Candidate profile
Screening questions
Audio/text responses
Processing:
Speech-to-text (if voice)
NLP evaluation
Communication scoring
Output:
Screening score
Transcript
Pass/Fail decision
3. Interview Intelligence Service
Purpose: Conduct HR & technical interviews
Input:
Candidate data
Interview type (HR/Technical)
Question bank
Processing:
Dynamic question generation
Answer evaluation
Context tracking
Output:
Interview score
Answer analysis
Strengths & weaknesses
4. Behavior Analysis Service
Purpose: Personality & culture fit analysis
Input:
Candidate responses
Voice/text signals
Processing:
Sentiment analysis
Tone & emotion detection
Behavioral modeling
Output:
Personality traits
Culture fit score
Risk indicators
5. Decision & Scoring Service
Purpose: Final hiring recommendation
Input:
Scores from all AI services
Hiring rules/config
Processing:
Weighted scoring
Rule-based + ML decisioning
Output:
Final score
Hire / Reject / Hold decision
Confidence level


Frontend
   ↓
Backend API
   ↓
AI Service (via REST / Queue)
   ↓
Processing Layer (ML Models)
   ↓
Storage Layer
   ↓
Backend (via Webhook/Response)
   ↓
Frontend 

Storage Components:
Relational DB → Candidate & job data
Object Storage → Resumes, audio files
Vector DB → Embeddings for semantic search
Model Registry → Versioned AI models
Logs & Monitoring → Observability

Deliverables Summary
✔ AI System Architecture Diagram
✔ Data Flow Diagram (Backend ↔ AI ↔ Storage)
✔ Input/Output Specifications for all AI services

DAY-3 Zecpath AI System – Environment & Repository Setup

🎯 Objective

Establish a professional AI development environment and scalable project structure for building Zecpath’s AI-powered hiring system.

⚙️ Environment Setup

1. Install Python

Ensure Python 3.9+ is installed:

python --version

2. Create Virtual Environment

python -m venv .venv

3. Activate Environment

.venv\Scripts\activate\ps1

4. Install Required Libraries

pip install -r requirements

Project Structure

zecpath-ai/
│
├── data/
│   ├── raw/              # Input files (resumes, job descriptions)
│   ├── processed/        # Output JSON/results
│   └── logs/             # Application logs
│
├── app/
│   ├── parsers/          # Resume parsing modules
│   ├── ats_engine/       # ATS scoring logic
│   ├── screening_ai/     # Screening AI services
│   ├── interview_ai/     # Interview AI modules
│   ├── scoring/          # Decision & scoring engine
│   ├── utils/            # Helper utilities (logging, cleaning, loaders)
│   └── __init__.py
│
├── tests/                # Unit & integration tests
│
├── scripts/              # Pipeline execution scripts
│
├── requirements.txt
├── README.md
└── .gitignor

Module Overview

parsers/ → Extract structured data from resumes (education, skills, certifications)

ats_engine/ → Match candidates with job descriptions and generate scores

screening_ai/ → Conduct initial candidate screening logic

interview_ai/ → Handle HR and technical interview workflows

scoring/ → Aggregate results and generate final decisions

utils/ → Common utilities like logging, file handling, and preprocessing

# Day 4: Data Understanding & Structuring

## 🎯 Objective
To deeply understand hiring data and convert unstructured content (resumes and job descriptions) into structuredAI-ready JSON forma. This enables better matching algorithms, automated screening, and structured data analysis.
## 🏗️ Data Entity Definitions
To ensure consistency across the AI model, we have defined four standard data entities:
| Entity | Description |
|---|---|
Candidate Profile| The root entity representing an individual's professional identity and contact info. |
Job Profile| The root entity representing a specific job opening and its requirements. |
Skill Object| A granular unit containing the skill name, proficiency level, and years of usage. |
Experience Object| A structured block for work history including title, company, duration, and key impact. |
## 📄 JSON Schema Designs
### 1. Resume Structured Schema
This schema transforms a standard resume into a machine-readable format.
```json
{
  "candidate_profile": {
    "personal_info": {
      "full_name": "string",
      "email": "string",
      "phone": "string",
      "location": { "city": "string", "country": "string" }
    },
    "education": [
      {
        "institution": "string",
        "degree": "string",
        "field_of_study": "string",
        "completion_year": "integer"
      }
    ],
    "experience": [
      {
        "job_title": "string",
        "company": "string",
        "start_date": "ISO8601",
        "end_date": "ISO8601/null",
        "responsibilities": ["string"],
        "achievements": ["string"]
      }
    ],
    "skills": [
      {
        "name": "string",
        "level": "Beginner/Intermediate/Expert",
        "years_of_experience": "float"
      }
    ],
    "certifications": ["string"]
  }
}

```
### 2. Job Description (JD) Schema
Designed to capture the core requirements and metadata of a vacancy.
```json
{
  "job_profile": {
    "metadata": {
      "job_id": "string",
      "title": "string",
      "department": "string",
      "work_type": "Remote/Hybrid/On-site"
    },
    "requirements": {
      "minimum_education": "string",
      "required_skills": [
        { "name": "string", "is_mandatory": "boolean" }
      ],
      "preferred_skills": ["string"],
      "min_experience_years": "integer"
    },
    "compensation": {
      "currency": "string",
      "range": { "min": "number", "max": "number" }
    }
  }
}

```
## 🛠️ Tasks Performed
 Domain Analysis:Analyzed 10+ resumes across Engineering, Marketing, and Sales.
 Pattern Recognition:Identified common structures in education (GPA, degree types) and experience (reverse-chronological vs. functional).
 Entity Mapping:Standardized "Designations" to prevent confusion between titles like "Software Engineer" and "SDE-1".
## 📁 Deliverables
 1. Resume Structured Schema(See resume_schema.json)
 2. Job Description Schema:(See jd_schema.json)
 3. AI Data Entity Design Document:Detailed breakdown of attribute logic.

 
# Day 5: Resume Text Extraction Engine
## 🎯 Objective
To build the core processing engine capable of converting unstructured resume files (PDF, DOCX) into clean, normalized text that can be used as high-quality input for AI models.
## 🛠️ Key Features & Tasks
### 1. Multi-Format Support
 PDF Reading:Implementing libraries (e.g., PyPDF2, pdfminer, or fitz) to handle complex PDF layers.
 DOCX Reading:Extracting XML-based text from Word documents using python-docx.
### 2. Data Pipeline & Cleaning
 Raw Extraction:Reliable retrieval of text while maintaining logical flow.
 Noise Reduction:Removing unwanted symbols, non-ASCII characters, and formatting artifacts.
 Normalizatio
   * StandardizinCapitalization(e.g., proper casing for names and titles).
   * CleaninBullet Pointsand special list characters.
   * MappinSection Headings(e.g., "Professional Experience" vs "Work History").
### 3. Structural Handling
 * Processing complex layouts includintablmulti-column forma, and basiOCRfor text embedded in images.
## 📂 Deliverables
| Deliverable | Description |
|---|---|
Extraction Engine| The Python/Node.js script or module that handles file uploads and text retrieval. 
Cleaned Outputs| A collection of .txt or .json files demonstrating the "before and after" of the cleaning process. 
Test Logs| Automated test run results showing successful extraction rates across different layouts. 

# Day 6: Job Description Parsing System

## 🎯 Objective
To build a system that converts unstructured employer job descriptions (JDs) into structured, AI-readable job requirement objects. This allows for automated matching against the candidate profiles built in previous days.
## 🛠️ Key Features & Tasks
### 1. Information Extraction
The system identifies and pulls specific data points from raw JD text:
 * Role Names: Standardizing titles (e.g., "Sr. Backend Engineer" vs "Backend Developer II").
 * Required Skills: Differentiating between "Must-have" (Hard skills) and "Nice-to-have" (Soft skills).
 * Experience Requirements: Extracting year ranges (e.g., "3-5 years") and seniority levels.
 * Education Preferences: Identifying degree levels (B.Tech, MS, PhD) and specific fields of study.
### 2. Intelligent Normalization
 * JD Text Cleaning: Removing boiler-plate "About the Company" text to focus on core requirements.
 * Synonym Detection: Mapping variations to a single standard (e.g., "Node.js", "NodeJS", and "Node" all map to node_js).
 * Role Variation Mapping: Understanding that "SDE-1" and "Junior Software Engineer" represent the same professional level.
### 3. Object Construction
 * Building a hierarchical Job Requirement Object structure.
 * Preparing AI-friendly JD Profiles optimized for vector embeddings or keyword matching algorithms.
## 📂 Deliverables
| Deliverable | Description |
|---|---|
| JD Parser Module | The Python/Node.js script that processes raw JD text into JSON. |
| Structured JD Samples | A collection of JSON files representing various industries (Tech, Finance, Healthcare). |
| Parsing Documentation | Technical notes on the logic used for synonym detection and entity extraction. |
## 🏗️ Structured Output Example
The parser converts raw text into an organized format like this:
```json
{
  "job_metadata": {
    "role": "Data Scientist",
    "seniority": "Mid-Level"
  },
  "requirements": {
    "mandatory_skills": ["Python", "SQL", "Machine Learning"],
    "experience_years": { "min": 3, "max": 5 },
    "education": "Master's in CS or related field"
  }
}

DAY-7 🚀 AI Recruitment Pipeline

An end-to-end AI-powered recruitment pipeline for processing resumes, extracting structured data, scoring candidates, and storing results using a scalable architecture.

🧠 Overview

This project demonstrates how to build a production-ready AI data pipeline using:

- FastAPI (API layer)
- PostgreSQL (structured storage)
- Local/S3 storage (resume files)
- Modular ML pipeline (parsing → features → scoring)

---

🏗️ System Architecture

Client (Upload Resume)
        ↓
FastAPI API Layer
        ↓
Resume Storage (Local / S3)
        ↓
Processing Pipeline
   ├── Resume Parser
   ├── Feature Extractor
   ├── Scoring Model
   └── Report Generator
        ↓
PostgreSQL Database
        ↓
Dataset Versioning (JSON)

📁 Project Structure

Zecpath_AI_pro /
│
├── app/
│   ├── main7.py                # API endpoints
│   ├── db/
│   │   ├── database.py        # DB connection
│   │   └── models.py          # ORM models
│   │
│   ├── services/
│   │   ├── parser.py          # Resume parsing
│   │   ├── scoring.py         # Candidate scoring
│   │   ├── feature_store.py   # Feature extraction
│   │
│   └── utils/
│       └── dataset.py         # Dataset versioning
│
├── storage/
│   └── resumes/               # Uploaded files
│
├── datasets/                  # Versioned datasets
│
└── requirements.txt

---

🔄 Data Pipeline Flow

1. Resume Upload

- User uploads a PDF resume via API
- File stored in "storage/resumes/" (or S3)

2. Resume Parsing

- Extracts:
  - Name
  - Skills
  - Experience
- (Currently rule-based, extensible to NLP/LLMs)

3. Feature Extraction

- Converts parsed data into ML features:
  - Skill count
  - Years of experience

4. Candidate Scoring

- Rule-based scoring (ML-ready)
- Produces ATS-style score (0–100)

5. Data Storage

Stored in PostgreSQL:

- Candidates Table
- ATS Scores Table
- (Optional) Screening Reports

6. Dataset Versioning

- Saves processed data into:

datasets/v1/data.json

- Enables reproducibility & ML training

---

🗄️ Storage Design

1. Structured Storage (PostgreSQL)

Table| Purpose
candidates| Stores parsed resume data
ats_scores| Stores candidate scores
screening_reports| Stores AI-generated reports

---

2. File Storage

- Local: "storage/resumes/"
- Cloud-ready: AWS S3

Stores:

- Raw resume PDFs

---

3. Dataset Storage

- Versioned JSON datasets
- Used for:
  - Model training
  - Experiment tracking

---

🧩 Database Schema

Candidate

- candidate_id (PK)
- name
- parsed_data (JSON)
- created_at

ATSScore

- id (PK)
- candidate_id
- job_id
- score
- model_version
- timestamp

---

⚙️ Setup Instructions

1. Install Dependencies

pip install fastapi uvicorn sqlalchemy psycopg2 boto3 pydantic
Install postgreSQL 16.11
---

2. Start PostgreSQL

Update connection in:

app/db/database.py

DATABASE_URL = "postgresql://postgres:Alina1803@localhost:5432/ai_pipeline"
---

3. Run API

uvicorn app.main7:app --reload

---

4. Open API Docs

http://127.0.0.1:8000/docs

---

📡 API Endpoint

POST "/upload-resume/"

Upload a resume and get a score.

Response:

{
  "candidate_id": "uuid",
  "score": 85
}

---

🧠 ML Readiness

This pipeline is designed to evolve into:

- Feature store integration
- Model training pipeline
- Real-time inference system
- LLM-based resume understanding

---

🚀 Future Improvements

- ✅ Async processing (Celery + Redis)
- ✅ S3 integration
- ✅ Advanced NLP (spaCy / LLMs)
- ✅ Model versioning & A/B testing
- ✅ Frontend dashboard (React)
- ✅ Docker + CI/CD

---

🏁 Conclusion

This project demonstrates a scalable AI data pipeline architecture that bridges:

- Backend engineering
- Data engineering
- Machine learning systems

It can serve as a foundation for building real-world ATS platforms or AI-driven hiring tools.

✅ System thinking (architecture)

✅ Data engineering understanding

✅ ML pipeline awareness

✅ Production mindset

DAY-8 # Resume Section Segmentation

## Objective
Automatically identify and segment resume sections using NLP.

## Features
- Rule-based + ML-based classification
- Handles multiple formats (PDF, DOCX, TXT)
- Accuracy evaluation

## Project Structure
- section_segmention8/ → core logic
- data/raw → datasets
- data/processed/output_8/outputs/ → predictions

## Tech Stack
- Python
- spaCy
- Scikit-learn

## Run
```bash
python main8.py

Day 9 – Skill Extraction Engine

📌 Overview

This module is responsible for extracting technical, business, and soft skills from parsed resume JSON files. It is part of the Zecpath AI hiring pipeline and powers downstream modules such as:

ATS scoring

Resume ↔ JD matching

Semantic ranking

Candidate shortlisting


The engine uses spaCy PhraseMatcher for production-grade NLP-based skill detection.

🎯 Objective

Accurately extract:

Technical skills

Business/domain skills

Soft skills

Multi-word phrases

Skill stacks (MERN, MEAN, etc.)

Synonyms

Spelling variants

Confidence score per skill

🏗️ Project Structure

app/
 └── services/
      └── skill_engine/
           ├── __init__.py
           ├── skill_dictionary.py
           ├── synonym_mapper.py
           ├── stack_resolver.py
           ├── confidence_engine.py
           ├── skill_extractor.py
           └── run_skill_pipeline.py


⚙️ Installation

Install spaCy and the English model:

pip install spacy
python -m spacy download en_core_web_sm

🚀 Features

✅ NLP-based phrase matching
✅ Case

📘 Day 10 – Experience Parsing & Relevance Engine

🎯 Objective

Build a system to:

- Extract professional experience from resumes
- Calculate total experience duration
- Detect gaps and overlapping roles
- Evaluate relevance of experience for a given job description

🧠 Overview

This module is a core part of the AI Resume Screening System.

It transforms raw resume text → structured experience data → relevance score

⚙️ Features

✅ Experience Extraction

- Company names
- Job roles
- Start & end dates
- Duration (in months)

✅ Experience Analysis

- Total experience calculation
- Gap detection
- Overlapping roles detection

✅ Relevance Engine

- Compares experience with job description
- Uses similarity logic (TF-IDF / cosine similarity)
- Generates relevance score (0–100)

✅ Multi-format Resume Support

- TXT
- DOCX
- PDF (text-based)
- Scanned PDFs (OCR enabled)

---

📁 Project Structure

app/
 ├── services/
 │    ├── experience_engine/
 │    │    ├── experience_parser.py
 │    │    ├── relevance_engine.py
 │    │
 │    ├── skill_engine9/
 │    │    ├── skill_extractor.py
 │    │    ├── synonym_mapper.py
 │
 ├── utils/
 │    ├── text_cleaner.py
 │    ├── date_utils.py
 │    ├── constants.py
 │    ├── file_loader.py


🔄 Pipeline Flow

Resume File (TXT / PDF / DOCX)
        ↓
File Loader (with OCR fallback)
        ↓
Text Cleaning
        ↓
Skill Extraction
        ↓
Experience Parsing
        ↓
Gap & Overlap Detection
        ↓
Relevance Scoring
        ↓
Structured JSON Output

📥 Input

Resume files placed in:

data/raw/

📤 Output

Processed results saved in:

data/processed/output_10/

Example output:

{
  "skills": ["audit", "taxation"],
  "experience": {
    "experiences": [
      {
        "company": "EY",
        "role": "Audit Associate",
        "duration_months": 24
      }
    ],
    "total_experience_months": 36
  },
  "relevance": {
    "relevance_score": 82.5
  }
}

🚀 How to Run

python -m app.services.experience_engine.main_pipeline10

---

📦 Dependencies

Install required libraries:

pip install pdfplumber python-docx pytesseract pillow pdf2image scikit-learn

⚠️ OCR Setup (Important)

To process scanned PDFs, install:

- Tesseract OCR
- Poppler (for PDF image conversion)

🧠 Key Learnings

- Resume parsing is unstructured data problem
- Regex alone is not enough → needs flexible logic
- OCR is essential for real-world resumes
- Relevance scoring enables intelligent filtering

🎯 Conclusion

Day 10 builds the core intelligence layer of the resume screening system:

✔ Converts raw resumes into structured experience data
✔ Detects inconsistencies
✔ Scores candidate-job fit


📘 # Day 11 – Implementation Guide

 create:

✔ Education parser
✔ Certification extractor
✔ Structured output
✔ Relevance logic

📁 📦 FOLDER STRUCTURE

Add this:

app/services/education_engine/
    ├── education_parser.py
    ├── certification_parser.py
    ├── education_relevance.py


📤 ✅ OUTPUT FORMAT

{
  "education": [
    {
      "degree": "B.Com from XYZ University",
      "year": "2020"
    }
  ],
  "certifications": [
    "Certified Financial Analyst"
  ],
  "education_relevance": {
    "education_score": 70
  }
}

🧠 SUMMARY

✔ Extracts education
✔ Extracts certifications
✔ Scores relevance
✔ Integrates into pipeline

# 🚀 Day 12 – Semantic Matching Engine

## 🎯 Objective
To move beyond keyword matching and enable deep **semantic resume-to-job matching** using AI embeddings.

## 🔥 Features

- 📄 Resume parsing (TXT, PDF, DOCX)
- 🧹 Text cleaning pipeline
- 🧠 Skill extraction (NLP-based)
- 💼 Experience parsing
- 🎓 Education & certification extraction
- 🤖 Semantic similarity scoring (AI-based)
- 📊 Structured JSON output
- 📁 Batch processing support

## 🏗️ Project Structure

app/ 
│ 
├── services/ 
│   ├── skill_engine9/ 
│   
├── experience_engine/ 
│   ├── education_engine11/ 
│   ├── semantic_engine/ 
│       ├── embedder.py 
│       ├── similarity_engine.py 
│       ├── semantic_matcher.py 
│ ├── utils/ 
│   ├── text_cleaner.py 
│   ├── file_loader.py 
│ data/ 
├── raw/ 
├── processed/ 
│   ├── output_12/

---

## ⚙️ Installation

### 1️⃣ Install dependencies

```bash
pip install spacy
pip install sentence-transformers
pip install scikit-learn
pip install pdfplumber python-docx pytesseract pillow pdf2image

2️⃣ Download spaCy model

python -m spacy download en_core_web_sm


🔥 Semantic Matching Engine

📌 Embedding Model

Uses:

all-MiniLM-L6-v2 (lightweight & fast)


📌 Process

1. Convert resume → embedding

2. Convert job description → embedding

3. Compute cosine similarity

📊 Similarity Score Meaning

Score	Interpretation

0.8+	Excellent match 🔥
0.6–0.8	Good match
0.4–0.6	Average
<0.4	Poor match ❌


▶️ Run Pipeline

python -m app.services.education_engine11.main_pipeline12

📁 Input

Place resumes in:
 
data/raw/

Supported formats:

.txt

.pdf (with OCR fallback)

.docx


📤 Output

Generated in:

data/processed/output_12/


📄 Sample Output

{
  "skills": ["audit", "taxation"],
  "experience": {
    "total_experience_months": 36
  },
  "education": [
    {
      "degree": "B.Com",
      "year": "2020"
    }
  ],
  "semantic_match": {
    "semantic_similarity": 0.82
  }
}


🔍 OCR Support

If PDF text extraction fails, OCR is used.

Install Tesseract:

Download and install Tesseract OCR

Set path in code:


pytesseract.pytesseract.tesseract_cmd = r"D:\tesseract\tesseract.exe"

🚀 Future Improvements

🔥 Final scoring system (skills + experience + semantic)

📊 Candidate ranking system

🌐 FastAPI backend

🧠 Custom ML model for scoring

📈 Dashboard UI


🧠 Tech Stack

Python

spaCy

Sentence Transformers

scikit-learn

pdfplumber

pytesseract


🎯 Outcome

This system provides:

✔ Deep semantic resume matching
✔ AI-based similarity scoring
✔ End-to-end resume analysis pipeline

👉 Ready for real-world ATS systems

 Author

Developed as part of AI Resume Screening System (Day 12)

# Deliverables

✔ Professional documentation  
✔ Clear architecture  
✔ Industry-style README  
✔ Ready for GitHub

# Day 13 – Unified ATS Scoring Pipeline

## Objective
Build a unified ATS scoring pipeline that combines:

- Skill extraction
- Experience relevance
- Education relevance
- Certification extraction
- Semantic similarity
- Final ATS scoring
- Recruiter-friendly score breakdown

This pipeline processes resumes from `data/raw/` and generates structured candidate intelligence JSON files for downstream ranking.

## Folder Structure
app/
└── services/
    └── ats_engine13/
        ├── ats_scorer.py
        └── run_pipeline.py

data/
├── raw/
└── processed/
    └── output_13/


## Pipeline Flow
Resume File
   ↓
File Loader
   ↓
Text Cleaner
   ↓
Skill Extractor
   ↓
Experience Parser + Relevance
   ↓
Education Parser + Relevance
   ↓
Certification Parser
   ↓
Semantic Similarity
   ↓
ATS Final Score
   ↓
JSON Output

## Scoring Components

### 1) Skill Score
Calculated using extracted skill count.

```python
skill_score = min(len(skills) * 10, 100)

# Day 14 – Candidate Ranking & Shortlisting Engine

## Objective
Build a cross-candidate ranking engine that reads Day 13 ATS outputs and converts them into:

- ranked candidate lists
- shortlist decisions
- review queue
- reject queue
- recruiter summaries
- hiring-ready outputs

This module acts as the **decision backbone layer** for Day 15 interview recommendations.

---

## Folder Structure
ranking_engine14/
│
├── rank_candidates.py
├── shortlist_engine.py
├── recruiter_summary.py
└── run_day14_pipeline.py

---

## Pipeline Role
Day 13 generates **individual candidate ATS intelligence**.

Day 14 transforms that into **cross-candidate hiring intelligence**.

### Flow
Day 13 Output JSONs
   ↓
Load All Candidates
   ↓
Sort by Final Score
   ↓
Assign Rank
   ↓
Apply Shortlist Rules
   ↓
Generate Recruiter Summary
   ↓
Save Ranked Output JSON

---

## Module Details

### `rank_candidates.py`
Responsible for:
- sorting candidates by `final_score`
- assigning rank positions
- preserving recruiter-ready order

### Logic
```python
ranked = sorted(
    candidates,
    key=lambda x: x["scores"]["final_score"],
    reverse=True
)

# Day 15 – Fairness, Normalization & Bias Reduction

## Objective
Improve fairness, reduce hidden bias, and standardize candidate evaluation after Day 14 ranking.

This module ensures:
- resume format neutrality
- score normalization
- sensitive field masking
- recruiter-safe candidate outputs
- fairness audit reporting

This acts as the **ethical AI decision layer** before recruiter review.

---

## Folder Structure

fairness_engine15/
│
├── resume_normalizer.py
├── score_normalizer.py
├── bias_masking.py
├── fairness_audit.py
└── run_fairness_pipeline.py

---

## Pipeline Flow
Day 14 Ranked Output
   ↓
Resume Standardization
   ↓
Sensitive Attribute Masking
   ↓
Score Normalization
   ↓
Fairness Audit
   ↓
Bias-Safe Recruiter Output

## Input
Reads from:
data/processed/output_14/ranked_candidates.json

## Output 
Python -m app.services.fairness_engine15.run_fairness_pipeline15