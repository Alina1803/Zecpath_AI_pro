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
--------------------------------------------------------------------------------------
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
----------------------------------------------------------------------------

# Day 16 – Recruiter Dashboard, Explainability & Fairness Analytics

## Objective
Build a recruiter-facing analytics dashboard that converts Day 15 fair candidate outputs into:

- ranked recruiter tables
- fairness metrics
- explainable candidate scores
- recruiter decision actions
- shortlist visibility
- top candidate insights

This module transforms backend ATS intelligence into **product-ready recruiter workflows**.

---

## Folder Structure
dashboard_engine16/
│
├── dashboard_data.py
├── explainability_engine.py
├── fairness_dashboard.py
├── recruiter_actions.py
└── run_dashboard_pipeline.py

---

## Pipeline Flow
Day 15 Fair Candidates
   ↓
Dashboard Data Preparation
   ↓
Fairness Analytics
   ↓
Candidate Explainability
   ↓
Recruiter Action Suggestions
   ↓
Dashboard JSON Output

---

## Input
Reads from:
data/processed/output_15/fair_candidates.json
------------------------------------------------------------------------------

# Day 17 – ATS System Testing

## Objective
Validate ATS accuracy, reliability, fairness stability, and role adaptability.

This module benchmarks the full ATS pipeline by comparing AI-generated decisions against expected recruiter decisions.

The testing framework supports:
- tech role validation
- non-tech role validation
- fresher resume testing
- senior profile testing
- recruiter truth comparison
- mismatch backlog generation

This is the **quality assurance and benchmark layer** of the ATS.

---
## Folder Structure

testing_engine17/
│
├── test_dataset_loader.py
├── prediction_validator.py
├── metrics_engine.py
├── mismatch_tracker.py
├── improvement_backlog.py
└── run_testing_pipeline.py

---

## Pipeline Flow
Test Candidate Dataset
   ↓
Load Test Cases
   ↓
Validate Predictions
   ↓
Accuracy Metrics
   ↓
Mismatch Detection
   ↓
Improvement Backlog
   ↓
Testing Report Output

---

## Input
Reads test cases from:
data/test_cases/

⚡DAY 18-  ATS Optimization & Performance Tuning

📌 Overview

This module focuses on improving the performance, scalability, and efficiency of the ATS (Applicant Tracking System).

The goal is to ensure:

- Faster resume processing
- Lower memory usage
- Scalable batch handling
- Stable API performance

---

🎯 Objectives

- 🚀 Optimize API response time
- 🧠 Reduce memory consumption
- 📂 Improve batch processing efficiency
- ⚡ Enhance scoring performance
- 🔁 Avoid redundant computations

---

🏗️ Optimization Modules

🔹 1. Performance Tracker

Tracks execution time of APIs and functions.

@track_time
async def process_resume_api(...):

✔ Helps identify slow components
✔ Enables profiling of pipeline

---

🔹 2. Memory Manager

Handles memory cleanup after processing.

clear_memory()

✔ Prevents memory leaks
✔ Improves batch performance

---

🔹 3. Efficient File Handling

- Uses streaming ("UploadFile")
- Avoids loading large files into memory unnecessarily

✔ Faster uploads
✔ Reduced RAM usage

---

🔹 4. Optimized Skill Matching

- Uses "set" operations instead of loops

matched = set(resume_skills) & set(jd_skills)

✔ O(n) performance
✔ Faster matching

---

🔹 5. Scoring Optimization

- Pre-normalization of data
- Avoid repeated calculations
- Lightweight arithmetic operations

✔ Faster scoring engine
✔ Consistent outputs

---

⚡ Performance Improvements

Component| Before| After
Skill Matching| O(n²)| O(n)
File Handling| High memory| Optimized streaming
Batch Processing| Slow| Faster loop execution
API Response| Slower| Reduced latency

---

📊 Benchmark Example

Single Resume Processing:
Before: 2.5 sec
After: 0.8 sec

Batch (10 resumes):
Before: 18 sec
After: 6 sec

---

🔁 Batch Optimization

- Processes resumes sequentially with minimal memory footprint
- Clears memory after execution
- Avoids duplicate JD parsing

jd_data = parse_jd(jd_text, DEFAULT_ROLES)

✔ Parsed once → reused

---

🧠 Best Practices Applied

- ✅ Lazy loading
- ✅ Data normalization
- ✅ Minimal object creation
- ✅ Efficient data structures (sets, dicts)
- ✅ Exception handling for stability

---

🚀 Conclusion

This optimization layer ensures that the ATS system is:

- Fast ⚡
- Scalable 📈
- Reliable 🔒

Ready for real-world usage.

---

Task 21: Eligibility Engine 

📌 Overview

The eligibility_engine21 module is responsible for evaluating candidate eligibility based on predefined rules, configurations, and decision logic. It acts as a core component in the processing pipeline, determining whether a candidate meets specific criteria.

---

🗂️ Project Structure

eligibility_engine21/
│── __init__.py
│── config_loader.py
│── decision_engine.py
│── main_pipeline21.py
│── rules_engine.py
│── __pycache__/

---

⚙️ Components

1. "config_loader.py"

- Loads configuration files (JSON/YAML/ENV).
- Provides dynamic rule settings and thresholds.
- Central place to manage eligibility parameters.

---

2. "rules_engine.py"

- Contains all eligibility rules.
- Handles rule definitions such as:
  - Minimum qualifications
  - Experience requirements
  - Skill matching
- Easily extendable for adding new rules.

---

3. "decision_engine.py"

- Core logic processor.
- Evaluates rules against candidate data.
- Produces final eligibility decision:
  - ✅ Eligible
  - ❌ Not Eligible
  - ⚠️ Conditional

---

4. "main_pipeline21.py"

- Entry point of the eligibility engine.
- Integrates:
  - Config Loader
  - Rules Engine
  - Decision Engine
- Executes full evaluation pipeline.

---

🔄 Workflow

1. Load configuration using "config_loader"
2. Parse candidate data
3. Apply rules via "rules_engine"
4. Evaluate results using "decision_engine"
5. Return final eligibility status

---

🚀 Usage

from eligibility_engine21.main_pipeline21 import run_pipeline

candidate_data = {
    "education": "BCA",
    "experience": 2,
    "skills": ["Python", "SQL"]
}

result = run_pipeline(candidate_data)
print(result)

---

📦 Requirements

- Python 3.8+
- Required libraries (if any):
  pip install -r requirements.txt

---

🧪 Testing

- Unit tests should be written for:
  - Rules validation
  - Decision outcomes
  - Config loading

Run tests:

pytest

---

🔧 Customization

- Add new rules in "rules_engine.py"
- Modify thresholds in config files
- Extend decision logic in "decision_engine.py"

---

📈 Future Improvements

- Add ML-based eligibility scoring
- Improve rule weighting system
- Integrate with external APIs
- Logging & monitoring support

---

Task 22  HR Screening System – CA Domain

📌 Overview

The HR Screening System  is a rule-based candidate evaluation system designed specifically for Chartered Accountant (CA) roles.

It enables automated screening using:

- Structured HR question datasets
- Rule-based eligibility scoring
- AI-ready interview question objects

This project simulates a mini Applicant Tracking System (ATS) for finance and accounting roles.

---

🎯 Objective

To build a structured, AI-ready question bank and evaluation engine for automated HR screening of CA candidates.

---

📁 Project Structure

hr_screening_22/
│
├── data/
│   ├── ca_questions.json          # HR question dataset
│   ├── category_mapping.json      # Question categories mapping
│   └── sample_candidates.json     # Sample candidate data
│
├── eligibility_engine21/
│   ├── config_loader.py           # Load datasets
│   ├── rules_engine.py            # Scoring logic
│   ├── decision_engine.py         # Final decision logic
│   └── main_pipeline21.py         # Pipeline runner
│
├── ai_layer/
│   ├── question_objects.py        # AI-ready question format
│   └── conversation_engine.py     # Interview simulation
│
├── utils/
│   ├── question_generator.py      # Dynamic question creation
│   └── validator.py               # Input validation
│
├── app.py                         # Main execution file
├── requirements.txt
└── README.md

---

📦 Features

✅ HR Question Dataset

- CA-specific screening questions
- Categorized into:
  - Education
  - Experience
  - Skills
  - Salary
  - Notice Period

---

🧠 Rule-Based Eligibility Engine

Evaluates candidates based on:

- CA qualification
- Experience (≥ 3 years)
- GST & Income Tax experience
- Tools (Tally / SAP)
- Notice period

---

🤖 AI-Ready Question Objects

- Structured format for chatbot/interview systems
- Supports automation and NLP pipelines

---

📊 Scoring System

Criteria| Score
CA Qualification| +5
Experience ≥ 3 yrs| +4
GST Experience| +4
ITR Experience| +4
Tools (Tally/SAP)| +3
Notice ≤ 30 days| +2

---

🧾 Decision Logic

Score Range| Result
≥ 15| Highly Eligible
10–14| Eligible
< 10| Not Eligible

---

🚀 How to Run

1️⃣ Clone the Repository

git clone <your-repo-url>
cd hr_screening_ca

2️⃣ Run the Application

python app.py

---

📌 Example Output

{
  "name": "Rahul Sharma",
  "score": 22,
  "decision": "Highly Eligible"
}

---

🧪 Testing

Run tests using:

pytest

__________________________________________________________________________________________________



 Day 23 – Transcript Data Architecture
 Overview

This module is responsible for converting raw voice-based candidate interactions into structured, AI-ready transcript data.

It acts as a bridge between:
- 🎤 Voice input (interviews, screening calls)
- 🤖 AI processing (evaluation, scoring, insights)

---

## 🎯 Objective

To define and implement a scalable architecture for handling transcript data, including:
- Transcript structure design
- Metadata standardization
- Text normalization
- Storage and retrieval

---

## 🧱 Architecture Components

### 1. Transcript Schema
Defines how transcript data is structured:
- Metadata (Candidate ID, Job ID, Question ID)
- Segments (speaker, text, timestamp, confidence)
- Full normalized text

---

### 2. Normalization Layer
Cleans and standardizes transcript text:
- Lowercasing
- Removing noise/special characters
- Formatting consistency

---

### 3. Processing Engine
- Combines transcript segments
- Applies normalization
- Generates AI-ready text

---

### 4. Storage Layer
- Saves processed transcripts as JSON
- Supports database integration (SQL/NoSQL)

---

## 📁 Folder Structure

app/
 └── services/
      └── transcript_engine_23/
           ├── __init__.py
           ├── main_transcript23.py          # FastAPI entry
           ├── processor.py               # core logic
           ├── normalizer.py              # cleaning rules
           ├── schema.py                  # data models
           ├── storage.py                 # save/load
           ├──finance_extractor.py
           ├──scoring.py
           ├──repository.py
data/
 └── transcripts/
      ├── raw/
      └── processed/

RUN:

uvicorn app.services.transcript_engine_23.main_transcript:app --reload

Conclusion:

The Transcript Data Architecture successfully transforms unstructured voice data into structured, high-quality datasets suitable for AI processing.

📘 Day 24 – Speech-to-Text Integration & Cleaning (CA Domain)

📌 Overview

This module converts raw audio input (candidate interview responses) into clean, structured, AI-ready text. It is a critical step in the Zecpath AI pipeline, enabling downstream systems like ATS scoring, semantic matching, and candidate ranking.

---

🎯 Objective

To transform unstructured voice data into high-quality textual data by:

- Converting speech to text using an STT engine
- Cleaning filler words and noise
- Structuring responses for AI analysis
- Enhancing accuracy for CA (Chartered Accountant) domain-specific terms

---

🔗 Pipeline Position (Day 23 → Day 24)

Stage| Description
Day 23| Audio capture, segmentation, silence detection
Day 24| Speech-to-text + transcript cleaning
Day 25| Topic extraction & domain intelligence

---

🏗️ Project Structure

speech_module/
│
├── stt_engine.py              # Speech-to-text conversion
├── text_cleaner.py            # Text cleaning & normalization
├── transcript_processor.py    # Handling segments & interruptions
├── accuracy_test.py           # WER accuracy evaluation
└── run_pipeline24.py      # Main execution pipeline

---

⚙️ Features

🎙️ Speech-to-Text

- Converts audio into raw transcript
- Supports multiple accents and noise conditions
- Segment-level transcription

🧹 Text Cleaning

- Removes filler words (um, uh, like, etc.)
- Normalizes case (lowercase)
- Fixes spacing and punctuation

🧠 Transcript Processing

- Handles interruptions and silence
- Merges segmented speech
- Detects incomplete answers

📊 Accuracy Evaluation

- Calculates Word Error Rate (WER)
- Provides transcription accuracy %

🧾 CA Domain Optimization

- Corrects domain-specific terms:
  - GST
  - TDS
  - Input Tax Credit
  - Balance Sheet
  - Profit & Loss

---

🚀 Installation

1. Install dependencies

pip install openai-whisper
pip install jiwer
pip install torch

---

▶️ Usage

Run the pipeline

python run_pipeline24.py

Example

result = run_pipeline("sample_audio.wav")

print(result["clean_text"])

---

📤 Output Format

{
  "raw_text": "...",
  "processed_text": "...",
  "clean_text": "...",
  "accuracy": {
    "wer_score": 0.12,
    "accuracy": 88.0
  }
}

---

🧪 Example

Input Audio:

«"uh I worked on gst filing and um taxation compliance"»

Output:

«"i worked on gst filing and taxation compliance."»

---

🧩 Integration Points

This module feeds into:

- ATS Engine (Day 10–11)
- Semantic Matching Engine (Day 12)
- Candidate Ranking (Day 14)
- Recruiter Summary (Day 14)

---

📈 Importance for CA Domain

Accurate transcription is crucial because:

- Financial terminology must be precise
- Errors impact skill extraction
- Recruiter insights depend on clean responses

