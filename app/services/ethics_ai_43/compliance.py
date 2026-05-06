import datetime

RETENTION_DAYS = 90

def check_retention(date_stored):
    today = datetime.datetime.now()
    diff = (today - date_stored).days

    if diff > RETENTION_DAYS:
        return "delete_or_anonymize"
    return "retain"


def consent_check(consent):
    return consent is True