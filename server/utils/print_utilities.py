
import pandas as pd

# Colors for CLI
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"


def calc_one_percent_of_records(data_frame: pd.DataFrame) -> float:
    """
    Calculates one percent of the total number of records in a DataFrame.

    Args:
        data_frame (pd.DataFrame): The DataFrame to analyze.
    
    Returns:
        float: One percent of the total number of records in the DataFrame.
    """
    TOTAL_NUM_RECORDS = data_frame.shape[0]
    ONE_PERCENT_OF_RECS = (1/100) * TOTAL_NUM_RECORDS
    return ONE_PERCENT_OF_RECS


def get_color(data_frame: pd.DataFrame, num_invalid_records: int) -> str:
    """
    Determines the color to use for printing based on the number of invalid records.

    Args:
        data_frame (pd.DataFrame): The DataFrame to analyze.
        num_invalid_records (int): The number of invalid records in the DataFrame.
    
    Returns:
        str: The color code to use for printing (RED, YELLOW, or GREEN).
    """
    color = RED  # default

    if num_invalid_records == 0:
        color = GREEN
    elif num_invalid_records <= calc_one_percent_of_records(data_frame):
        color = YELLOW

    return color


def print_num_empty_recs(data_frame: pd.DataFrame, column_name: str):
    """
    Prints the number of empty records in a given column of a DataFrame.

    Args:
        data_frame (pd.DataFrame): The DataFrame to analyze.
        column_name (str): The name of the column to check.
    """
    NUM_RECORDS = 6303
    num_empty_records = NUM_RECORDS - data_frame[column_name].count()
    color = get_color(data_frame, num_empty_records)
    
    print(f"Encountered {color}{num_empty_records}{RESET} null value(s).")


def print_num_expected_strings(data_frame: pd.DataFrame, column_name: str, value_to_count: str):
    """
    Prints the number of unexpected input values in a given column of a DataFrame.

    Args:
        data_frame (pd.DataFrame): The DataFrame to analyze.
        column_name (str): The name of the column to check.
        value_to_count (str): A specific value to count in the column. If provided
            this will count the occurrences of this value.  
    """
    # Count the number of unexpected strings
    num_unexpected_strs = (
        data_frame[column_name] == value_to_count
    ).sum()

    color = get_color(data_frame, num_unexpected_strs)

    print(f"Encountered {color}{num_unexpected_strs}{RESET} unexpected input value(s).")
