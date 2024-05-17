
import pytest
import sys
sys.path.insert(0, '/var/www/html/retos-python-backend/nivel-2-facil/002-basic-calculator/')
from calculator import calculate


def test_calculate():
    assert calculate(2, "+", 2) == 4
    assert calculate(2, "*", 2) == 4
    assert calculate(4, "/", 2) == 2
    assert calculate(4, "/", 0) == "Can't divide by 0!"
    assert calculate(4, "-", 2) == 2
    assert calculate(4, "x", 2) == "Invalid operator"
