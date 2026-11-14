from server.utils.preprocessing import gender_cleaner

def test_null():
    assert gender_cleaner.categorize_gender("") == "Unknown"
    
def test_invalid_input():
    assert gender_cleaner.categorize_gender("Invalid Input") == "Unknown"

def test_valid_input_1():
    assert gender_cleaner.categorize_gender("m") == "M"

def test_valid_input_2():
    assert gender_cleaner.categorize_gender("f") == "F"

def test_typo_1():
    assert fatality_cleaner.categorize_fatality("n") == "M"

def test_typo_2():
    assert fatality_cleaner.categorize_fatality("j") == "M"

def test_typo_3():
    assert fatality_cleaner.categorize_fatality("k") == "M"

def test_typo_4():
    assert fatality_cleaner.categorize_fatality(",") == "M"

def test_typo_5():
    assert fatality_cleaner.categorize_fatality("d") == "F"

def test_typo_6():
    assert fatality_cleaner.categorize_fatality("r") == "F"

def test_typo_7():
    assert fatality_cleaner.categorize_fatality("t") == "F"

def test_typo_8():
    assert fatality_cleaner.categorize_fatality("g") == "F"

def test_typo_7():
    assert fatality_cleaner.categorize_fatality("c") == "F"

def test_typo_8():
    assert fatality_cleaner.categorize_fatality("v") == "F"