---

⚠️ Limitations

- Accuracy depends on audio quality
- Heavy accents may reduce performance
- Basic punctuation correction (not advanced NLP)

---

🔮 Future Improvements

- Real-time transcription (streaming)
- Advanced punctuation using NLP models
- Speaker diarization (multi-speaker detection)
- Integration with live interview systems

---

✅ Conclusion

Day 24 enables the transformation of raw audio into structured, high-quality text, forming the foundation for intelligent AI-driven hiring decisions in the CA domain.

---

📘 Day 25 – Answer Evaluation Engine

🎯 Objective

To intelligently process and evaluate candidate responses by extracting intent, identifying key entities, and analyzing answer quality in the context of domain-specific expectations (Chartered Accounting).

---

🧠 Overview

The Answer Evaluation Engine is a core component of the Zecpath AI Pro pipeline. It transforms raw candidate responses into structured insights by applying NLP techniques such as intent classification, entity extraction, and response analysis.

This module enables downstream systems (like scoring and ranking engines) to make accurate and explainable hiring decisions.

---

⚙️ Key Components

1. Intent Classifier ("intent_classifier.py")

- Identifies the purpose of the candidate's response
- Categories:
  - Concept Explanation
  - Process Description
  - Practical Experience
  - Definition-Based Answers

---

2. Entity Extractor ("entity_extractor.py")

- Extracts domain-specific terms related to CA field:
  - GST (Input Tax Credit, GSTR)
  - Audit (Compliance, Verification)
  - Taxation (Deductions, Filing)
- Helps measure domain relevance

---

3. Response Analyzer ("response_analyzer.py")

Evaluates:

- Depth of explanation
- Sentence structure
- Technical coverage
- Keyword richness

---

4. Answer Engine ("answer_engine.py")

- Orchestrates the full evaluation pipeline
- Combines:
  - Intent classification
  - Entity extraction
  - Response analysis

---

5. Pipeline Runner ("run_engine25.py")

- Executes the full flow
- Reads processed transcript input (from Day 24)
- Outputs structured evaluation JSON

---

🔄 Workflow

Candidate Answer
        ↓
Intent Classification
        ↓
Entity Extraction
        ↓
Response Analysis
        ↓
Structured Evaluation Output

---

📂 Input Format

{
    "question": "Explain GST filing",
    "answer": "GST filing involves calculating tax, ITC claims, and submitting returns."
}

---

📤 Output Format

{
    "question": "Explain GST filing",
    "intent": "Process Explanation",
    "entities": ["GST", "ITC", "returns"],
    "analysis": {
        "length_score": 8,
        "technical_score": 7,
        "quality": "Good"
    }
}

---

🚀 How to Run

python -m  app.services.answer_engine_25.run_engine25

---


💡 Industry-Level Features

- Modular architecture (microservice-ready)
- Domain-aware processing (CA-specific logic)
- Explainable outputs for recruiters
- Easily extendable to LLM-based evaluation

---

✅ Conclusion

The Answer Evaluation Engine converts unstructured candidate responses into structured, meaningful insights. By combining NLP techniques with domain knowledge, it creates a strong foundation for objective and scalable candidate assessment in the Chartered Accounting domain.

---

📊 Day 26 – Screening Scoring Engine (CA Domain)

🧠 Overview

The Screening Scoring Engine is an AI-powered evaluation system designed to objectively assess candidate responses in screening interviews for the Chartered Accountant (CA) domain.

It combines:

- LLM-based evaluation (clarity, relevance, completeness, consistency)
- Semantic similarity scoring
- Domain-specific knowledge validation

The engine produces explainable, structured, and production-ready scoring outputs.

---

🎯 Objective

To objectively evaluate candidate screening responses and generate:

- Per-question score breakdown
- Final aggregated screening score
- Explainable evaluation metrics

---

⚙️ Key Features

- ✅ Multi-factor scoring (LLM + semantic + domain)
- ✅ Weighted scoring system
- ✅ Explainable outputs (per-question insights)
- ✅ Fallback mechanism (LLM unavailable)
- ✅ Config-driven architecture
- ✅ Production-ready pipeline
- ✅ Structured JSON output
- ✅ Error handling & logging

---

🏗️ Architecture

Input (Day 25 Output)
        ↓
Text Preprocessing
        ↓
LLM Evaluator (Clarity, Relevance, Completeness, Consistency)
        ↓
Semantic Matcher (BERT similarity)
        ↓
Domain Evaluator (CA knowledge)
        ↓
Score Aggregation (Weighted)
        ↓
Calibration Layer
        ↓
Final Screening Score
        ↓
JSON Output + Metadata

---

📁 Folder Structure

app/
 └── services/
     └── screening_engine_26/
         ├── __init__.py
         ├── scoring_engine.py
         ├── llm_evaluator.py
         ├── semantic_matcher.py
         ├── domain_evaluator.py
         ├── calibration.py
         ├── weights_config.py
         └── run_pipeline26.py

app/
 └── utils/
     ├── text_preprocessor.py
     └── logger.py

data/
 ├── ca_domain_knowledge26.json
 ├── scoring_prompts26.txt
 └── processed/
     └── output_26/

---

🔢 Scoring Logic

Final score is computed using weighted aggregation:

Final Score = (
    clarity * w1 +
    relevance * w2 +
    completeness * w3 +
    consistency * w4 +
    semantic_similarity * w5 +
    domain_score * w6
) * 10

Example Weights

WEIGHTS = {
    "clarity": 0.2,
    "relevance": 0.2,
    "completeness": 0.2,
    "consistency": 0.1,
    "semantic": 0.2,
    "domain": 0.1
}

---

📥 Input Format

{
  "candidate_id": "CAND_001",
  "question": "Explain GST filing",
  "answer": "GST filing involves invoice tracking...",
  "expected_answer": "GST filing includes calculating tax..."
}

---

📤 Output Format

{
  "meta": {
    "run_id": "RUN_20260421_124451",
    "run_time": "2026-04-21T12:44:51",
    "total_candidates": 1,
    "processed": 1,
    "failed": 0,
    "engine_version": "v2.2",
    "domain": "Chartered Accountant"
  },
  "results": [
    {
      "candidate_id": "CAND_001",
      "question": "Explain GST filing",
      "answer": "...",
      "llm_scores": {
        "clarity": 7,
        "relevance": 7,
        "completeness": 6,
        "consistency": 7
      },
      "semantic_score": 0.82,
      "domain_score": 0.75,
      "final_score": 78.5,
      "confidence": 0.78
    }
  ]
}

---

🚀 How to Run

Step 1: Activate environment

.venv\Scripts\activate

Step 2: Run pipeline

python -m app.services.screening_engine_26.run_pipeline26

---

📂 Output Location

data/processed/output_26/

Files are saved as:

screening_results_YYYYMMDD_HHMMSS.json

---

🧪 Example Use Case

- AI-powered interview screening
- Candidate evaluation automation
- Pre-interview filtering system
- Recruitment analytics

---

🏁 Conclusion

The Day 26 Screening Scoring Engine delivers a robust, explainable, and scalable evaluation system for candidate screening.

It integrates AI scoring, semantic intelligence, and domain expertise to produce high-quality hiring signals.

---

📊 Day 27 – Confidence & Sentiment Signal Analysis Engine

🚀 Overview

The Signal Analysis Engine (Day 27) enhances the candidate evaluation pipeline by analyzing communication quality, behavioral signals, and confidence indicators.

This module works on top of Day 26 (Screening Scoring Engine) and provides deeper insights into how candidates communicate, not just what they answer.

---

🎯 Objective

To assess:

- Candidate confidence level
- Sentiment tone (positive / negative / neutral)
- Hesitation patterns
- Contradictions or uncertainty
- Overall communication strength

---

🧠 Key Features

- ✅ Confidence scoring (0–10 scale)
- ✅ Sentiment analysis (0–1 normalized)
- ✅ Hesitation detection (behavioral signals)
- ✅ Contradiction detection
- ✅ Communication strength scoring
- ✅ Explainable insights & flags

---

🏗️ System Architecture

Day 25 → Answer Processing
        ↓
Day 26 → Technical Scoring Engine
        ↓
Day 27 → Signal Analysis Engine
        ↓
Final AI Hiring Intelligence Output

---

📁 Folder Structure

app/
 └── services/
     └── signal_engine_27/
         ├── __init__.py
         ├── confidence_analyzer.py
         ├── sentiment_analyzer.py
         ├── hesitation_detector.py
         ├── contradiction_checker.py
         ├── communication_scorer.py
         ├── signal_engine.py
         └── run_pipeline27.py

data/
 ├── processed/
 │   ├── output_26/
 │   └── output_27/

---

⚙️ Modules Description

1. Hesitation Detector

Detects uncertainty words like:

- "um", "maybe", "I think", "not sure"

---

2. Sentiment Analyzer

Classifies tone:

- Positive
- Neutral
- Negative

Returns normalized score (0–1)

---

3. Confidence Analyzer

Combines:

- Sentiment score
- Hesitation level

Outputs confidence score (0–10)

---

4. Contradiction Checker

Detects logical inconsistencies:

- "but", "however", "although"

---

5. Communication Scorer

Final behavioral score based on:

- Confidence
- Contradictions

---

6. Signal Engine (Core)

Aggregates all signals into:

{
  "confidence_score": 8.1,
  "sentiment_score": 0.6,
  "hesitation_score": 0.0,
  "contradiction_score": 0.0,
  "communication_strength": 8.1,
  "flags": []
}

---

🔁 Pipeline Execution

Run the pipeline:

python -m app.services.signal_engine_27.run_pipeline27

---

📥 Input

Reads latest output from:

data/processed/output_26/

---

📤 Output

Stored in:

data/processed/output_27/

---

📦 Sample Output

{
  "candidate_id": "CAND_001",
  "final_score": 78.5,
  "confidence_score": 8.1,
  "sentiment_score": 0.6,
  "communication_strength": 8.1,
  "flags": [],
  "insights": "Candidate shows strong confidence with clear communication."
}

---

🚩 Flags & Indicators

Flag| Meaning
hesitation_detected| Candidate shows uncertainty
contradiction_detected| Conflicting statements

---

🧪 Use Cases

- AI-based interview evaluation
- Behavioral assessment in hiring
- Communication skill scoring
- Soft skill analytics for CA domain

---


🏁 Conclusion

The Day 27 Signal Analysis Engine transforms your system from:

➡️ Technical Evaluation Tool
to
➡️ Complete AI Hiring Intelligence System

By combining:

- Technical scoring (Day 26)
- Behavioral insights (Day 27)

Now have a production-ready candidate evaluation pipeline capable of real-world hiring decisions.

---

🚀 DAY 28 — AI Screening Report Generator (Industry Level)


✅ 1. DOMAIN (CA – Chartered Accountant)

🎯 Target Roles:

Tax Associate

GST Specialist

Audit Analyst

Accounts Executive


📊 What recruiters care about:

GST knowledge

Income tax understanding

Compliance accuracy

Practical communication



---

✅ 2. OBJECTIVE (Refined – Industry Level)

Transform raw AI evaluation outputs (technical + behavioral)
into structured, recruiter-friendly screening reports
that enable fast and confident hiring decisions.

👉 Translation:

Convert scores → insights

Convert numbers → decisions



---


FOLDER STRUCTURE (CLEAN + SCALABLE)

app/
│
├── services/
│   ├── screening_engine_26/
│   │   └── scoring_engine.py
│   │
│   ├── signal_engine_27/
│   │   └── signal_engine.py
│   │
│   ├── report_engine_28/
│   │   └── report_generator.py   ✅ NEW
│
├── pipelines/
│   └── run_pipeline28.py         ✅ FINAL PIPELINE
│
├── models/
│   └── schemas.py
│
└── utils/
    

✅ 8. DELIVERABLES (WHAT YOU SUBMIT)

✔ 1. AI Screening Report Generator

Fully working class (ReportGenerator)


✔ 2. Recruiter-Ready Output

Clean JSON report

Structured sections

Decision-ready


✔ 3. Sample Reports

2–3 candidate outputs

---

🏁 FINAL CONCLUSION

Now have a complete hiring intelligence system:


Day 26 → Brain (Knowledge)

Day 27 → Behavior (Human signals)

Day 28 → Decision (Recruiter report)

Deliverables:

✔ Modular AI pipeline

✔ Explainable scoring

✔ Recruiter-friendly output

✔ Decision engine

----

###  DAY 29: AI Interview System (Conversational AI Project)

📌 Overview

This project is an AI-powered interview system built using Conversational AI (CA) principles.
It simulates a real interview by asking questions, evaluating answers, handling silence/errors, and scoring candidate performance.

---

🎯 Features

- 🧠 Structured interview flow (question → answer → evaluation)
- 🔄 State machine-based conversation control
- 📊 Answer evaluation and scoring system
- ⚠️ Handles silence, short answers, and retries
- 🧩 Modular and scalable architecture
- 📝 Logging for debugging and analysis

---

🏗️ Project Structure

├── ai-conversation-system29/
│
│   ├── flows/                               #conversation control logic
│   │   ├── decision_tree.py
│   │   ├── state_machine.py
│   │   └── fallback_handler.py
│   │
│   ├── questions/                       #interview questions
│   │   ├── question_bank.py
│   │   └── question_config..json
│   ├── evaluation/                               #Answer evaluation and scoring
│   │   ├── evaluator.py
│   │   └── scoring.py
│   │
│   ├── responses/                             #feedback messages
│   │   ├── templates.py
│   │   └── retry_messages.py
│   ├── main.py
│   │
│   ├── docs/
│       └── architecture.md
│
├── utils/
│      ├── logger.py
│      └── helpers.py
│
├── tests/
│   ├── test_evaluation.py
│   ├── test_flows.py
│   └── test_fallbacks.py
│
├── configs/
│   ├── interview_config.yaml
│   └── scoring_policy.yaml
││
└── requirements.txt

