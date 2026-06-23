from fastapi import FastAPI

from app.services.security_governance_55.audit_log_engine import AuditLogger

from app.services.security_governance_55.access_control import has_access

from app.services.security_governance_55.consent_manager import ConsentManager

from app.services.security_governance_55.retention_policy import RETENTION_POLICY

from app.services.security_governance_55.governance_validator import GovernanceValidator

from app.services.security_governance_55.compliance_checker import ComplianceChecker

from app.services.security_governance_55.security_report_generator import (
    SecurityReportGenerator,
)

# ==========================================
# FASTAPI APP
# ==========================================

app = FastAPI(title="Zecpath Security & AI Governance", version="55.0")


# ==========================================
# SECURITY PIPELINE
# ==========================================


class SecurityPipeline:

    def run(self, candidate):

        candidate_id = candidate.get("candidate_id", "UNKNOWN")

        role = candidate.get("role", "viewer")

        consent = ConsentManager().capture_consent(candidate_id)

        access = has_access(role, "read")

        audit = AuditLogger().log_event(
            event_type="AI_EVALUATION",
            candidate_id=candidate_id,
            data={"action": "report_access"},
        )

        governance = GovernanceValidator().validate()

        compliance = ComplianceChecker().check()

        final = {
            "candidate_id": candidate_id,
            "consent": consent,
            "access_granted": access,
            "audit_log": audit,
            "retention_policy": RETENTION_POLICY,
            "governance": governance,
            "compliance": compliance,
        }

        return SecurityReportGenerator().generate(final)


# ==========================================
# PIPELINE INSTANCE
# ==========================================

pipeline = SecurityPipeline()


# ==========================================
# HEALTH CHECK
# ==========================================


@app.get("/")
def home():

    return {"module": "Day 55 Security & AI Governance", "status": "Running"}


# ==========================================
# SECURITY VALIDATION API
# ==========================================


@app.post("/security-check")
def security_check(candidate: dict):

    return pipeline.run(candidate)
