from server.preprocessing import fatality_cleaner

def test_empty_str():
    assert fatality_cleaner.categorize_fatality("") == "Unknown"
    
def test_invalid_input():
    assert fatality_cleaner.categorize_fatality("Invalid Input") == "Unknown"

def test_valid_input_1():
    assert fatality_cleaner.categorize_fatality("y") == "Y"

def test_valid_input_2():
    assert fatality_cleaner.categorize_fatality("n") == "N"

def test_typo_1():
    assert fatality_cleaner.categorize_fatality("M") == "N"

def test_typo_2():
    assert fatality_cleaner.categorize_fatality("B") == "N"

def test_typo_3():
    assert fatality_cleaner.categorize_fatality("H") == "N"

def test_typo_4():
    assert fatality_cleaner.categorize_fatality("J") == "N"

def test_typo_5():
    assert fatality_cleaner.categorize_fatality("U") == "Y"

def test_typo_6():
    assert fatality_cleaner.categorize_fatality("H") == "Y"

def test_typo_7():
    assert fatality_cleaner.categorize_fatality("G") == "Y"

def test_typo_8():
    assert fatality_cleaner.categorize_fatality("T") == "Y"