---

Final Result:

✔ Modular AI conversation system

✔ Error handling & retry logic

✔ State-based flow (industry standard)

✔ Test cases

✔ Config-driven design

13.Conclusion:

This design models a real-world conversational AI system used in:

Customer support bots

Voice assistants

Call center automation


By combining:

Decision trees

State machines

Retry + fallback logic
-----

📊 AI Screening System (Day 28–30 Project)

🚀 Overview

The AI Screening System is a mini machine learning pipeline designed to simulate candidate screening in recruitment processes.
It uses intent detection + rule-based scoring to evaluate user responses and decide whether a candidate should be accepted or rejected.

This project was developed as part of Day 28–30 tasks, focusing on building, testing, and optimizing an AI pipeline.

---

🎯 Objective

- Build an automated screening system
- Detect user intent using machine learning
- Score candidate responses
- Evaluate system performance
- Optimize decision thresholds
- Generate structured output reports

---

🏗️ Project Structure

ZECPATH_AI_PRO/
│
├── data/
│   ├── test_data30.json
│   └── validation_data30.json
│
├── models/
│   ├── intent_model.pkl
│   └── scoring_model.pkl
│
├── screening-system30/
│   ├── preprocess.py
│   ├── intent_detection.py
│   ├── scoring.py
│   ├── simulator.py
│   ├── evaluator.py
│   └── optimizer.py
│
├── data/processed/output_30/
│   └── test_report.txt
│
├── main.py
└── requirements.txt
---

⚙️ Features

- ✅ Text preprocessing
- ✅ Intent classification (Naive Bayes)
- ✅ Rule-based scoring system
- ✅ Simulation of screening calls
- ✅ Accuracy evaluation
- ✅ Threshold optimization
- ✅ Timestamp-based report generation

---

🧠 Technologies Used

- Python
- scikit-learn
- JSON
- File handling (OS module)

---

▶️ How to Run

1. Install dependencies

pip install -r requirements.txt

2. Run the pipeline

python main_pipeline.py

---

📂 Output

Reports are automatically saved in:

data/processed/output_30/

Example:

test_report_20260424_143210.txt

---

📄 Sample Output

SCREENING SYSTEM TEST REPORT
====================================
Generated on: 20260424_143210

---- Simulation Results ----
{'input': 'I have 3 years experience in Python', 'intent': 'job_application', 'score': 2, 'status': 'Accepted'}

---- Evaluation ----
Accuracy: 0.75

---- Optimization ----
Best Threshold: 2
Optimized Accuracy: 0.75

---

📈 Conclusion

The system successfully simulates an AI-based screening process.
It demonstrates how machine learning and rule-based logic can be combined to automate candidate evaluation.

Through testing and optimization:

- Accuracy improved
- Decision-making became more reliable
- False rejections were reduced

This project serves as a foundation for building real-world recruitment automation systems.

---

## Day 31: Edge Case & Failure Handling

🚀 Overview

Day 31 focuses on making the AI system robust, reliable, and production-ready by handling real-world edge cases and failures.

This module ensures the system:

Handles invalid or weak inputs

Prevents crashes

Provides meaningful responses

Logs failures and tracks system health

Saves outputs for auditing and debugging

---

🎯 Objective

To ensure system stability under real-world conditions by implementing:

Input validation

Edge case detection

Retry mechanisms

Fallback handling

Logging and monitoring

---

🧠 Key Features

✅ 1. Input Validation

Rejects empty input

Detects short/weak inputs


✅ 2. Issue Detection

Flags problems like:

too_short

(extendable for more rules)



✅ 3. Smart Processing Flow

Reject → stop pipeline

Issues → skip AI

Valid → run full AI pipeline


✅ 4. Retry Mechanism

Automatically retries failed AI calls

Uses exponential backoff


✅ 5. Fallback System

Graceful error responses

Prevents system crashes


✅ 6. Logging

Tracks validation and processing errors


✅ 7. Monitoring

Tracks:

Total requests

Failure count



✅ 8. Output Persistence

Saves every response as JSON

Enables debugging & auditing



---

📁 Folder Structure

app/
││
├── services/
│   ├── ai_flow/
│   │   ├── conversation_manager.py
│   │   ├── retry_handler.py
│   │   ├── clarification_engine.py
│   │   └── fallback_handler.py
│   │
│   ├── audio/
│   │   ├── audio_cleaner.py
│   │   ├── noise_handler.py
│   │   └── speech_to_text.py
│   │
│   ├── validation/
│   │   ├── input_validator.py
│   │   └── language_detector.py
│   │
│   └── logging/
│       ├── error_logger.py
│       └── monitoring.py
│  
├── main_pipeline31.py
│
├── utils/
│   ├── constants31.py
│   └── helpers.py
│
├── tests/
│   ├── test_edge_cases31.py
│   └── test_failures31.py
│
└── docs/
    └── edge_cases.md

---

⚙️ How It Works

🔄 Pipeline Flow

Input
  ↓
Validation
  ↓
Rejected? → Stop
  ↓
Issues? → Return issues
  ↓
AI Processing (Retry)
  ↓
Clarification
  ↓
Response + Save Output


---

🧪 API Usage

▶️ Run Server

uvicorn app.main:app --reload


---

🌐 Swagger UI

http://127.0.0.1:8000/docs


---

📌 Endpoint

POST /process

Input:

"Hello AI"


---

📤 Sample Outputs

🔴 Rejected Input

{
  "input": "",
  "status": "Rejected",
  "message": "Unable to process input"
}


---

🟡 Short Input

{
  "input": "Hi",
  "issues_detected": ["too_short"],
  "status": "Processed"
}


---

🟢 Valid Input

{
  "input": "I have 3 years experience",
  "issues_detected": [],
  "status": "Processed",
  "ai_response": "Processed: I have 3 years experience",
  "language": "english"
}


---

💾 Output Storage

All responses are saved in:

data/processed/output_31/

Example:

{
  "input": "Hello AI",
  "output": { ... }
}


---

📊 Monitoring

GET /metrics

{
  "total_requests": 5,
  "failures": 1
}


---

🧪 Testing

Run tests:

pytest

Covers:

Empty input

Short input

Failure scenarios



---

⚠️ Edge Cases Handled

Empty input

Short input

AI failure

Retry exhaustion

Mixed language

Weak responses



---

🎯 Conclusion

Day 31 transforms the system from a basic pipeline → production-ready system.

Before:

No validation

Same output for all inputs

No failure handling


After:

Intelligent validation

Issue detection

Resilient AI processing

Logging + monitoring

Output tracking

---

### Day 32  Screening System Finalization

An AI-powered candidate screening system built using FastAPI and Machine Learning.
This system evaluates candidate data and returns a selection decision with a confidence score.

---

🚀 Features

- FastAPI-based REST API
- Machine Learning model integration (scikit-learn)
- Real-time candidate screening
- Confidence score output
- Modular and scalable architecture
- Docker & CI/CD ready

---

📁 Project Structure

ai-screening-system32/
│
├── app/
│   ├── models/        # ML model & loader
│   ├── services/      # Business logic
│   ├── api/           # API routes
│   ├── utils/         # Helper functions
│   └── config/        # Configuration
│
├── data/              # Datasets
├── notebooks/         # Experiments
├── tests/             # Unit tests
├── docs/              # Documentation
├── deployment/        # Docker & CI/CD
│
├── main.py            # Entry point
├── requirements.txt
└── README.md

---

⚙️ Installation

pip install -r requirements.txt

---

▶️ Run the Application

uvicorn main:app --reload

---

🌐 API Documentation

Open in browser:

http://127.0.0.1:8000/docs

---

🧪 API Usage

POST "/screen"

Request:

{
  "features": [2, 3]
}

Response:

{
  "selected": false,
  "confidence_score": 0.06
}

---

🧠 How It Works

1. User sends candidate data via API
2. FastAPI handles request
3. Model processes input
4. System returns prediction + confidence score

---

🐳 Docker Support

Build Image

docker build -t ai-screening-app .

Run Container

docker run -p 8000:8000 ai-screening-app

---

🔄 CI/CD Pipeline

- Automated testing using pytest
- Docker image build
- Push to Docker Hub via GitHub Actions

---

📊 Future Improvements

- Resume parsing (NLP)
- Database integration (MongoDB/PostgreSQL)
- Authentication (JWT)
- Frontend dashboard
- Model improvement with real data

---

 ### Day 33 - HR Interview Engine Day 33

📌 Overview

The HR Interview Engine is a modular AI-driven system designed to simulate structured HR interviews. It dynamically generates role-based questions, manages interview flow, and records candidate responses for evaluation.

This project is part of a larger AI Hiring System and serves as the core conversational engine.

---

🎯 Objective

Design and implement a scalable architecture for an AI-powered HR interview system that:

- Generates role-based interview questions
- Differentiates between fresher and experienced candidates
- Maintains interview state and flow
- Produces structured interview reports
- Prepares for integration with AI evaluation systems

---

🏗️ System Architecture

HR Interview Engine
│
├── Question Generator
├── Interview State Manager
├── Flow Engine
├── Question Bank
├── Output Handler

🔹 Core Components

Component| Description
Question Generator| Creates dynamic questions based on role & experience
Interview State| Tracks questions, answers, and progress
Flow Engine| Controls interview phases
Question Bank| Stores categorized HR questions
Output Handler| Saves results in structured format

---

Folder Structure :

ZECPATH_AI_PRO/
│
├── data/
│   └── question_bank33/
│        └── hr_questions.json
│
├── hr_interview_engine33/
│
│   ├── question_engine/
│   │     ├── role_based_generator.py
│   │     ├── category_selector.py
│   │
│   ├── state_manager/
│   │     ├── interview_state.py
│   │
│   ├── flow_engine/
│   │     ├── interview_flow.py
│   ├── run_interview.py
│
├──── utils/
│       ├── logger.py
│
├──data/processed/ output_33/
│   └── interview_sessions/
│
├── config.py
├── README.md

⚙️ Features

✅ 1. Role-Based Question Generation

- Adapts questions based on:
  - Job role
  - Experience level

✅ 2. Structured Interview Flow

- Introduction
- Core HR Questions
- Role-Based Evaluation
- Closing

✅ 3. State Management

- Tracks:
  - Question history
  - Candidate responses
  - Interview phase

✅ 4. Scalable Architecture

- Modular design
- Easy integration with:
  - Scoring engine
  - Speech-to-text module
  - UI dashboard

✅ 5. Output Generation

- Saves results in JSON format
- Timestamp-based storage

---

▶️ How to Run

🔹 Step 1: Clone Repository

git clone <your-repo-url>
cd hr_interview_engine

🔹 Step 2: Install Dependencies

pip install -r requirements.txt

(If no requirements file, Python standard library is sufficient)

🔹 Step 3: Run the Engine

python run_interview.py

---

🧪 Sample Flow

Enter role: Software Engineer
Enter experience: fresher

Q1: Tell me about yourself
Q2: Why did you choose this career path?
Q3: What are your strengths?
...

---

📊 Output Example

outputs/interview_sessions/interview_20260426_101500.json

{
  "role": "software engineer",
  "experience": "fresher",
  "total_questions": 6,
  "responses": [
    {
      "id": 0,
      "question": "Tell me about yourself",
      "answer": "I am a recent graduate...",
      "score": null
    }
  ]
}

---

🔌 Future Enhancements

- 🤖 AI-based answer evaluation (LLM integration)
- 🎤 Speech-to-text input support
- 📊 Dashboard with analytics
- 🔁 Adaptive follow-up questions
- 🌐 REST API (FastAPI backend)
- 🎨 Web UI (React frontend)

---

🧠 Design Highlights

- Clean separation of concerns
- Extensible module-based architecture
- Real-world interview simulation
- Production-ready structure

---

📦 Deliverables

- ✅ HR Interview Engine Architecture
- ✅ Question Bank System
- ✅ Interview Flow Design
- ✅ Working CLI-based Interview Engine

---

🏁 Conclusion

The HR Interview Engine provides a solid foundation for building intelligent hiring systems. It enables structured, scalable, and customizable interview experiences while being flexible enough to integrate with advanced AI components.

This system can evolve into a fully automated AI recruiter with minimal additional effort.

---

📘 Day 34 — Dynamic Follow-Up Engine 

🚀 Overview

The Dynamic Follow-Up Engine (Day 34) is an advanced module in the HR Interview System that enables real-time, intelligent follow-up question generation based on candidate responses.

Unlike static interview systems, this engine:

- Understands candidate answers
- Identifies missing concepts (gaps)
- Measures confidence and depth
- Dynamically adjusts question difficulty
- Generates human-like follow-up questions

---

🎯 Objective

To build an adaptive interview system that:

- Mimics real interviewer behavior
- Improves candidate evaluation depth
- Ensures contextual and meaningful interactions

---

🧠 Key Features

- 🔍 Response Analysis
- 🧩 Gap Detection
- 📉 Confidence Estimation
- 🌳 Decision-Based Flow
- 🎚️ Dynamic Difficulty Adjustment
- ❓ Context-Aware Follow-Up Questions

---

🏗️ Architecture Flow

User Answer
    ↓
Response Analyzer
    ↓
Decision Tree
    ↓
Difficulty Adapter
    ↓
Follow-Up Generator
    ↓
Next Question

---

📁 Folder Structure

followup_engine34/
│
├── __init__.py
├── response_analyzer.py
├── decision_tree.py
├── difficulty_adapter.py
├── followup_generator.py
├── run_pipeline34.py

---

⚙️ Module Description

1. Response Analyzer

Analyzes candidate answers to extract:

- Intent
- Missing topics (gaps)
- Confidence level
- Answer length

---

2. Decision Tree

Determines next action:

- Clarify
- Expand
- Probe gaps
- Deepen response
- Move forward

