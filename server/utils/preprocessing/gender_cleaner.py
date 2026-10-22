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
    txt = txt.replace("N", "M")  ## Typo
    return txt


def categorize_gender(txt: str) -> str:
    """
    Categorizes a gender string into "M" (Male), "F" (Female), or None based on its content.

    Args:
        txt (str): The string to categorize.
    
    Returns:
        str: "M" for male, "F" for female, or None if the string is invalid or cannot be categorized.
    """

    # Skip null values
    if pd.isna(txt):
        return None

    txt = normalize_txt(txt)

    if txt == "M" or txt == "F":
        return txt
    elif txt != "":
        print(f"Encountered unexpected string: \"{txt}\"")
    
    return None
