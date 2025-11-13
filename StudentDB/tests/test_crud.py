from src.validation import validate_student
import pytest

def test_validate_student_valid():
    student = {"name": "Tude", "age": 20, "major": "Data Science"}
    assert validate_student(student) is True

def test_validate_student_invalid_age():
    student = {"name": "Tude", "age": -1, "major": "Data Science"}
    with pytest.raises(ValueError):
        validate_student(student)
