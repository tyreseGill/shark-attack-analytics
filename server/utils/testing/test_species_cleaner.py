from server.utils.preprocessing import species_cleaner

def test_empty_str():
    assert species_cleaner.categorize_species("") == "Unknown"
    
def test_invalid_input():
    assert species_cleaner.categorize_species("Invalid Input") == "Unknown"

def test_valid_input_1():
    assert species_cleaner.categorize_species("White shark") == "Great White Shark"

def test_valid_input_2():
    assert species_cleaner.categorize_species("zambesi") == "Bull Shark"

def test_valid_input_3():
    assert species_cleaner.categorize_species("grey nurse") == "Sand Tiger Shark"

def test_typo_1():
    assert species_cleaner.categorize_species("Grest White Sjark") == "Great White Shark"

def test_typo_2():
    assert species_cleaner.categorize_species("Bill Sjarl") == "Bull Shark"

def test_typo_3():
    assert species_cleaner.categorize_species("tifer") == "Tiger Shark"

def test_typo_4():
    assert species_cleaner.categorize_species("Gray nurse") == "Sand Tiger Shark"
