STACKS = {
    "core_ca": [
        "accounting", "financial reporting", "gst",
        "taxation", "auditing", "bookkeeping"
    ],

    "tax_specialist": [
        "gst", "income tax", "direct tax",
        "indirect tax", "tax compliance", "filing"
    ],

    "audit_stack": [
        "auditing", "internal audit", "statutory audit",
        "risk management", "compliance", "sox"
    ],

    "finance_analyst": [
        "financial analysis", "forecasting", "budgeting",
        "cost accounting", "management accounting"
    ],

    "data_driven_ca": [
        "advanced excel", "power bi", "data analysis",
        "financial modeling"
    ],

    "erp_stack": [
        "sap fico", "sap", "oracle erp",
        "netsuite", "erp systems"
    ],

    "automation_stack": [
        "excel vba", "python", "sql",
        "automation", "rpa", "uipath"
    ]
}


def expand_stack(skill):
    skill = skill.lower()

    expanded = set()

    for stack_name, stack_skills in STACKS.items():
        if skill in stack_skills:
            expanded.update(stack_skills)

    return list(expanded) if expanded else [skill]