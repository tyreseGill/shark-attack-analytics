import pandas as pd
import re

# Keywords synonymous with time of day
MORNING_CUES = {"morning", "am", "a.m.", "daybreak", "dawn", "sunrise", "sunup"}
AFTERNOON_CUES = {"afternoon", "lunch", "midday", "noon", "p.m.", "pm", "daytime"}
EVENING_CUES = {"evening", "sundown", "sunset", "dusk", "evening", "twilight", "nightfall"}
NIGHT_CUES = {"night", "dark"}

TIME_FORMAT = re.compile(r"\d{1,2}[h]?\d{2}")


def extract_hour(time_txt: str) -> int:
    """
    Extracts the hour from a time string.

    Args:
        time_txt (str): The time string to extract the hour from.

    Returns:
        int: The extracted hour as an integer.
    """
    time_txt = get_time_format(time_txt)
    
    try:
        if "h" in time_txt:
            hour, _ = time_txt.split("h")
        else:
            hour = time_txt[:2]
    except Exception as e:
        print(f"Exception: {e} on {time_txt}")

    try:
        hour = int(hour)
    except ValueError:
        raise ValueError(f"Invalid hour value on \"{time_txt}\": {hour}")

    return hour


def contains_time_format(time_txt: str) -> bool:
    """
    Checks if a time string contains a valid time format.

    Args:
        time_txt (str): The time string to check.
    
    Returns:
        bool: True if a valid time format is found, False otherwise.
    """
    match_found = TIME_FORMAT.search(time_txt)
    return match_found


def get_time_format(time_txt: str) -> str:
    """
    Extracts the time format from a time string.

    Args:
        time_txt (str): The time string to extract the format from.

    Returns:
        str: The extracted time format.
    """
    match_found = TIME_FORMAT.search(time_txt)

    if match_found:
        return match_found.group(0)
    else:
        raise ValueError(f"Time string ({time_txt}) does not contain a valid time format.")


def average_hours(time_txt_1: str, time_txt_2: str) -> str:
    """
    Averages two time strings and returns the average time in a standardized format.

    Args:
        time_txt_1 (str): The first time string.
        time_txt_2 (str): The second time string.
    
    Returns:
        str: The average time in the format "HHh00" (e.g., "12h00").
    """
    time_txt_1 = time_txt_1.replace(" ", "")
    time_txt_2 = time_txt_2.replace(" ", "")

    match_found = contains_time_format(time_txt_1) and contains_time_format(time_txt_2)

    if match_found:
        hour_1 = extract_hour(time_txt_1)
        hour_2 = extract_hour(time_txt_2)
        avg_hour = str(int((hour_1 + hour_2) / 2))
        return f"{avg_hour.zfill(2)}h00"
    else:
        raise ValueError(f"Both time strings ({time_txt_1}, {time_txt_2}) must be in a valid format.")


def check_for_category_fit(time_txt: str) -> str:
    """
    Checks if a time string contains keywords that fit into specific time categories (Morning, Afternoon, Evening, Night).

    Args:
        time_txt (str): The time string to check.
    
    Returns:
        str: The corresponding time category if a fit is found, None otherwise.
    """
    # Categorize time based on presence of certain keywords
    if any(x for x in MORNING_CUES if x in time_txt):
        return "Morning"
    if any(x for x in AFTERNOON_CUES if x in time_txt):
        return "Afternoon"
    if any(x for x in EVENING_CUES if x in time_txt):
        return "Evening"
    if any(x for x in NIGHT_CUES if x in time_txt):
        return "Night"


def normalize_time_txt(time_txt: str) -> str:
    """
    Normalizes time string to a more standard format for easier processing.

    Args:
        time_txt (str): The time string to normalize.

    Returns:
        str: The normalized time string.
    """
    
    # Remove quotes, brackets, and double dashes
    time_txt = time_txt.lower()
    time_txt = time_txt.replace("\"", "")
    time_txt = time_txt.replace(">", "")
    time_txt = time_txt.replace("<", "")
    time_txt = time_txt.replace("--", "-")

    # Replace common typos
    time_txt = time_txt.replace("hoo", "h00")
    time_txt = time_txt.replace("afternon", "afternoon")

    # Replace different time formats with a standard format
    time_txt = time_txt.replace(":", "h")
    time_txt = time_txt.replace("j", "h")  # There exist typos wherein "j" is used instead of "h" to denote hours

    return time_txt


def categorize_hour(hour: int) -> str:
    """
    Categorizes an hour into a time of day category (Morning, Afternoon, Evening, Night).

    Args:
        hour (int): The hour to categorize.
    
    Returns:
        str: The corresponding time of day category.
    """
    if 5 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 17:
        return "Afternoon"
    elif 17 <= hour < 21:
        return "Evening"
    else:
        return "Night"


def categorize_time_based_on_hour(time_txt: str) -> str:
    """
    Categorizes a time string into a time of day category based on the hour.

    Args:
        time_txt (str): The time string to check.
    
    Returns:
        str: The corresponding time category if a fit is found, None otherwise.
    """
    # Categorize time based on hour if no indicatory keywords are found
    if contains_time_format(time_txt):
        contains_before = "before " in time_txt
        hour = extract_hour(time_txt)

        if contains_before:
            hour -= 1

        return categorize_hour(hour)
    else:
        return None


def categorize_time_based_on_keywords(time_txt: str) -> str:
    """
    Categorizes a time string into a time of day category based on indictory keywords.

    Args:
        time_txt (str): The time string to check.
    
    Returns:
        str: The corresponding time category if a fit is found, None otherwise.
    """
    if any(x for x in MORNING_CUES if x in time_txt):
        return "Morning"
    if any(x for x in AFTERNOON_CUES if x in time_txt):
        return "Afternoon"
    if any(x for x in EVENING_CUES if x in time_txt):
        return "Evening"
    if any(x for x in NIGHT_CUES if x in time_txt):
        return "Night"
    else:
        return None


def categorize_time(time_txt: str) -> str:
    """
    Categorizes a time string into a time of day category (Morning, Afternoon, Evening, Night) based on keywords or hour.

    Args:
        time_txt (str): The time string to categorize.
    
    Returns:
        str: The corresponding time of day category, or None if the time string is invalid or cannot be categorized.
    """

    # Skip null values
    if pd.isna(time_txt):
        return None

    # Rewrite time string to a more standard format
    normalized_time_txt = normalize_time_txt(time_txt)

    # Skip empty strings
    if len(normalized_time_txt.strip()) <= 1:
        return None
    
    category = (
        categorize_time_based_on_hour(normalized_time_txt)
        or categorize_time_based_on_keywords(normalized_time_txt)
    )

    if category:
        return category
    else:
        print(f"Encountered improper time string: \"{time_txt}\".")
        return None