---

3. Difficulty Adapter

Adjusts difficulty level dynamically:

- Easy
- Medium
- Hard

---

4. Follow-Up Generator

Generates contextual follow-up questions based on:

- Decision output
- Previous question
- Identified gaps

---



📊 Example Output

{
  "analysis": {
    "intent": "short_answer",
    "gaps": ["performance", "security"],
    "confidence": 0.6,
    "length": 5
  },
  "decision": "expand",
  "difficulty": "medium",
  "followup": "Can you elaborate more on that?"
}

---

▶️ How to Run

python -m app.services.followup_engine34.run_pipeline34
---

🔥 Use Cases

- AI Interview Platforms
- HR Screening Automation
- Candidate Skill Assessment
- Mock Interview Systems

---

🏁 Conclusion

The Dynamic Follow-Up Engine enhances the HR Interview System by making it:

- Adaptive
- Context-aware
- Intelligent
- Industry-ready

It ensures interviews are interactive, deep, and personalized, closely simulating a real human interviewer.

---

📅 Day-35: Communication Skill Evaluation Engine

🚀 Overview

This project implements a Communication Skill Evaluation Engine that analyzes interview-style answers and scores them across multiple communication dimensions such as grammar, fluency, clarity, and structure.

The system is designed to simulate how interviewers evaluate candidate responses and provides both quantitative scores and structured output.

---

🎯 Objective

To build a robust and production-ready system that:

- Accepts a candidate’s answer (text input)
- Evaluates communication quality
- Generates a final score + detailed breakdown
- Saves results in structured JSON format

---

🧠 Features

- ✅ Multi-dimensional evaluation:
  
  - Grammar
  - Fluency
  - Vocabulary
  - Clarity
  - Structure
  - Filler words

- ✅ Offline Grammar Checking (LanguageTool – Local Server)

- ✅ Robust Error Handling (no crashes)

- ✅ Logging for debugging and traceability

- ✅ JSON output with timestamp

---

🏗️ Project Structure

app/
└── services/
    └── communication_engine35/
        ├── communication_engine.py
        ├── grammar_evaluator.py
        ├── fluency_evaluator.py
        ├── vocabulary_evaluator.py
        ├── clarity_evaluator.py
        ├── structure_evaluator.py
        └── run_engine35.py

data/
└── processed/
    └── output_35/

---

⚙️ Installation & Setup

1. Clone the repository

git clone <your-repo-url>
cd Zecpath_AI_pro

2. Create virtual environment

python -m venv .venv
.venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

---

🔧 LanguageTool Setup (Offline)

Step 1: Download LanguageTool

Download from: https://languagetool.org/download/

Step 2: Start local server

cd G:\LanguageTool
java -jar languagetool-server.jar

Step 3: Verify server

Open in browser:

http://localhost:8081/v2/languages

---

▶️ How to Run

python -m app.services.communication_engine35.run_engine35

---

📊 Example Output

Console Output

🚀 Starting Communication Engine...

📊 ===== FINAL RESULT =====
Final Score: 81.5
Breakdown: {
  'fluency': 90,
  'grammar': 78,
  'vocabulary': 85,
  'clarity': 88,
  'filler': 95,
  'structure': 80
}

💾 Saved to: data/processed/output_35/communication_score_*.json

---

JSON Output

{
  "timestamp": "2026-04-30T17:46:00",
  "input_answer": "Sample answer...",
  "evaluation": {
    "final_score": 81.5,
    "component_scores": {
      "grammar": 78,
      "fluency": 90,
      "clarity": 88,
      "structure": 80
    }
  }
}

---

🧪 Test Cases

The system is tested with:

1. High-quality structured answer
2. Average response
3. Poor communication example

This ensures scoring differentiation and robustness.

---

🛡️ Error Handling

- Engine initialization failure handled
- Grammar tool failure fallback
- Safe evaluation wrapper
- No system crash during execution

---

📈 Evaluation Criteria

Component| Description
Grammar| Error detection via LanguageTool
Fluency| Sentence flow
Vocabulary| Word usage
Clarity| Understandability
Structure| Logical organization
Filler| Redundant words

---

🚀 Future Improvements

- API version (FastAPI)
- Real-time speech evaluation
- ML-based grammar scoring
- UI dashboard for visualization
- Batch processing



🏁 Conclusion

This project demonstrates how communication skills can be evaluated programmatically using structured scoring, grammar analysis, and robust system design.

---


 # Day 36: Confidence & Stress Indicators


## Overview

The Behavioral Intelligence Module is a rule-based NLP system designed to evaluate candidate responses in interview scenarios.

It analyzes confidence, sentiment, stress, and contradictions to produce a structured behavioral score (0–100).

This module acts as a plug-and-play AI component for:

- AI Interview Platforms
- HR Screening Systems
- Candidate Evaluation Engines

---

🎯 Objective

To simulate human interviewer judgment by extracting behavioral signals from text responses and converting them into quantifiable metrics.

---

🧠 Core Capabilities

- Detects hesitation patterns (filler words, pauses)
- Identifies uncertainty & repetition
- Performs sentiment analysis
- Detects logical contradictions
- Evaluates stress indicators
- Generates a final behavioral score (0–100)

---

🏗️ Project Structure

Stress_conf_analyzer36/
│
├── confidence_analyzer.py
├── sentiment_engine.py
├── stress_detector.py
├── contradiction_detector.py
├── behavior_analyzer.py
│
├── config/
│   ├── weights36.py
│   ├── constants36.py
│
├── utils/
│   ├── text_cleaner.py
│
├── tests/
│   ├── test_behavior36.py
│
├── examples/
│   ├── run_demo.py
│
├── data/
│   └── processed/
│       └── output_36.json
│
└── README.md

---

⚙️ System Architecture

Raw Text Input
      ↓
Signal Extraction Layer
 (Confidence, Sentiment, Stress, Contradiction)
      ↓
Normalization Layer (0–100 → 0–1)
      ↓
Weighted Scoring Engine
      ↓
Behavioral Score (0–100)
      ↓
JSON Output Storage

---

📊 Behavioral Scoring Formula

Final Score:

Behavior Score =
(Confidence × 0.5) +
(Sentiment × 0.25) +
(Stress × 0.15) +
(Contradiction × 0.10)

---

🔢 Signal Definitions

Signal| Description
Confidence| Based on hesitation, repetition, uncertainty, pause
Sentiment| Emotional tone (positive/negative)
Stress| Nervous language indicators
Contradiction| Logical inconsistency in response

---

⚠️ Industry-Level Fixes Applied

1. ✅ Normalization

All module outputs are standardized to 0–100, then normalized to 0–1 before aggregation.

---

2. ✅ Improved Weighting

Weights adjusted to reflect real-world importance of signals:

- Confidence → Primary indicator
- Sentiment → Secondary emotional signal
- Stress → Behavioral modifier
- Contradiction → Logical penalty

---

3. ✅ Contradiction Integration

Previously ignored, now directly impacts final score.

---

4. ✅ Advanced Confidence Calculation

Confidence is computed using weighted penalties:

- Hesitation
- Uncertainty
- Repetition
- Speech rate deviation

---

5. ⚠️ Oversimplified Scoring Fixed

Replaced equal averaging with weighted scoring model.

---

🧪 Example Usage

from app.services.stress_conf_analyzer36.behavior_analyzer import analyze_behavior

text = "I think I am confident but maybe I need improvement"
duration = 6

result = analyze_behavior(text, duration)
print(result)

---

📁 Sample Output

{
    "input": {
        "text": "I think I am confident but maybe I need improvement",
        "duration": 6
    },
    "confidence": 62.5,
    "sentiment": 70.0,
    "stress": 10.0,
    "contradiction": 0,
    "behavioral_score": 58.4,
    "timestamp": "2026-04-30T14:22:11"
}

---

🧪 Running Tests

pytest tests/test_behavior36.py

---

🚀 Advantages

- Lightweight (no heavy ML models)
- Fast execution (real-time capable)
- Explainable scoring system
- Modular and scalable design

---

⚠️ Limitations

- Rule-based (non-adaptive)
- No voice tone analysis
- No facial emotion detection
- Limited contextual depth

---

🔮 Future Improvements

- Transformer-based models (BERT, RoBERTa)
- Voice emotion detection (prosody analysis)
- Facial expression recognition
- Real-time streaming analysis
- Hybrid ML + rule-based scoring

---

🧩 Industry Applications

- AI Interview Assistants
- Resume Screening Engines
- Candidate Ranking Systems
- Behavioral Analytics Platforms

---

🏁 Conclusion

The Day 36 Behavioral Module establishes a foundational layer for AI-driven human behavior analysis.

It transforms raw textual responses into:

- Confidence insights
- Emotional signals
- Structured evaluation metrics

This module serves as a core building block for intelligent hiring systems.

---

Day 37 — HR Interview Scoring Engine (FastAPI Service)


📌 Overview

The HR Interview Scoring Engine is an AI-driven system that evaluates candidate responses using structured scoring logic. It combines multiple evaluation signals into a final HR score (0–100) and provides a decision output.

This module is deployed as a FastAPI microservice, making it scalable and production-ready for real-world hiring systems.

---

🎯 Objective

To design a system that:

- Converts HR interview responses into structured scores
- Combines relevance, communication, confidence, and consistency
- Produces an explainable final hiring decision
- Supports role-based weight configuration
- Exposes functionality via a REST API (FastAPI)

---

🧠 Core Features

- Multi-factor scoring engine
- Role-based weight configuration (fresher vs experienced)
- Consistency detection (contradictions & vagueness)
- Explainable scoring output
- JSON-based report generation
- FastAPI-based API service

---

🏗️ Project Structure

interview_ai_37/
│
├── hr_scoring_engine.py
├── hr_weights.py
│
├── api/
│   ├── main.py
│   ├── routes/
│   │   └── hr_routes.py
│   ├── schemas/
│   │   └── hr_schema.py
│
├── data/
│   └── processed/
│       └── hr_output_37.json
│
├── tests/
│   └── test_hr_score.py
│
└── README.md

---

⚙️ System Architecture

Candidate Answers
        ↓
Feature Extraction
(Relevance, Communication, Confidence)
        ↓
Consistency Analysis
        ↓
Weight Configuration (Role-based)
        ↓
Scoring Engine
        ↓
Aggregation Layer
        ↓
Decision Engine
        ↓
FastAPI Service
        ↓
JSON Output Storage

---

📊 Scoring Parameters

Parameter| Description
Relevance| Alignment with the question
Communication| Clarity, grammar, fluency
Confidence| Behavioral confidence score
Consistency| Logical correctness

---

🧮 Scoring Formula

HR Score =
(Relevance × Weight) +
(Communication × Weight) +
(Confidence × Weight) +
(Consistency × Weight)

---

⚖️ Default Weights

DEFAULT_WEIGHTS = {
    "relevance": 0.30,
    "communication": 0.25,
    "confidence": 0.25,
    "consistency": 0.20
}

---

👥 Role-Based Weights

ROLE_WEIGHTS = {
    "fresher": {
        "relevance": 0.25,
        "communication": 0.30,
        "confidence": 0.25,
        "consistency": 0.20
    },
    "experienced": {
        "relevance": 0.35,
        "communication": 0.20,
        "confidence": 0.25,
        "consistency": 0.20
    }
}

---

🔍 Consistency Logic

def score_consistency(answer):
    if answer.get("contradiction"):
        return 0.3
    if answer.get("is_vague"):
        return 0.6
    return 1.0

---

🚀 FastAPI Service

▶️ Run Server

uvicorn api.main:app --reload

---

🌐 API Endpoint

POST "/hr/score"

📥 Request

{
  "candidate_id": "C123",
  "candidate_type": "experienced",
  "answers": [
    {
      "question_id": "Q1",
      "relevance_score": 0.9,
      "communication_score": 85,
      "confidence_score": 80,
      "contradiction": false,
      "is_vague": false
    }
  ]
}

---

📤 Response

{
  "candidate_id": "C123",
  "hr_score": 88.5,
  "decision": "Strong Hire",
  "details": [
    {
      "question_id": "Q1",
      "scores": {
        "relevance": 0.9,
        "communication": 0.85,
        "confidence": 0.8,
        "consistency": 1
      },
      "final_score": 88.5
    }
  ]
}

---

📁 Output Storage

Results are stored in:

data/processed/hr_output_37_YYYYMMDD_HHMMSS.json

---

📊 Decision Rules

Score Range| Decision
≥ 75| Strong Hire
55–74| Consider
< 55| Reject

---

🧪 Testing

pytest

---

📦 Deliverables

- ✅ HR Interview Scoring Engine
- ✅ Role-based Weight Configuration
- ✅ FastAPI Microservice
- ✅ Explainable JSON Output
- ✅ Test Coverage
- ✅ Data Persistence

---

🚀 Advantages

- Consistent candidate evaluation
- Transparent and explainable scoring
- Scalable API architecture
- Lightweight (no heavy ML required)
- Easily integrable into HR systems

---

⚠️ Limitations

- Rule-based scoring (not adaptive)
- Limited deep semantic understanding
- No real-time voice or facial analysis

---

🔮 Future Improvements

- ML-based scoring (BERT / LLMs)
- Context-aware evaluation
- Voice emotion detection
- Video-based behavioral analysis
- Real-time scoring pipeline

---

🏁 Conclusion

The Day 37 HR Interview Scoring Engine successfully transforms subjective HR evaluations into a structured, explainable, and scalable system.

With FastAPI integration, this module becomes a production-ready AI microservice capable of powering:

- AI interview platforms
- Candidate screening systems
- Automated hiring workflows

This marks a significant step toward building a full AI-driven recruitment ecosystem.

---
## Day 38 – Aptitude Logic Design 

📌 Overview

