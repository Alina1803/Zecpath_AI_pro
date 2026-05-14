from app.services.parsers.resume_parser import parse_resume


def test_pdf_resume_parser():

    sample_resume = """
    John Doe
    Backend Developer
    Python FastAPI SQL
    """

    result = parse_resume(sample_resume)

    assert result is not None


def test_resume_contains_skills():

    sample_resume = """
    Python FastAPI Machine Learning
    """

    result = parse_resume(sample_resume)

    assert "skills" in result