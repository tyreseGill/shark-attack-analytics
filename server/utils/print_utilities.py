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


def print_num_expected_strings(
    data_frame: pd.DataFrame,
    column_name: str,
    value_to_count: Optional[str] = None,
    accepted_outputs: Optional[Set[str]] = None,
    accepted_type: Optional[Union[Type, Tuple[Type, ...]]] = None,
):
    """
    Prints the number of unexpected input values in a given column of a DataFrame.

    Args:
        data_frame (pd.DataFrame): The DataFrame to analyze.
        column_name (str): The name of the column to check.
        value_to_count (Optional[str]): A specific value to count in the column. If provided
            this will count the occurrences of this value.
        accepted_outputs (Optional[Set[str]]): A set of accepted string values. If provided
            this will count the number of values in the column that are not in this set.
        accepted_type (Optional[Union[Type, Tuple[Type, ...]]]): A type or tuple of types that are considered valid for the column. If provided
            this will count the number of values in the column that are not of this type.        
    """
    selected_options = sum(
        option is not None
        for option in (value_to_count, accepted_outputs, accepted_type)
    )

    # Check that exactly one of the parameters is provided
    if selected_options == 0:
        raise Exception("Expected input for one of the parameters: value_to_count, accepted_outputs, accepted_type.")
    elif selected_options > 1:
        raise Exception("Expected input for just one of the following parameters: value_to_count, accepted_outputs, accepted_type.")

    # Count the number of unexpected strings based on the provided parameter
    if accepted_outputs is not None:
        values = data_frame[column_name]
        num_unexpected_strs = (
            values.notna() & ~values.isin(accepted_outputs)
        ).sum()
    elif value_to_count is not None:
        num_unexpected_strs = (
            data_frame[column_name] == value_to_count
        ).sum()
    else:
        values = data_frame[column_name]
        num_unexpected_strs = (
            values.notna()
            & ~values.map(lambda value: isinstance(value, accepted_type))
        ).sum()

    color = RED  # default

    if num_unexpected_strs == 0:
        color = GREEN
    elif num_unexpected_strs <= calc_one_percent_of_records(data_frame):
        color = YELLOW

    print(f"Encountered {color}{num_unexpected_strs}{RESET} unexpected input values.")