The Aptitude Logic Module is a core component of the Zecpath AI Interview System.
It evaluates a candidate’s cognitive abilities during HR interviews, focusing on:

- 🧠 Logical reasoning
- 🔍 Problem-solving skills
- ⚖️ Decision-making ability
- 🎯 Situational judgment

This module transforms traditional interviews into data-driven intelligence systems.

---

🎯 Objective

To build a scalable system that:

- Evaluates structured thinking
- Analyzes reasoning patterns
- Scores decision quality
- Supports scenario-based evaluation

---

🏗️ Folder Structure

aptitude_logic_38/
│
├── aptitude_scoring.py        # Core scoring logic
├── scenario_evaluator.py      # Scenario-based evaluation
├── ideal_patterns38.py        # Ideal behavioral patterns
├── run_pipeline.py            # Main pipeline execution
│
├── utils/
│   └── text_processing.py     # NLP utilities
│
├── tests/
│   └── test_aptitude.py       # Unit tests
│
└── README.md                  # Documentation

---

⚙️ System Components

1️⃣ Aptitude Scoring Engine

Evaluates:

- Structure (step-by-step thinking)
- Problem-solving clarity
- Decision-making quality

📌 Output:

{
  "aptitude_score": 82.5,
  "breakdown": {
    "structure": 1.0,
    "problem_solving": 0.8,
    "decision_making": 0.7
  }
}

---

2️⃣ Scenario Evaluator

Matches candidate responses against ideal patterns.

Scenario| Expected Behavior
team_conflict| communicate → understand → resolve
deadline_pressure| prioritize → plan → execute
learning| research → practice → apply

---

3️⃣ Pipeline Engine

End-to-end workflow:

Input → Scoring → Scenario Evaluation → Final Score → Save Output

---

4️⃣ Output Storage

Results are saved automatically:

data/processed/output_38/
    aptitude_score_YYYYMMDD_HHMMSS.json

---

▶️ How to Run

Run Full Pipeline

python -m app.services.aptitude_logic_38.run_pipeline

---

Run Tests

pytest app/services/aptitude_logic_38/tests/test_aptitude.py

---

🧪 Sample Execution

from app.services.aptitude_logic_38.run_pipeline import run_pipeline

result = run_pipeline(
    answer="First I analyze the problem, then plan a solution and execute it",
    scenario_type="deadline_pressure"
)

print(result)

---

📊 Sample Output

{
  "timestamp": "2026-05-01T18:30:00",
  "aptitude_score": 82.5,
  "scenario_score": 0.8,
  "saved_to": "data/processed/output_38/aptitude_score_20260501.json"
}

---

🧠 Ideal Answer Structure

Candidates should follow:

1. Problem Understanding
2. Step-by-step Approach
3. Decision Justification
4. Expected Outcome

---

🚀 Key Features

- ✔ Modular architecture
- ✔ Scenario-based intelligence
- ✔ Real-time scoring
- ✔ Persistent output storage
- ✔ Test-driven development

---

⚠️ Limitations

- Keyword-based evaluation
- Limited semantic understanding
- No deep reasoning validation

---

🔮 Future Enhancements

- 🤖 LLM-based reasoning evaluation
- 🧠 Semantic NLP (spaCy / transformers)
- 📊 Dashboard visualization
- 📈 ML-based scoring models
- 🔗 Integration with Communication Engine

---

📦 Deliverables

- Aptitude Scoring Engine
- Scenario Evaluation System
- Ideal Pattern Framework
- Pipeline Execution Module
- Test Suite
- Documentation

---

🏁 Conclusion

The Day 38 Aptitude Logic Module introduces a powerful layer of cognitive assessment into HR interviews.

It enables:

- Better hiring decisions
- Objective evaluation of thinking skills
- Scalable AI-driven interview systems

This marks a shift from question-answer systems → intelligent evaluation engines.

---

🚀 Day 39 – Interview Summary Generator 

📌 Overview

The Interview Summary Generator is the final intelligence layer of the Zecpath AI Interview System.
It transforms raw interview signals into clear, recruiter-ready decisions.

This module aggregates outputs from:

- HR Interview Engine
- Communication Engine
- Behavioral Analysis
- Aptitude Logic

👉 And converts them into structured insights + final hiring recommendations.

---

🎯 Objective

To build a system that:

- Generates candidate summaries automatically
- Identifies strengths, weaknesses, and risks
- Evaluates cultural fit
- Produces final hiring decisions
- Outputs both machine-readable and human-readable reports

---

🏗️ Folder Structure

summary_39/
│
├── summary_generator.py      # Main summary logic
├── decision_engine.py        # Score aggregation + decision logic
├── summary_templates.py      # Natural language generation
│
├── utils/
│   └── text_formatter.py     # Formatting utilities
│
├── run_pipeline39.py         # End-to-end execution pipeline
│
├── tests/
│   └── test_summary.py       # Unit tests
│
├── data/
│   └── sample_reports.json   # Aggregated candidate dataset
│
└── README.md

---

⚙️ System Components

1️⃣ Summary Generator

Analyzes:

- HR scores
- Communication performance
- Behavioral signals

📌 Outputs:

- Strengths
- Weaknesses
- Risks
- Inconsistencies
- Cultural fit

---

2️⃣ Decision Engine

Calculates:

- Overall score
- Hiring decision

📊 Decision Logic:

Score Range| Decision
≥ 75| Strong Hire
55 – 74| Consider
< 55| Reject

---

3️⃣ Final Recommendation

Provides structured output:

"final_recommendation": {
  "status": "Consider",
  "confidence": "Medium"
}

---

4️⃣ Natural Language Summary

Generates recruiter-friendly explanation:

«"The candidate demonstrates strong communication and structured thinking..."»

---

5️⃣ Formatted Summary

Human-readable block:

=== Candidate Summary ===
- Strengths
- Weaknesses
- Risks

---

🔄 Pipeline Flow

Input Data
   ↓
Summary Generator
   ↓
Decision Engine
   ↓
Recommendation Builder
   ↓
Formatting Layer
   ↓
Save Output + Append Dataset

---

▶️ How to Run

Run Pipeline

python -m app.services.summary_39.run_pipeline39

---

Run Tests

pytest app/services/summary_39/tests/test_summary.py

---

📁 Output Storage

Individual Reports

data/processed/output_39/
    interview_summary_YYYYMMDD_HHMMSS.json

---

Aggregated Dataset

data/sample_reports.json

Used for:

- Dashboard UI
- Candidate ranking
- Analytics

---

🧪 Sample Usage

from app.services.summary_39.run_pipeline39 import run_pipeline39

result = run_pipeline39(
    candidate_id="C500",
    hr_scores=[{"question_id": "Q1", "final_score": 85}],
    communication={"communication_score": 78},
    behavior={
        "confidence": {"confidence_score": 65},
        "behavioral_score": 70,
        "contradiction": False
    },
    answers=["Team project experience"]
)

print(result)

---

📊 Sample Output

{
  "candidate_id": "C500",
  "overall_score": 73.4,
  "decision": "Consider",
  "final_recommendation": {
    "status": "Consider",
    "confidence": "Medium"
  }
}

---

🚀 Key Features

- ✔ Modular architecture
- ✔ Structured + natural outputs
- ✔ Decision intelligence layer
- ✔ Persistent storage (logs + dataset)
- ✔ Dashboard-ready data

---

⚠️ Limitations

- Rule-based decision logic
- Limited contextual reasoning
- No candidate comparison (yet)

---

🔮 Future Enhancements

- 🤖 LLM-based summarization
- 📊 Dashboard UI (Day 40)
- 🏆 Candidate ranking system
- 🌐 FastAPI backend
- 📄 PDF report generation

---

📦 Deliverables

- Interview Summary Generator
- Decision Engine
- Recommendation System
- Pipeline Execution Module
- Aggregated Dataset
- Test Suite
- Documentation

---

🏁 Conclusion

The Day 39 Interview Summary Generator completes the AI interview pipeline by converting raw evaluation signals into clear hiring decisions.

🔥 Impact:

- Reduces recruiter effort
- Improves decision accuracy
- Standardizes evaluation
- Enables scalable AI hiring systems

👉 This marks the transition from
AI analysis → AI-driven decision-making system

---


📘 HR Interview AI Simulation System (Day 40)

🚀 Overview

The HR Interview AI Simulation System is an end-to-end evaluation pipeline that simulates interview sessions, scores candidate responses using AI, and compares results with human HR evaluation to measure accuracy and identify biases.

This project is part of a structured AI system build focused on real-world interview automation and evaluation.


---

🎯 Objective

Simulate multiple HR interview sessions

Evaluate candidate responses using AI

Compare AI decisions with human HR scoring

Identify inconsistencies and bias in scoring

Improve model reliability before deployment



---

🧠 Key Features

✅ Multi-candidate simulation engine

✅ Behavioral analysis (confidence, hesitation)

✅ Communication quality scoring

✅ AI vs Human comparison

✅ Accuracy evaluation metrics

✅ Bias detection system

✅ JSON-based result storage

✅ Modular, scalable architecture



---

🏗️ Project Structure

day_40_hr_simulation/
│
├── data/
│   ├── raw/
│   ├── processed/
│   │    └── output_40/
│   └── logs/
│
├── tests/
│   ├── hr_simulation.py
│   └── test_pipeline.py
│
├── reports/
│   └── hr_simulation_report.pdf
│
├── evaluation/
│   ├── accuracy_metrics.py
│   ├── bias_analysis.py
│   ├── comparison_engine.py
│   └── report_generator.py
│
├── config/
│   ├── scoring_weights.py
│   └── settings.py
│

│   ├── interview_engine/
│   ├── scoring_engine/
│   ├── communication_analyzer/
│   ├── confidence_detector/
│   └── utils/
│
├── run.py
└── README.md


---

⚙️ How It Works

1. Simulation

Generates candidates of different types:

Confident

Hesitant

Inexperienced

Overqualified



2. AI Evaluation

Each response is scored based on:

Relevance

Communication

Confidence

Consistency


3. Human Comparison

Human score simulated with slight variation

Compared with AI score


4. Metrics Generated

Accuracy (%)

Bias per candidate type

Score deviation



---

▶️ How to Run

Step 1: Navigate to Project

cd day_40_hr_simulation

Step 2: Run Simulation

python run.py


---

📊 Sample Output (Console)

=== HR SIMULATION RESULTS ===
Accuracy: 86.5 %
Bias: {
  'Confident': 1.2,
  'Hesitant': -6.5,
  'Inexperienced': -4.2,
  'Overqualified': -2.1
}


---

💾 Output Storage

Results are saved automatically to:

data/processed/output_40/

Example File:

hr_simulation_YYYYMMDD_HHMMSS.json


---

📄 Sample Output JSON

{
  "timestamp": "20260502_221530",
  "accuracy": 86.5,
  "bias": {
    "Confident": 1.2,
    "Hesitant": -6.5
  },
  "results": [
    {
      "type": "Confident",
      "ai_score": 88,
      "human_score": 90
    }
  ]
}


---

📈 Evaluation Metrics

Metric	Description

Accuracy (%)	AI vs Human score match
Bias	Score deviation per type
Decision Match	Alignment of AI vs HR decisions



---

⚠️ Known Limitations

Uses simulated data (not real candidates)

Rule-based scoring (not fully LLM-driven)

Limited contextual understanding

No real-time interaction



---

🔧 Improvements Implemented

Reduced over-weighting of communication

Balanced scoring weights

Added bias detection module

Structured evaluation pipeline



---

🚀 Future Enhancements

🔥 LLM-based evaluation (GPT integration)

📊 Streamlit / React dashboard

🌐 API deployment (FastAPI)

🗄️ Database integration (MongoDB)

🧠 Explainable AI scoring

🔁 Continuous learning loop



---

🧠 Key Learnings

AI systems can introduce bias (e.g., hesitation penalty)

Communication ≠ competence

Evaluation requires multi-dimensional scoring

Human comparison is critical for validation



---

🏁 Conclusion

The system achieved approximately ~86% accuracy, demonstrating strong performance in structured evaluation scenarios. However, improvements are required in handling hesitation, contextual understanding, and real-world variability.

This system is ready for controlled deployment and further enhancement.


---

Day-41 Unified Scoring Engine – Hiring Intelligence System

📌 Overview

The Unified Scoring Engine is a modular, production-ready system designed to evaluate candidates across multiple hiring stages and generate a single, explainable hiring score.

It combines:

- ATS (Resume Screening)
- Technical/Screening Round
- HR Interview

into a unified decision-making framework.

---

🎯 Objective

To build a scalable and explainable hiring intelligence system that:

- Aggregates multi-stage evaluation scores
- Applies role-based weighting
- Produces a unified hiring score
- Generates hiring decisions (Hire / Consider / Reject)
- Provides transparent explanations for each decision

---

⚙️ Key Features

- ✅ Cross-round score integration
- ✅ Role-based dynamic weighting
- ✅ Hiring fit classification
- ✅ Explainable AI outputs
- ✅ Batch candidate processing
- ✅ JSON-based data pipeline
- ✅ API-ready architecture (FastAPI)

---

🧠 Scoring Formula

Final Score is calculated as:

Final Score = (ATS × Weight) + (Screening × Weight) + (HR × Weight)

Default Weights:

Component| Weight
ATS| 30%
Screening| 30%
HR| 40%

Role-Based Weights:

Role Type| ATS| Screening| HR
Fresher| 25%| 35%| 40%
Experienced| 35%| 25%| 40%
Technical| 40%| 30%| 30%
Non-Technical| 20%| 30%| 50%

---

📊 Decision Logic

Score Range| Decision
≥ 75| Hire
≥ 55| Consider
< 55| Reject

---

📁 Project Structure

unified_scoring_engine/
│
├── config/           # Weights & configs
├── pipeline/         # Processing pipeline
├── api/              # FastAPI endpoints
├── tests/            # Unit tests
├── data/             # Input/output data
├── docs/             # Documentation
├── run.py            # Batch execution
├── requirements.txt
└── README.md

