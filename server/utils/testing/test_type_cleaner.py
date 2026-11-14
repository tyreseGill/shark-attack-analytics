
ACCEPTABLE_TYPES = {"Provoked", "Unprovoked", "Boating", "Sea Disaster", "Invalid"}

from server.utils.preprocessing import type_cleaner

def test_null():
    assert type_cleaner.categorize_type("") == "Questionable"
    
def test_invalid_input():
    assert type_cleaner.categorize_type("Invalid Input") == "Questionable"

def test_valid_input_1():
    assert type_cleaner.categorize_type("Provoked") == "Provoked"

def test_valid_input_2():
    assert type_cleaner.categorize_type("Unprovoked") == "Unprovoked"

def test_valid_input_3():
    assert type_cleaner.categorize_type("Boating") == "Boating"

def test_valid_input_4():
    assert type_cleaner.categorize_type("Sea Disaster") == "Sea Disaster"

def test_valid_input_5():
    assert type_cleaner.categorize_type("Invalid") == "Invalid"

def test_valid_input_6():
    assert type_cleaner.categorize_type("Questionable") == "Questionable"

def test_typo_1():
    assert type_cleaner.categorize_type("Prlvpked") == "Provoked"

def test_typo_2():
    assert type_cleaner.categorize_type("Unorofoled") == "Unprovoked"

def test_typo_3():
    assert type_cleaner.categorize_type("Boatijg") == "Boating"

def test_typo_4():
    assert type_cleaner.categorize_type("Sea Dksaster") == "Sea Disaster"

def test_typo_5():
    assert type_cleaner.categorize_type("Invaljd") == "Invalid"

def test_typo_6():
    assert type_cleaner.categorize_type("Questjonable") == "Questionable"