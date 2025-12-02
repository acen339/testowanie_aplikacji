import pytest
from nwd import nwd

# Testy jednostkowe (unit tests)
def test_nwd_prosta_para():
    assert nwd(8, 12) == 4

def test_nwd_liczby_pierwsze():
    assert nwd(7, 13) == 1

def test_nwd_rowne_liczby():
    assert nwd(9, 9) == 9

# Ćwiczenie: dodaj test sprawdzający działanie dla (0, 5) i (5, 0)