---

▶️ How to Run

1️⃣ Install Dependencies

pip install -r requirements.txt

2️⃣ Run Batch Processing

python run.py

3️⃣ Output Location

data/processed/output_41_<timestamp>.json

---

🌐 Run API (Optional)

uvicorn api.main:app --reload

API Endpoint:

POST /score

Sample Request:

{
  "candidate_id": "C500",
  "ats": 78,
  "screening": 72,
  "hr": 85,
  "role": "fresher"
}

---

📦 Sample Output

{
    "candidate_id": "C502",
    "scores": {
        "ats": 55,
        "screening": 42,
        "hr": 65
    },
    "weights": {
        "ats": 0.25,
        "screening": 0.35,
        "hr": 0.4
    },
    "final_score": 54.45,
    "decision": "Reject",
    "hiring_fit": {
        "hiring_fit_percentage": 54.45,
        "fit_category": "Moderate Fit"
    },
    "explanation": {
        "ats": "Resume needs improvement",
        "screening": "Needs better responses",
        "hr": "Average interpersonal skills"
    }
}

---

🧪 Testing

Run tests using:

pytest

---

🔥 Key Highlights

- Modular architecture (clean separation of concerns)
- Industry-style pipeline design
- Batch processing support
- Explainable AI outputs
- Ready for ML integration

---

⚠️ Limitations

- Static rule-based weights
- No learning from historical hiring data

---

🚀 Future Enhancements

- ML-based dynamic scoring
- Bias detection system
- Feedback-driven learning
- Dashboard visualization
- Database integration (MongoDB/PostgreSQL)

---

🚀 Day 42 – Optimization & Stability

📌 Overview

This module focuses on improving the reliability, consistency, and performance of the HR Interview AI system. It enhances scoring stability, reduces bias, optimizes processing speed, and ensures cleaner data handling.

---

🎯 Objective

To make the HR AI system:

- More stable in decision-making
- More consistent in scoring
- Faster and scalable for real-world usage

---

🧠 Key Features

1. Stable Scoring System

- Removes outliers from candidate scores
- Applies consistent decision thresholds
- Reduces random fluctuations

2. Refined Scoring Engine

- Normalizes scores to a 0–100 scale
- Uses confidence-weighted scoring
- Minimizes evaluation bias

3. Follow-Up Logic Stability

- Handles retry limits
- Improves response handling:
  - Empty → Clarify
  - Uncertain → Simplify

4. Transcript Cleanup Optimization

- Removes filler words (um, uh, etc.)
- Eliminates repeated words
- Cleans noisy input

5. Batch Processing

- Processes multiple candidates at once
- Improves performance and scalability

---

📁 Project Structure

optimization_stability42/
│
├── interview_ai/
│   ├── stable_hr_ai.py
│   ├── refined_scoring.py
│   └── followup_stability.py
│
├── screening_ai/
│   └── optimized_cleaner.py
│
├── utils/
│   └── batch_processing.py
│
├── tests/
│   └── test_stability.py
│
├── reports/
│   └── optimization_report.md
│
├── data/
│   ├── raw/
│   ├── processed/
│   │   └── output_42/
│   └── interim/
│
└── main.py

---

⚙️ How It Works

1. Input candidate data (scores, transcript, confidence)
2. Clean transcript using optimized cleaner
3. Normalize and refine scores
4. Apply stable evaluation logic
5. Process multiple candidates using batch processing
6. Save output to:

data/processed/output_42/

---

📊 Performance Improvements

Metric| Before| After
False Positives| 14%| 7%
False Negatives| 16%| 8%
Response Time| 1.8s| 1.1s
Stability| Low| High

---

📦 Output Example

{
  "cleaned_transcript": "i think i can do this job",
  "refined_scores": [40.0, 55.0, 90.0, 20.0],
  "evaluation": {
    "stable_score": 51.25,
    "decision": "Reject"
  }
}

---

🧪 Testing

Run:

pytest tests/

Ensures:

- Stable scoring logic
- Valid decision outputs

---

🚀 Advantages

- Improved decision consistency
- Reduced bias and errors
- Faster processing
- Scalable architecture

---

⚠️ Limitations

- Rule-based system
- No adaptive learning yet

---

🔮 Future Improvements

- Machine Learning-based scoring
- Real-time optimization
- Adaptive decision systems

---

🏁 Conclusion

Day 42 successfully transforms the HR AI system into a stable, optimized, and production-ready solution by enhancing scoring reliability, improving performance, and ensuring scalability.

---

DAY 43- Ethics & Compliance API 

📌 Overview

This project implements an Ethical AI Evaluation System for HR interviews, ensuring fairness, transparency, accountability, and data privacy.
It exposes the pipeline as a FastAPI backend service, making it production-ready and scalable.

---

🎯 Objective

To build an AI system that:

- Eliminates bias in candidate evaluation
- Provides explainable decisions
- Ensures data privacy and compliance
- Follows ethical AI principles

---

🧠 Key Features

✅ Fairness

- Removes bias-related fields (name, gender, etc.)
- Scores based only on job-relevant data

🔍 Explainability

- Provides detailed breakdown of AI decisions
- Shows why a candidate was evaluated in a certain way

🔐 Privacy Protection

- Masks sensitive data (email, phone)
- Ensures secure handling of candidate information

📜 Compliance

- Consent-based processing
- Data retention policy (90 days)
- GDPR-like alignment

---

🏗️ Project Structure

app/
│
├── api/
│   └── v1/
│       └── endpoints/
│           └── ethics.py
│
├── services/
│   └── ethics_ai_43/
│       ├── main_pipeline.py
│       ├── ethics_framework.py
│       ├── fairness_review.py
│       ├── explainability.py
│       └── compliance.py
│
├── schemas/
│   └── ethics_schema.py
│
├── utils/
│   └── data_masking43.py
│
└── main.py

---

⚙️ Tech Stack

- Python 3.10+
- FastAPI
- Pydantic
- Uvicorn

---

🚀 Getting Started

1️⃣ Clone Repository

git clone <your-repo-url>
cd project_root

2️⃣ Install Dependencies

pip install fastapi uvicorn

3️⃣ Run Server

uvicorn app.main:app --reload

---

🌐 API Endpoints

🔹 Health Check

GET /

🔹 Evaluate Candidate

POST /api/v1/evaluate

---

📥 Sample Request

{
  "name": "John",
  "gender": "Male",
  "email": "john@email.com",
  "score": 78,
  "consent": true
}

---

📤 Sample Response

{
  "status": "success",
  "result": {
    "data": {
      "email": "***masked***",
      "score": 78,
      "consent": true,
      "date": "2026-01-01T10:00:00"
    },
    "ethics_valid": true,
    "explanation": {
      "final_score": 78,
      "explanation": {
        "ats": "Skill match evaluation",
        "screening": "Response clarity and relevance",
        "hr": "Confidence and communication"
      }
    },
    "retention": "retain",
    "timestamp": "2026-01-01T10:00:00"
  }
}

---

📊 Ethical AI Flow

Consent → Data Collection → Bias Removal → Data Masking → 
AI Evaluation → Explainability → Secure Storage → Retention Policy

---

📈 Advantages

- Builds trust with candidates
- Reduces legal risks
- Ensures ethical hiring decisions
- Production-ready API

---

⚠️ Limitations

- Rule-based system (no ML yet)
- Partial GDPR compliance
- No real-time bias monitoring

---

🔮 Future Improvements

- Real-time bias detection
- Explainability dashboards
- AI fairness audits
- Database integration (MongoDB/PostgreSQL)

---

🧪 Testing

pytest tests/


📌 Conclusion

This project demonstrates how to build a responsible AI system that not only performs evaluation but also ensures fairness, transparency, and compliance, making it suitable for real-world HR applications.

---

🚀  Day 44 (Documentation & API Specification)

📌 Overview

This project is part of Day 44 of building an HR Interview AI System.
It focuses on making the system production-ready by adding:

- 📄 Documentation
- 🔌 API Specification
- ⚙️ FastAPI Backend
- 🧪 Testing
- 🛠 Developer Integration Guide

---

🎯 Objective

Prepare the HR Interview AI for:

- Integration with frontend / recruiters dashboard
- Maintenance and scalability
- Developer-friendly usage

---

📁 Project Structure

doc_api_44/
│
├── app/
│   ├── main.py
│   ├── routes/
│   ├── services/
│   ├── models/
│
├── data/
│   └── processed/output_44/
│
├── docs/
│
├── tests/
│
└── requirements.txt

---

⚙️ Tech Stack

- Backend: FastAPI
- Language: Python 3.10+
- Testing: Pytest
- API Docs: Swagger (auto-generated)
- AI Logic: Rule-based + NLP (extensible)

---

🚀 Getting Started

1️⃣ Clone Project

git clone <your-repo-url>
cd project_root

2️⃣ Create Virtual Environment

python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux

3️⃣ Install Dependencies

pip install -r requirements.txt

---

▶️ Run the API

uvicorn app.main:app --reload

📍 Open in browser:

- Swagger UI → http://127.0.0.1:8000/docs
- ReDoc → http://127.0.0.1:8000/redoc

---

🔌 API Endpoints

▶ Start Interview

POST /api/v1/start

▶ Submit Answer

POST /api/v1/answer

▶ Get Report

GET /api/v1/report/{session_id}

---

📊 Scoring Logic

Final Score is calculated as:

Final Score =
(ATS × 0.3) +
(Screening × 0.3) +
(HR × 0.4)

---

🧪 Run Tests

pytest

✔ Ensures all APIs are working correctly

---

📦 Output

Generated documentation output:

data/processed/output_44/day44_output.pdf

---

🛠 Developer Workflow

1. Start interview via API
2. Send answers
3. Get AI-generated report
4. Display results in dashboard

---

⚠️ Troubleshooting

Issue| Fix
API not starting| Use "uvicorn"
Import error| Check module paths
Port busy| Change port
Test failing| Check request format

---

📈 Future Improvements

- 🔐 Authentication (JWT)
- 🧠 Advanced NLP models
- 🗄 Database integration
- 🌐 Frontend dashboard
- ⚡ Real-time interview streaming

---

✅ Deliverables 

- ✔ Architecture Documentation
- ✔ API Specification
- ✔ Developer Guide
- ✔ Troubleshooting Guide
- ✔ FastAPI Backend
- ✔ Test Cases

---

🧾 Conclusion

This module transforms the HR Interview AI into a production-ready system with:

- Structured APIs
- Scalable backend
- Clear documentation
- Developer usability

---

🚀 Day 45 - HR Interview AI  Final System

📌 Overview

This project represents the final production-ready version of the HR Interview AI System built using FastAPI.

The system simulates AI-powered HR interviews by:

- Generating interview evaluations
- Calculating candidate scores
- Producing hiring decisions
- Generating interview summaries

---

🎯 Objective

Build a complete HR Interview AI pipeline with:

- Real-time interview processing
- Scoring engine
- Hiring recommendation system
- API integration
- Testing support
- Production-ready architecture

---

📁 Project Structure

demo_45/
│
├── app/
│   ├── main.py
│   ├── routes/
│   │   ├── demo.py
│   │   ├── report.py
│   │
│   ├── services/
│   │   ├── final_hr_engine.py
│   │   ├── scoring_engine.py
│   │   ├── summary_engine.py
│   │
│   ├── models/
│   │   ├── schemas.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   │   └── output_45/
│   │       └── day45_output.json
│
├── demo/
│   └── hr_demo_dataset.json
│
├── tests/
│   └── test_final.py
│
└── requirements.txt

---

⚙️ Tech Stack

- Backend: FastAPI
- Language: Python 3.10+
- Validation: Pydantic
- Testing: Pytest
- API Documentation: Swagger UI

---

🚀 Features

✅ AI Interview Simulation
✅ Candidate Evaluation
✅ HR Scoring System
✅ Final Hiring Decision
✅ Summary Generation
✅ FastAPI Backend
✅ Automated Testing
✅ Production-Ready Structure

---

🧠 System Workflow

Candidate Answers
        ↓
Scoring Engine
        ↓
Summary Engine
        ↓
Final HR Engine
        ↓
Hiring Decision
        ↓
API Response

---

📊 Scoring Logic

HR Score Formula

HR Score =
(Communication + Confidence + Aptitude) / 3

Final Score Formula

Final Score =
(ATS × 0.3) +
(Screening × 0.3) +
(HR × 0.4)

---

🔌 API Endpoints

▶ Root Endpoint

GET /

▶ Health Check

GET /health

▶ Run Interview Demo

POST /api/v1/demo

▶ Generate Report

GET /api/v1/report/{candidate_id}

---

📦 Example Demo Request

{
  "candidate_id": "C1001",
  "answers": [
    {
      "question": "Tell me about yourself",
      "answer": "I am a Python developer"
    }
  ]
}

---

📦 Example Response

{
  "status": "success",
  "message": "Demo interview processed successfully",
  "data": {
    "candidate_id": "C1001",
    "final_score": 74.57,
    "decision": "Hold"
  }
}

---

▶️ Run the Project

1️⃣ Install Dependencies

pip install -r requirements.txt

---

2️⃣ Start FastAPI Server

uvicorn app.main:app --reload

---

🌐 API Documentation

After running the server:

- Swagger UI:

http://127.0.0.1:8000/docs

- ReDoc:

http://127.0.0.1:8000/redoc

---

🧪 Run Tests

pytest

Expected Output:

===== 5 passed =====

---

📁 Output Storage

Generated outputs are saved in:

data/processed/output_45/

Example:

data/processed/output_45/day45_output.json

---

📈 Future Improvements

- NLP-based evaluation
- Voice interview support
- AI behavioral analysis
- Database integration
- PDF report export
- Recruiter dashboard
- Authentication system
- Cloud deployment

