import pandas as pd
from typing import Optional, Set, Tuple, Type, Union

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

    color = RED  # default

    if num_unexpected_strs == 0:
        color = GREEN
    elif num_unexpected_strs <= calc_one_percent_of_records(data_frame):
        color = YELLOW

    print(f"Encountered {color}{num_unexpected_strs}{RESET} unexpected input values.")
