# ==========================================
# 🎯 CA DOMAIN CONFIG (GLOBAL PROJECT)
# ==========================================

DOMAIN_NAME = "chartered_accounting"

DEFAULT_ROLES = [
    "Chartered Accountant",
    "Senior Chartered Accountant",
    "Tax Consultant",
    "Tax Manager",
    "Audit Manager",
    "Internal Auditor",
    "Financial Controller",
    "Finance Manager",
    "MIS Analyst",
    "FP&A Analyst",
    "Accounts Manager",
    "Cost Accountant",
    "Forensic Auditor",
    "Compliance Manager",
    "Treasury Manager",
    "Risk Analyst",
    "Financial Reporting Manager",
    "Business Finance Manager",
    "Virtual CFO",
    "Chief Financial Officer"
]

SKILL_DATABASE = [
    "gst", "taxation", "tds", "tally", "sap fico",
    "financial reporting", "audit", "statutory audit",
    "internal audit", "bank reconciliation",
    "accounts payable", "accounts receivable",
    "mis reporting", "budgeting", "forecasting",
    "financial analysis", "ifrs", "gaap",
    "income tax", "roc filing", "compliance",
    "excel", "power bi", "cash flow",
    "cost accounting", "variance analysis"
]

# 🔥 NEW: SYNONYMS (VERY IMPORTANT)
SKILL_SYNONYMS = {
    "gst": ["goods and services tax"],
    "tds": ["tax deducted at source"],
    "sap fico": ["sap finance", "sap fico module"],
    "ifrs": ["international financial reporting standards"],
    "gaap": ["generally accepted accounting principles"],
    "fp&a": ["financial planning and analysis"],
    "mis reporting": ["management information system reporting"]
}