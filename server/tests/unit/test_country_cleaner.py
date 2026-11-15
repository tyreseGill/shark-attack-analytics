from server.preprocessing import country_cleaner

def test_empty_str():
    assert country_cleaner.categorize_country("") == "Unknown"

def test_usa_1():
    assert country_cleaner.categorize_country("United States of America") == "USA"

def test_usa_2():
    assert country_cleaner.categorize_country("United States") == "USA"

def test_usa_3():
    assert country_cleaner.categorize_country("US") == "USA"

def test_atlantic_ocean():
    assert country_cleaner.categorize_country("Atlantic Ocean") == "OPEN OCEAN"

def test_pacific_ocean():
    assert country_cleaner.categorize_country("Pacific Ocean") == "OPEN OCEAN"

def test_indian_ocean():
    assert country_cleaner.categorize_country("Indian Ocean") == "OPEN OCEAN"

def test_arctic_ocean():
    assert country_cleaner.categorize_country("Arctic Ocean") == "OPEN OCEAN"

def test_southern_ocean():
    assert country_cleaner.categorize_country("Southern Ocean") == "OPEN OCEAN"

def test_sea():
    assert country_cleaner.categorize_country("Red Sea") == "OPEN OCEAN"
