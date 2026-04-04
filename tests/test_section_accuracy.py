from app.services.section_segmenter import segment_sections

def test_section_detection():
    
    text = """
    SKILLS
    Python, SQL

    EDUCATION
    B.Tech Computer Science
    """

    sections = segment_sections(text)

    assert "skills" in sections
    assert "education" in sections