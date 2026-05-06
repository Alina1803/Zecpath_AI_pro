import datetime
import pytest

from app.services.ethics_ai_43.compliance import consent_check, check_retention
from app.services.ethics_ai_43.fairness_review import remove_bias_features
from app.utils.data_masking43 import mask_data


# -------------------------------
# Test Consent Logic
# -------------------------------
def test_consent_given():
    assert consent_check(True) is True


def test_consent_not_given():
    assert consent_check(False) is False


# -------------------------------
# Test Data Retention Policy
# -------------------------------
def test_retention_within_limit():
    recent_date = datetime.datetime.now() - datetime.timedelta(days=30)
    assert check_retention(recent_date) == "retain"


def test_retention_exceeded():
    old_date = datetime.datetime.now() - datetime.timedelta(days=120)
    assert check_retention(old_date) == "delete_or_anonymize"


# -------------------------------
# Test Bias Removal
# -------------------------------
def test_remove_bias_features():
    candidate = {
        "name": "John",
        "gender": "Male",
        "age": 25,
        "score": 80
    }

    result = remove_bias_features(candidate)

    assert "name" not in result
    assert "gender" not in result
    assert "age" not in result
    assert "score" in result


# -------------------------------
# Test Data Masking
# -------------------------------
def test_mask_data():
    data = {
        "email": "test@mail.com",
        "phone": "1234567890"
    }

    masked = mask_data(data)

    assert masked["email"] == "***masked***"
    assert masked["phone"] == "***masked***"


# -------------------------------
# Edge Case Testing
# -------------------------------
def test_empty_candidate_bias_removal():
    assert remove_bias_features({}) == {}


def test_mask_data_no_sensitive_fields():
    data = {"score": 90}
    assert mask_data(data) == data