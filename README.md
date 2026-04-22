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