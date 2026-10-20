import pandas as pd

ACCEPTABLE_TYPES = {"Provoked", "Unprovoked", "Boating", "Seadisaster", "Questionable", "Invalid"}


def normalize_txt(txt: str) -> str:
    """
    Normalizes a string by capitalizing it, removing spaces, and replacing certain substrings.

    Args:
        txt (str): The string to normalize.
    
    Returns:
        str: The normalized string.
    """
    txt = txt.capitalize()
    txt = txt.replace(" ", "")
    
    if "Boat" in txt:
        txt = "Boating"

    return txt


def categorize_type(txt: str) -> str:
    """
    Categorizes a type string based on its content.

    Args:
        txt (str): The string to categorize.
    
    Returns:
        str: The corresponding category if a fit is found, None otherwise.
    """

    # Skip null values
    if pd.isna(txt):
        return None

    txt = normalize_txt(txt)

    if txt in ACCEPTABLE_TYPES:
        return txt
    elif txt != "":
        print(f"Encountered unexpected string: \"{txt}\"")
    
    return None
