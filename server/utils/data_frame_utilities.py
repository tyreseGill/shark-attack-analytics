import pandas as pd
import os
from pathlib import Path


RAW_FILE_PATH = os.path.normpath("../server/data/raw/attacks.csv")
PROCESSED_FILE_PATH = os.path.normpath("../server/data/processed/attacks.csv")


def get_data_path(file_path: str) -> str:
    """
    Determines the appropriate data file path to use based on the existence of a processed file.

    Args:
        file_path (str): The path to the raw data file.
    
    Returns:
        str: The path to the data file to be used (either processed or raw).
    """

    # Use the processed file if it exists and the user did not explicitly request the raw file
    if os.path.exists(PROCESSED_FILE_PATH) and PROCESSED_FILE_PATH in file_path:
        DATA_PATH = PROCESSED_FILE_PATH
    elif os.path.exists(RAW_FILE_PATH) and RAW_FILE_PATH in file_path:
        DATA_PATH = RAW_FILE_PATH
    else:
        raise FileNotFoundError(
            f"Please download the file \"attacks.csv\" from Kaggle and paste it under the folder \"{os.path.normpath("server/data/raw/")}\"."
        )

    return DATA_PATH


def get_data_frame(file_path: str="server/data/raw/attacks.csv") -> pd.DataFrame:
    """
    Reads the shark attack data from a CSV file and returns it as a pandas DataFrame.

    Args:
        file_path (str): The path to the CSV file containing the shark attacks data. Defaults to "server/data/processed/attacks.csv".

    Returns:
        pd.DataFrame: A data frame containing the shark attacks data.
    """
    DATA_PATH = get_data_path(
        os.path.normpath(file_path)  # Normalizes file path to avoid parsing errors
    )
    
    is_raw_file = RAW_FILE_PATH in DATA_PATH

    expected_columns = [
        "Date",
        "Type",
        "Country",
        "Area",
        "Location",
        "Activity",
        "Gender" if not is_raw_file else "Sex ",
        "Age",
        "Fatal" if not is_raw_file else "Fatal (Y/N)",
        "Time",
        "Species" if not is_raw_file else "Species "
    ]

    data_frame = pd.read_csv(
        DATA_PATH,
        encoding="latin1",
        usecols=expected_columns
    )

    if is_raw_file:
        data_frame = data_frame.rename(
            columns={
                "Sex ": "Gender",
                "Fatal (Y/N)": "Fatal",
                "Species ": "Species"
            }
        )

    return data_frame


def get_raw_data() -> pd.DataFrame:
    """
    Generates a data frame based on unprocessed data from CSV file.

    Returns:
        pd.DataFrame: A data frame containing unprocessed shark attack records.
    """
    data_frame = pd.read_csv(
        os.path.normpath("server/data/raw/attacks.csv")
    )
    return data_frame


def get_processed_data() -> pd.DataFrame:
    """
    Generates a data frame based on processed data from CSV file.

    Returns:
        pd.DataFrame: A data frame containing processed shark attack records.
    """
    data_frame = pd.read_csv(
        os.path.normpath("server/data/processed/attacks.csv")
    )
    return data_frame
    