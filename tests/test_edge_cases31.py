from app.services.edge_case_31.validation.input_validator import validate_input

def test_empty_input():
    assert validate_input("") == (False, "Empty input")

def test_short_input():
    assert validate_input("a")[0] == False