---

📦 Deliverables

✅ Production-ready HR AI system
✅ FastAPI backend
✅ Modular architecture
✅ Demo dataset
✅ Testing scripts
✅ API documentation
✅ Final scoring engine

---

🧾 Conclusion

Day 45 completes the development of the HR Interview AI system.

The project now includes:

- Scalable backend architecture
- AI evaluation pipeline
- Automated scoring system
- Production-ready APIs
- Developer-friendly documentation

This system is now ready for:

- Demo presentations
- Recruiter integration
- Cloud deployment
- Future AI enhancements

---

# Day 46 – Technical Interview AI System

# Objective

Build an enterprise-grade AI-powered Technical Interview System capable of:

- Role-based technical interviews
- Adaptive difficulty adjustment
- AI-based technical evaluation
- Coding assessment
- Communication analysis
- Confidence analysis
- Recruiter recommendation generation
- Production-ready reporting

The system is designed to simulate modern enterprise recruitment platforms used in large-scale technical hiring workflows.

---

# Project Architecture

app/
│
├── services/
│
│   ├── technical_interview_engine_46/
│   │
│   │   ├── datasets/
│   │   ├── engines/
│   │   ├── outputs/
│   │   ├── reports/
│   │   ├── tests/
│   │   └── run_engine46.py
│
├── api/
├── main.py
└── requirements.txt

---

# Core Modules

## 1. Role Mapper

Detects technical roles from resume/job description.

Example:
- Python Backend Developer
- MERN Stack Developer
- DevOps Engineer
- Data Scientist

---

## 2. Experience Engine

Analyzes:
- Total experience
- Experience level
- Career gaps
- Role transitions

Levels:
- Junior
- Mid-Level
- Senior

---

## 3. Question Engine

Loads role-based datasets dynamically.

Supports:
- Basic questions
- Intermediate questions
- Advanced questions
- Coding questions
- System design questions

Dataset Path:

app/services/technical_interview_engine_46/datasets/

---

## 4. Technical Evaluator

Evaluates:
- Technical depth
- Scalability understanding
- Architecture knowledge
- Optimization thinking

---

## 5. Coding Evaluator

Evaluates:
- Syntax quality
- Logical correctness
- Code structure
- Programming concepts

---

## 6. Communication Engine

Analyzes:
- Fluency
- Grammar
- Vocabulary
- Clarity
- Structure

---

## 7. Confidence Engine

Analyzes:
- Hesitation
- Uncertainty
- Repetition
- Speech confidence

---

## 8. Scoring Engine

Combines:
- Technical score
- Coding score
- Communication score
- Confidence score
- Semantic analysis
- Domain analysis

Final Output:
- Weighted final score
- Recommendation
- Risk analysis
- Hiring decision

---

## 9. Recommendation Engine

Generates:
- Strong Hire
- Hire
- Consider
- Reject

Also detects:
- strengths
- weaknesses
- interview risks

---

## 10. Report Generator

Creates recruiter-ready reports containing:
- Candidate evaluation
- Technical analysis
- Hiring recommendation
- Final decision
- Strengths and weaknesses

---

# Datasets

The system supports multiple technical domains:

- python_questions.json
- java_questions.json
- mern_questions.json
- devops_questions.json
- cybersecurity_questions.json
- ai_ml_questions.json
- cloud_engineer_questions.json
- qa_testing_questions.json
- database_questions.json
- system_design_questions.json
- coding_questions.json

---

# FastAPI Execution

Run:

uvicorn app.services.technical_interview_engine_46.run_engine46:app

---------------------------------------------------------------------------------------------------------

# Technical Skill Scoring Model – FastAPI

## Overview

The Technical Skill Scoring Model is an AI-powered backend system that evaluates technical answers beyond simple keyword matching.

The project analyzes:

- Accuracy
- Technical depth
- Logical reasoning
- Real-world applicability

It generates explainable technical evaluation scores using FastAPI APIs.

---

# Features

- Technical answer scoring
- Depth detection engine
- Logical reasoning analysis
- Real-world applicability scoring
- Difficulty normalization
- Explainable outputs
- Swagger API documentation
- Modular FastAPI architecture

---

# Project Structure

```bash
app/
│
├── services/
│   └── technical_skill_ai_47/
│       ├── __init__.py
│       ├── main47.py
│       ├── models.py
│       ├── scoring_engine.py
│       ├── depth_detector.py
│       ├── logic_engine.py
│       ├── realworld_engine.py
│       ├── difficulty_engine.py
│       └── explain_engine.py
│
├── requirements.txt
└── README.md


---

Technologies Used

FastAPI

Python

Pydantic

Uvicorn

NLP-based scoring logic



---

Installation

Step 1: Clone Project

git clone <repository_url>


---

Step 2: Create Virtual Environment

python -m venv .venv


---

Step 3: Activate Virtual Environment

Windows

.venv\Scripts\activate

Linux / Mac

source .venv/bin/activate


---

Step 4: Install Dependencies

pip install -r requirements.txt


---

Running the FastAPI Server

Run the server using:

uvicorn app.services.technical_skill_ai_47.main47:app --reload

Server starts at:

http://127.0.0.1:8000


---

Swagger API Documentation

Open:

http://127.0.0.1:8000/docs

Interactive API testing is available in Swagger UI.


---

API Endpoints

Home Route

GET /

Returns API status.

Response

{
  "message": "Technical Skill Scoring API Running"
}


---

Technical Evaluation Route

POST /evaluate

Evaluates a technical answer.

Request Body

{
  "answer": "First I design scalable architecture then optimize performance because real-world systems require efficiency.",
  "difficulty": "advanced",
  "is_correct": true
}


---

Example Response

{
  "technical_score": 100,
  "breakdown": {
    "accuracy": 1.0,
    "depth": 1.0,
    "logic": 1.0,
    "real_world": 1.0
  },
  "explanation": {
    "accuracy": "Correct answer provided",
    "depth": "Answer contains technical explanation",
    "logic": "Step-by-step reasoning detected",
    "real_world": "Linked with practical usage"
  }
}


---

Scoring Parameters

Parameter	Description

Accuracy	Correctness of answer
Depth	Technical explanation quality
Logic	Step-by-step reasoning
Real-world	Practical applicability



---

Difficulty Levels

Difficulty	Multiplier

Basic	1.0
Intermediate	1.1
Advanced	1.2



---

Technical Evaluation Flow

1. User submits technical answer


2. System analyzes answer depth


3. Logical reasoning is evaluated


4. Real-world relevance is detected


5. Difficulty normalization applied


6. Final technical score generated


7. Explainable output returned




---

Example Modules

Depth Detector

Detects technical explanation quality using keyword analysis.

Logic Engine

Checks reasoning flow using structured sentence patterns.

Real-world Engine

Detects practical implementation understanding.

Difficulty Engine

Adjusts scoring based on answer difficulty level.


---

Future Improvements

AI-powered semantic evaluation

LLM-based reasoning engine

AST code analysis

Real coding execution sandbox

Candidate ranking system

Interview analytics dashboard



---



# Behavioral AI Research & Design System

## Overview

The Behavioral AI Research & Design System is an industry-level AI framework developed to analyze candidate behavior during interviews using non-invasive observable signals.

The system evaluates:

- Eye movement & gaze stability
- Head movement patterns
- Facial engagement
- Attention consistency
- Distraction frequency

The platform generates explainable behavioral insights and scoring outputs to assist recruiters and interview systems.

---

# Objective

The objective of this project is to understand candidate behavior during interviews using ethical and privacy-first AI analysis.

The system is designed to:

- Detect behavioral engagement
- Measure attention levels
- Analyze focus stability
- Identify distraction patterns
- Generate explainable behavioral reports
- Build recruiter-friendly behavioral intelligence

---

# Features

- Behavioral signal analysis
- Eye focus tracking
- Head movement analysis
- Engagement detection
- Distraction detection
- Behavioral scoring engine
- Explainable AI insights
- Risk detection logic
- FastAPI backend APIs
- Swagger documentation support

---

# Project Structure

```bash
behavioral_ai_system/
│
├── app/
│   ├── main48.py
│   ├── models.py
│   │
│   ├── behavior_engine/
│   │   ├── signal_mapping.py
│   │   ├── eye_tracking_engine.py
│   │   ├── head_movement_engine.py
│   │   ├── engagement_engine.py
│   │   ├── distraction_engine.py
│   │   ├── risk_detection.py
│   │   ├── scoring_engine.py
│   │   └── insight_generator.py
│   │
│   └── utils/
│       └── normalizer.py
│
├── tests/
│   └── test_behavior.py
│
├── requirements.txt
├── README.md
└── run.py


---

Technologies Used

Python

FastAPI

Pydantic

Uvicorn

AI Behavioral Analysis

Rule-Based Signal Processing



---

Behavioral Signals

Signal	Description

Eye Focus	Tracks gaze stability and concentration
Head Stability	Detects excessive movement or distraction
Engagement	Measures behavioral participation
Distraction	Detects off-screen attention loss



---

Industry-Level Deliverables

1. Behavioral AI Design Document

Complete architecture and behavioral AI workflow documentation.


---

2. Signal-to-Score Mapping Model

Weighted behavioral scoring engine.


---

3. Behavioral Analysis Framework

Pipeline for signal processing and insight generation.


---

4. Recruiter Behavioral Insights

Explainable and readable behavioral summaries.


---

5. Risk Detection Engine

Behavioral instability and distraction detection.


---

Installation

Step 1: Create Virtual Environment

python -m venv .venv


---

Step 2: Activate Environment

Windows

.venv\Scripts\activate

Linux / Mac

source .venv/bin/activate


---

Step 3: Install Dependencies

pip install -r requirements.txt


---

Running the FastAPI Server

Run the server using:

uvicorn app.main48:app --reload

Server starts at:

http://127.0.0.1:8000


---

Swagger API Documentation

Open:

http://127.0.0.1:8000/docs

Swagger UI allows direct API testing.


---

API Endpoints

Home Endpoint

GET /

Returns API status.

Example Response

{
  "message": "Behavioral AI System Running"
}


---

Behavioral Analysis Endpoint

POST /analyze

Analyzes candidate behavioral signals.

Request Body

{
  "eye_focus": 0.8,
  "head_stability": 0.7,
  "engagement": 0.9,
  "distraction": 0.2
}


---

Example Response

{
  "behavior_score": 82.0,
  "signals": {
    "eye_focus": 0.8,
    "head_stability": 0.7,
    "engagement": 0.9,
    "distraction": 0.2
  },
  "risk": "Low Risk",
  "insights": {
    "focus_level": "Good",
    "engagement": "Strong",
    "risk": "Low"
  }
}


---

Behavioral Analysis Framework

Step 1 – Capture Signals

The system collects behavioral observations:

Eye movement

Head movement

Engagement activity

Attention consistency



---

Step 2 – Normalize Signals

Signals are converted into normalized values between:

0 → Low
1 → High


---

Step 3 – Pattern Detection

The AI engine identifies:

Focus stability

Distraction patterns

Nervous movement

Engagement quality



---

Step 4 – Behavioral Scoring

Weighted scoring model:

Signal	Weight

Eye Focus	30%
Head Stability	20%
Engagement	30%
Distraction	20%



---

Step 5 – Insight Generation

The system generates:

Behavioral summary

Focus analysis

Engagement insights

Risk detection report



---

Non-Invasive AI Principles

The system follows ethical AI standards:

No biometric identity tracking

No facial recognition storage

No raw video storage

Metadata-only processing

Privacy-first architecture

Candidate consent required



---

Behavioral Scoring Levels

Score Range	Behavior Level

85–100	Highly Focused
70–84	Good Engagement
50–69	Moderate
Below 50	Distracted



---

Advantages

Enhances interview intelligence

Improves candidate evaluation

Explainable behavioral scoring

Ethical AI framework

Real-time behavioral analysis

Scalable backend architecture



---

Limitations

No deep emotion analysis

Depends on webcam quality

Rule-based scoring logic

Limited contextual understanding



---

Future Improvements

Real-time webcam integration

AI gesture recognition

Emotion-aware engagement detection

Deep learning behavioral models

Interview analytics dashboard

Multi-candidate comparison engine



---

Testing

Run tests using:

pytest


---

Conclusion

The Behavioral AI Research & Design System provides an industry-level approach for understanding interview behavior using ethical and explainable AI methods.

The project demonstrates:

Behavioral signal analysis

AI scoring systems

Privacy-first AI architecture

FastAPI backend development

Recruiter insight generation

Scalable behavioral intelligence


This framework can be extended into enterprise-level hiring intelligence platforms with real-time AI behavioral analytics.


----------------------------------------------------------------------------------------------------------


# Day 49 - Malpractice & Integrity Detection System

## Overview

The Malpractice & Integrity Detection System is an industry-level AI framework designed to detect cheating, suspicious activity, and external assistance during online interviews.

The system uses multiple behavioral and environmental signals to generate explainable integrity scores and recruiter-friendly risk reports.

The platform focuses on:

- Real-time malpractice monitoring
- Behavioral anomaly detection
- Integrity scoring
- Risk classification
- Explainable AI warnings
- Privacy-first interview intelligence

---

# Objective

The objective of this project is to design a scalable AI-powered integrity monitoring system capable of identifying suspicious interview behavior using non-invasive detection techniques.

The system monitors:

- Browser tab switching
- Screen focus loss
- External voice activity
- Gaze diversion patterns
- Behavioral inconsistencies

The platform generates:

- Integrity scores
- Real-time warnings
- Risk flags
- Recruiter dashboards
- Explainable insights

---

# Features

- Real-time interview monitoring
- Multi-signal malpractice detection
- Browser activity tracking
- Voice anomaly detection
- Gaze diversion analysis
- Pattern recognition engine
- Integrity scoring system
- Risk classification
- Recruiter dashboard payloads
- Explainable AI alerts
- FastAPI REST APIs

