import re
import pandas as pd


def contains_decade(input_txt: str) -> bool:
    """
    Checks if a string contains a decade in the format "XXs".

    Args:
        input_txt (str): The string to check.
    
    Returns:
        bool: True if the string contains a decade, False otherwise.
    """
    decade_match = re.fullmatch(r"(\d{2})s", input_txt)
    return bool(decade_match)


def get_decade(txt: str) -> int | str:
    """
    Extracts the decade from a string containing an age.

    Args:
        txt (str): The string containing an age.

    Returns:
        int | str: The decade as an integer if the input is in the format "XXs", otherwise returns the original input string.
    """
    decade_match = re.fullmatch(r"(\d{2})s", txt)

    if decade_match:
        decade = int(decade_match.group(1))
        return decade + 5
    else:
        raise ValueError(f"Input string '{txt}' is not in the expected format 'XXs'.")


def contains_numbers(txt: str) -> bool:
    """
    Checks if a string contains numbers.

    Args:
        age (str): The string to check.
    
    Returns:
        bool: True if the string contains any numbers, False otherwise.
    """
    numbers  = [
        int(x) for x in re.findall(r"\d+", txt)
    ]
    return bool(numbers)


def get_average_age(txt: str) -> int | str:
    """
    Calculates the average of all numbers found in a string.

    Args:
        txt (str): The string containing numbers.
    
    Returns:
        int | str: The average of the numbers as an integer if numbers are found, otherwise returns the original input string.
    """
    numbers  = [
        int(x) for x in re.findall(r"\d+", txt)
    ]
    
    if numbers:
        return int(
            sum(numbers) / len(numbers)
        )
    else:
        raise ValueError(f"Input string '{txt}' does not contain any numbers.")


def normalize_input(input_txt: str | int) -> str:
    """
    Normalizes input by converting it to uppercase, removing spaces, and replacing certain substrings where applicable.

    Args:
        input_txt (str): The input to normalize.
    
    Returns:
        str: The normalized string.
    """
    
    if type(input_txt) is str:
        input_txt = input_txt.lower()

        if "teen" in input_txt:
            return 16

        if "months" in input_txt:
            return 1
        
        if contains_decade(input_txt):
            return get_decade(input_txt)

        if contains_numbers(input_txt):
            return get_average_age(input_txt)

    return input_txt


def categorize_age(input_txt: str | int) -> int:
    """
    Categorizes an input string or integer into an appropriate age value.

    Args:
        input_txt (str | int): The input to categorize.
    
    Returns:
        int: The categorized input as an integer.
    """

    # Skip null values
    if pd.isna(input_txt):
        return None

    input_txt = normalize_input(input_txt)

    if type(input_txt) is int:
        return input_txt

    # if input_txt.replace(" ", "") != "":
    #     print(f"Encountered unexpected string: \"{input_txt}\"")

    return None
