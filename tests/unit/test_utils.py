
import sys
sys.path.append(".") # Adds higher directory to python modules path.

from utils import create_deck

def test_length_create_deck() -> None:
    assert len(create_deck()) == 40