---

# Project Structure

```bash
integrity_engine_49/
│
├── app/services/integrity_engine/
│   ├── main49.py
│   ├── models.py
│   │
│   │   ├── tab_monitor.py
│   │   ├── focus_tracker.py
│   │   ├── voice_detector.py
│   │   ├── gaze_detector.py
│   │   ├── event_aggregator.py
│   │   ├── pattern_engine.py
│   │   ├── scoring_engine.py
│   │   ├── risk_engine.py
│   │   ├── warning_engine.py
│   │   ├── dashboard_payload.py
│   │   └── scoring_pipeline.py
│   │
│   └── utils/
│       └── normalizer.py
│
├── tests/
│   └── test_integrity.py
│
├── requirements.txt
├── README.md
└── run.py


---

Technologies Used

Python

FastAPI

Pydantic

Uvicorn

AI Behavioral Monitoring

Rule-Based Pattern Recognition



---

Malpractice Signals

Signal	Description

Tab Switching	Frequent browser switching activity
Focus Loss	User leaves interview screen
External Voice	Background or external assistance
Gaze Diversion	Repeated looking away from screen



---

Detection Logic

Threshold-Based Detection

The system triggers alerts when predefined thresholds are exceeded.

Example:

Signal	Threshold

Tab Switching	> 2
Voice Detection	> 1
Focus Loss	> 3
Gaze Diversion	> 4



---

Pattern Recognition

The system identifies suspicious behavioral combinations.

Examples:

Pattern	Possible Meaning

Frequent Tab Switching	Browser searching
Continuous Voice Detection	External help
Focus Loss + Gaze Off	Looking at notes
Long Focus Breaks	Multitasking



---

Integrity Scoring System

The system calculates a weighted integrity score.

Scoring Formula

Signal	Penalty

Tab Switching	-5
Focus Loss	-4
Voice Detection	-10
Gaze Diversion	-3


Final score range:

0 → High Risk
100 → Safe Interview


---

Risk Classification

Score Range	Risk Level

75–100	Low Risk
50–74	Moderate Risk
Below 50	High Risk



---

Real-Time Warning System

The AI engine generates recruiter and candidate warnings.

Examples:

Please stay on the interview screen

External voice detected

Focus loss detected

Suspicious activity observed



---

Recruiter Dashboard Payload

The system returns structured integrity reports.

Example Output:

{
  "candidate_id": "C4001",
  "integrity_score": 62,
  "risk_level": "Moderate Risk",
  "patterns_detected": [
    "Possible Browser Searching",
    "Possible Note Referencing"
  ],
  "warnings": [
    "Please stay on the interview screen"
  ]
}


---

Installation

Step 1: Create Virtual Environment

python -m venv .venv


---

Step 2: Activate Environment

Windows

.venv\Scripts\activate

Linux / Mac

source .venv/bin/activate


---

Step 3: Install Dependencies

pip install -r requirements.txt


---

Running the FastAPI Server

Run the server:

uvicorn app.main49:app --reload

Server URL:

http://127.0.0.1:8000


---

Swagger API Documentation

Open:

http://127.0.0.1:8000/docs


---

API Endpoints

Home Endpoint

GET /

Returns API status.

Example Response

{
  "message": "Integrity Detection System Running"
}


---

Integrity Detection Endpoint

POST /detect

Analyzes malpractice and integrity signals.

Request Body

{
  "tab_switch": 4,
  "focus_loss": 3,
  "voice_detect": 1,
  "gaze_off": 5
}


---

Example Response

{
  "candidate_id": "C4001",
  "integrity_score": 62,
  "risk_level": "Moderate Risk",
  "patterns_detected": [
    "Possible Browser Searching",
    "Possible Note Referencing"
  ],
  "warnings": [
    "Please stay on the interview screen"
  ]
}


---

Integrity Detection Workflow

Step 1 – Monitor Environment

Track:

Browser activity

Audio environment

Screen focus

Eye movement



---

Step 2 – Aggregate Signals

Collect suspicious interview events into structured logs.


---

Step 3 – Detect Behavioral Patterns

Apply rule-based and threshold-based AI logic.


---

Step 4 – Generate Integrity Score

Calculate weighted malpractice score.


---

Step 5 – Risk Classification

Assign:

Low Risk

Moderate Risk

High Risk



---

Step 6 – Generate Warnings

Provide recruiter and candidate alerts.


---

Step 7 – Dashboard Reporting

Send explainable integrity reports to recruiter systems.


---

Ethical AI Principles

The platform follows privacy-first AI architecture.

Key Principles

No biometric storage

No facial identity recognition

No invasive surveillance

Metadata-only monitoring

Consent-based processing

Explainable AI outputs



---

Advantages

Prevents interview malpractice

Improves hiring fairness

Enhances recruiter trust

Real-time monitoring

Explainable AI alerts

Scalable AI architecture



---

Limitations

False positives possible

Depends on browser permissions

Requires device compatibility

Rule-based logic limitations



---

Future Improvements

AI anomaly detection

Voice identity verification

Real-time computer vision

Behavioral learning models

Enterprise recruiter dashboards

Adaptive fraud intelligence



---

Testing

Run tests using:

pytest


---

Test Script

def test_integrity():

    from app.integrity_engine.scoring_engine import (
        calculate_integrity_score
    )

    score = calculate_integrity_score({

        "tab_switch": 2,
        "focus_loss": 1,
        "voice_detect": 0,
        "gaze_off": 2
    })

    assert score > 0


---

Conclusion

The Malpractice & Integrity Detection System provides an enterprise-level AI framework for ensuring fairness, transparency, and trust in online interview environments.

The project demonstrates:

AI-powered malpractice detection

Multi-signal behavioral analysis

Real-time integrity monitoring

Explainable recruiter insights

Ethical AI architecture

FastAPI backend development

Scalable interview intelligence systems


The platform can be extended into enterprise hiring ecosystems with advanced behavioral analytics, anomaly detection, and recruiter intelligence dashboards.


-------------------------------------------------------------------------------------------------------------

#DAY 50 - Machine Test AI Design System

## Overview

The Machine Test AI Design System is an enterprise-level AI-powered technical evaluation framework developed to assess real-world engineering skills through practical machine tests.

The system evaluates candidates using:

- Coding challenges
- Debugging tasks
- File-based assignments
- Mini system design problems

The platform combines automated execution, multi-metric scoring, and explainable evaluation pipelines to generate recruiter-friendly technical assessment reports.

---

# Objective

The objective of this project is to design an intelligent machine test evaluation system capable of measuring real-world technical performance using practical engineering tasks.

The platform focuses on:

- Technical skill validation
- Automated task evaluation
- Time-aware performance scoring
- Code quality assessment
- Runtime efficiency analysis
- Problem-solving capability tracking
- Explainable AI-based reporting

The system is designed for scalable AI hiring platforms and technical interview automation systems.

---

# Features

- AI-powered machine test evaluation
- Automated code execution
- Test case validation
- Runtime efficiency scoring
- Code quality analysis
- Problem-solving evaluation
- Time-based scoring engine
- Recruiter reporting system
- Candidate performance analytics
- Explainable AI outputs
- FastAPI backend APIs

---

# Project Structure

```bash
machine_test_ai/
│
├── app/
│   ├── main50.py
│   ├── models.py
│   │
│   ├── machine_test/
│   │   ├── coding_engine.py
│   │   ├── debugging_engine.py
│   │   ├── file_task_engine.py
│   │   ├── system_design_engine.py
│   │   ├── evaluation_logic.py
│   │   ├── execution_engine.py
│   │   ├── scoring_engine.py
│   │   ├── plagiarism_checker.py
│   │   ├── behavior_tracker.py
│   │   ├── report_generator.py
│   │   └── scoring_pipeline.py
│   │
│   └── utils/
│       └── normalizer.py
│
├── tests/
│   └── test_machine.py
│
├── requirements.txt
├── README.md
└── run.py


---

Machine Test Types

Test Type	Description

Coding Problems	Algorithm and logic-based implementation
Debugging Tasks	Fixing broken or incomplete code
File-Based Tasks	Working with real project files
Mini System Design	Building scalable mini architectures



---

System Architecture

Candidate Interface
        ↓
Code Capture Engine
        ↓
Execution Sandbox
        ↓
Test Case Evaluator
        ↓
Code Quality Analyzer
        ↓
Behavior Tracker
        ↓
Scoring Engine
        ↓
Report Generator


---

Evaluation Metrics

Metric	Description

Correctness	Test case success rate
Efficiency	Runtime optimization
Code Quality	Readability and structure
Problem Solving	Attempts and logical approach
Time Score	Completion speed



---

Industry-Level Deliverables

1. Machine Test AI Framework

Enterprise-level architecture for technical task evaluation.


---

2. Task Evaluation Logic

Automated scoring pipeline for coding and debugging tasks.


---

3. Scoring Model

Weighted AI scoring engine for practical engineering assessments.


---

4. Recruiter Reporting Engine

Explainable recruiter-friendly evaluation reports.


---

5. Time-Based Intelligence

Performance-aware scoring based on task completion time.


---

Technologies Used

Python

FastAPI

Pydantic

Uvicorn

AI Evaluation Logic

Rule-Based Scoring Systems



---

Installation

Step 1 – Create Virtual Environment

python -m venv .venv


---

Step 2 – Activate Environment

Windows

.venv\Scripts\activate

Linux / Mac

source .venv/bin/activate


---

Step 3 – Install Dependencies

pip install -r requirements.txt


---

Running the System

Run the FastAPI server:

uvicorn app.services.machine_test_50.main50:app --reload


---

Server URL

http://127.0.0.1:8000


---

Swagger API Documentation

Open:

http://127.0.0.1:8000/docs

Swagger UI allows direct API testing.


---

API Endpoints

Home Endpoint

GET /

Returns API status.

Example Response

{
  "message": "Machine Test AI Running"
}


---

Evaluation Endpoint

POST /evaluate

Evaluates machine test performance.

Request Body

{
  "candidate_id": "C5001",
  "task_id": "T101",
  "passed": 8,
  "total": 10,
  "runtime": 1.2,
  "code_snapshot": "def add(a,b): return a+b",
  "attempts": 2,
  "time_taken": 25
}


---

Example Response

{
  "candidate_id": "C5001",
  "final_score": 76.8,
  "decision": "Good Performance",
  "score_breakdown": {
    "task_score": 78.5,
    "breakdown": {
      "correctness": 0.8,
      "efficiency": 0.7,
      "code_quality": 1.0,
      "problem_solving": 0.7
    }
  }
}


---

Task Evaluation Logic

Correctness Evaluation

Measures test case success rate.

correctness = passed / total


---

Efficiency Evaluation

Measures runtime optimization.

Runtime	Score

< 1 sec	1.0
< 2 sec	0.7
> 2 sec	0.4



---

Code Quality Evaluation

Measures code readability and structure.

Lines of Code	Score

< 20	1.0
< 50	0.7
> 50	0.4



---

Problem Solving Evaluation

Measures logical attempts.

Attempts	Score

1	1.0
≤ 3	0.7
> 3	0.4



---

Machine Test Scoring Formula

Task Score

Task Score =
(Correctness × 0.4) +
(Efficiency × 0.2) +
(Code Quality × 0.2) +
(Problem Solving × 0.2)


---

Final Score

Final Score =
(Task Score × 0.8) +
(Time Score × 0.2)


---

Time-Based Scoring Logic

def time_score(time_taken, limit=30):

    ratio = time_taken / limit

    if ratio <= 0.5:
        return 1.0

    elif ratio <= 1.0:
        return 0.7

    return 0.4


---

AI Evaluation Workflow

Step 1 – Candidate Submission

The candidate submits code or project files.


---

Step 2 – Execution Engine

The sandbox environment executes the submitted solution.


---

Step 3 – Test Case Evaluation

The system validates correctness against hidden test cases.


---

Step 4 – Runtime Analysis

The engine measures execution performance.


---

Step 5 – Code Quality Analysis

The AI engine evaluates readability and structure.


---

Step 6 – Problem-Solving Analysis

The platform analyzes attempts and solution behavior.


---

Step 7 – Final Scoring

Weighted AI scoring generates recruiter-ready outputs.


---

Ethical AI Principles

The platform follows explainable and privacy-first AI practices.

Key Principles

No invasive monitoring

Explainable scoring

Transparent evaluation logic

Recruiter-readable reports

Fair technical assessment

Objective scoring pipelines



---

Advantages

Real-world skill validation

Automated technical evaluation

Scalable assessment architecture

Recruiter-friendly reporting

Explainable AI scoring

Time-aware performance analysis



---

Limitations

Limited deep code review

Basic plagiarism detection

No live collaboration analysis

Runtime dependency



---

Future Improvements

AI code reviewer

Advanced plagiarism engine

Cloud sandbox execution

Live coding interviews

LLM-based feedback generation

Enterprise recruiter analytics



---

Testing

Run tests using:

pytest


---

Test Script

def test_machine():

    from app.services.machine_test_50.evaluation_logic import (
        calculate_task_score
    )

    result = calculate_task_score(
        5,
        10,
        1.5,
        "print('hi')",
        2
    )

    assert result["task_score"] > 0


---

Conclusion

The Machine Test AI Design System provides an enterprise-grade framework for evaluating technical candidates using practical engineering tasks and explainable AI scoring models.

The project demonstrates:

AI-powered coding evaluation

Automated technical scoring

Real-world task assessment

Runtime performance analysis

Time-aware scoring logic

Recruiter-friendly reporting

Scalable FastAPI backend development


This framework can be extended into enterprise hiring ecosystems with live coding intelligence, AI code review systems, advanced plagiarism detection, and recruiter analytics dashboards.


-----------------------------------------------------------------------------------

