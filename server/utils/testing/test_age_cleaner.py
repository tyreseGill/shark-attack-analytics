from server.utils.preprocessing import age_cleaner

def test_null():
    assert age_cleaner.categorize_age("") == None
    
def test_invalid_input():
    assert age_cleaner.categorize_age("Invalid Input") == None

def test_negative_age():
    assert age_cleaner.categorize_age("-1") == None

def test_valid_age():
    assert age_cleaner.categorize_age("25") == 25

def test_likely_typo():
    assert age_cleaner.categorize_age("123") == None

def test_age_in_days_1():
    assert age_cleaner.categorize_age("20 days") == 0

def test_age_in_days_2():
    assert age_cleaner.categorize_age("364 days") == 1

def test_age_in_days_3():
    assert age_cleaner.categorize_age("365 days") == 1

def test_age_in_months_1():
    assert age_cleaner.categorize_age("2 months") == 0

def test_age_in_months_2():
    assert age_cleaner.categorize_age("11 months") == 1

def test_age_in_months_3():
    assert age_cleaner.categorize_age("12 months") == 1

def test_age_in_months_4():
    assert age_cleaner.categorize_age("24 months") == 2

def test_age_in_years_1():
    assert age_cleaner.categorize_age("0.4 years") == 0

def test_age_in_years_2():
    assert age_cleaner.categorize_age("0.9 years") == 1

def test_age_in_years_3():
    assert age_cleaner.categorize_age("1.1 years") == 1

def test_age_in_years_4():
    assert age_cleaner.categorize_age("2.1 years") == 2

def test_unicode_age_1():
    assert age_cleaner.categorize_activity("½") == 1

def test_unicode_age_2():
    assert age_cleaner.categorize_activity("1 ¾") == 1
