from server.utils.preprocessing import activity_cleaner

def test_empty_str():
    assert activity_cleaner.categorize_activity("") == "Unknown"
    
def test_gibberish_input():
    assert activity_cleaner.categorize_activity("Gibberish Input") == "Other"

def test_interacting_with_shark():
    assert activity_cleaner.categorize_activity("Bit at an aquarium when feeding a leopard shark by hand") == "Interacting with Sharks"

def test_boating_activity():
    assert activity_cleaner.categorize_activity("Attacked by a large great white while kayaking") == "Boating"

def test_fishing_activity():
    assert activity_cleaner.categorize_activity("Got bit by a shark while trawling for clams") == "Fishing"

def test_surfing_activity():
    assert activity_cleaner.categorize_activity("Grazed by a shark after falling off surfboard") == "Surfing"

def test_floating_activity():
    assert activity_cleaner.categorize_activity("Raft attacked by multiple sharks while adrift at sea") == "Floating/Treading Water"
    
def test_diving_activity():
    assert activity_cleaner.categorize_activity("Injured by large shark while diving for lobsters") == "Diving"

def test_swimming_activity():
    assert activity_cleaner.categorize_activity("Bitten while going out for a late-night swim") == "Swimming"

def test_snorkeling_activity():
    assert activity_cleaner.categorize_activity("Attacked while snorkeling in a coral reef") == "Snorkeling"

def test_wading_activity():
    assert activity_cleaner.categorize_activity("Attacked while wading through waist deep water") == "Wading in Shallow Water"

def test_typo_1():
    assert activity_cleaner.categorize_activity("Attacked by sharks in three feet of water about ten feet from the beach") == "Wading in Shallow Water"

def test_typo_2():
    assert activity_cleaner.categorize_activity("Bit while sirfing") == "Wading in Shallow Water"

def test_multiple_activities_1():
    assert activity_cleaner.categorize_activity("Attacked while standing in water fishing.") == "Fishing"

def test_multiple_activities_2():
    assert activity_cleaner.categorize_activity("Bit on hand while attempting to remove hook from shark's mouth during boating trip") == "Boating"


