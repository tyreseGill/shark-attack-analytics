from server.utils.preprocessing import time_cleaner

def test_null():
    assert time_cleaner.categorize_time("") == None
    
def test_invalid_input_1():
    assert time_cleaner.categorize_time("Invalid Input") == None

def test_invalid_input_2():
    assert time_cleaner.categorize_time("60h60") == None

def test_valid_input_1():
    assert time_cleaner.categorize_time("08h15") == "Morning"

def test_valid_input_2():
    assert time_cleaner.categorize_time("12h30") == "Afternoon"

def test_valid_input_3():
    assert time_cleaner.categorize_time("20h45") == "Evening"

def test_overflow():
    assert time_cleaner.categorize_time("14h49439389358543") == "Afternoon"

def test_before_midnight():
    assert time_cleaner.categorize_time("23h59") == "Night"

def test_stroke_of_midnight():
    assert time_cleaner.categorize_time("00h01") == "Night"

def test_before_morning():
    assert time_cleaner.categorize_time("04h59") == "Night"

def test_morning():
    assert time_cleaner.categorize_time("05h00") == "Morning"

def test_before_afternoon():
    assert time_cleaner.categorize_time("11h59") == "Morning"

def test_afternoon():
    assert time_cleaner.categorize_time("12h00") == "Afternoon"

def test_before_evening():
    assert time_cleaner.categorize_time("16h59") == "Afternoon"

def test_evening():
    assert time_cleaner.categorize_time("17h00") == "Evening"

def test_before_night():
    assert time_cleaner.categorize_time("20h59") == "Evening"

def test_evening():
    assert time_cleaner.categorize_time("21h00") == "Night"

def test_morning_cue_1():
    assert time_cleaner.categorize_time("breakfast") == "Morning"

def test_morning_cue_2():
    assert time_cleaner.categorize_time("morning") == "Morning"

def test_afternoon_cue_1():
    assert time_cleaner.categorize_time("lunch") == "Afternoon"

def test_afternoon_cue_2():
    assert time_cleaner.categorize_time("afternoon") == "Afternoon"

def test_evening_cue_1():
    assert time_cleaner.categorize_time("dinner") == "Evening"

def test_evening_cue_2():
    assert time_cleaner.categorize_time("evening") == "Evening"

def test_night_cue():
    assert time_cleaner.categorize_time("night") == "Night"
