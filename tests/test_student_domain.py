import pytest
from domains.student import Student

def test_gueltige_matrikelnummer_akzeptieren():
    """Testet die Validierung der Matrikelnummer."""
    student = Student(id="IU123", name="Max", lastname="Mustermann")
    assert student.id == "IU123"

def test_ungueltige_matrikelnummer_ablehnen():
    """Testet die Validierung der Matrikelnummer mit einer ungültigen Eingabe."""
    with pytest.raises(ValueError):
        Student(id="123", name="Max", lastname="Mustermann")

