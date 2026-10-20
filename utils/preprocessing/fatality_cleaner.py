import pandas as pd


def normalize_txt(txt: str) -> str:
    """
    Normalizes a string by converting it to uppercase, removing spaces, and replacing certain substrings.

    Args:
        txt (str): The string to normalize.
    
    Returns:
        str: The normalized string.
    """
    txt = txt.upper()
    txt = txt.replace(" ", "")
    txt = txt.replace("UNKNOWN", "")
    txt = txt.replace("M", "N")
    return txt


def categorize_fatality(txt: str) -> str:
    """
    Categorizes a fatality string into "Y" (Yes), "N" (No), or None based on its content.

    Args:
        txt (str): The string to categorize.
    
    Returns:
        str: "Y" if the string indicates a fatality, "N" if it indicates no fatality, or None if the string is invalid or cannot be categorized.
    """

    # Skip null values
    if pd.isna(txt):
        return None

    txt = normalize_txt(txt)

    if txt == "Y" or txt == "N":
        return txt
    elif txt != "":
        print(f"Encountered unexpected string: \"{txt}\"")
    
    return None