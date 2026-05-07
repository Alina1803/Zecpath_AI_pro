# ==========================================
# 🎯 CA DOMAIN CONFIG
# ==========================================

DOMAIN_NAME = "chartered_accounting"


# ==========================================
# 🎯 DEFAULT ROLES
# ==========================================

DEFAULT_ROLES = [

    "Chartered Accountant",
    "Tax Consultant",
    "Audit Manager",
    "Internal Auditor",
    "Finance Manager",
    "Accounts Manager",
    "Cost Accountant",
    "Compliance Manager",
    "Risk Analyst",
    "Chief Financial Officer"
]


# ==========================================
# 🎯 SKILL DATABASE
# ==========================================

SKILL_DATABASE = [

    # Tax
    "gst",
    "taxation",
    "income tax",
    "tds",

    # Accounting
    "accounting",
    "financial reporting",
    "cost accounting",
    "accounts payable",
    "accounts receivable",
    "bank reconciliation",

    # Audit
    "audit",
    "statutory audit",
    "internal audit",

    # Compliance
    "roc filing",
    "compliance",

    # Finance
    "financial analysis",
    "budgeting",
    "forecasting",
    "cash flow",

    # ERP / Tools
    "tally",
    "sap fico",
    "excel",
    "power bi",

    # Standards
    "ifrs",
    "gaap",

    # Reporting
    "mis reporting",
    "fp&a"
]


# ==========================================
# 🎯 SKILL SYNONYMS
# ==========================================

SKILL_SYNONYMS = {

    "gst": [
        "goods and services tax"
    ],

    "tds": [
        "tax deducted at source"
    ],

    "sap fico": [
        "sap finance",
        "sap fico module"
    ],

    "ifrs": [
        "international financial reporting standards"
    ],

    "gaap": [
        "generally accepted accounting principles"
    ],

    "fp&a": [
        "financial planning and analysis"
    ],

    "mis reporting": [
        "management information system reporting"
    ],

    "audit": [
        "auditing",
        "financial audit"
    ],

    "accounting": [
        "bookkeeping",
        "financial accounting"
    ]
}


# ==========================================
# 🎯 DOMAIN KEYWORDS
# ==========================================

DOMAIN_KEYWORDS = [

    "chartered accountant",
    "tax consultant",
    "auditor",
    "accountant",
    "finance manager",
    "financial controller"
]


# ==========================================
# 🎯 MATCH THRESHOLDS
# ==========================================

MIN_CA_SKILL_MATCH = 3

MIN_CA_MATCH_PERCENT = 10