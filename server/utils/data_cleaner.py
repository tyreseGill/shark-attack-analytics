from server.utils.data_frame_utilities import get_data_frame
from server.utils.preprocessing.type_cleaner import categorize_type
from server.utils.preprocessing.country_cleaner import categorize_country
from server.utils.preprocessing.activity_cleaner import categorize_activity
from server.utils.preprocessing.gender_cleaner import categorize_gender
from server.utils.preprocessing.age_cleaner import categorize_age
from server.utils.preprocessing.fatality_cleaner import categorize_fatality
from server.utils.preprocessing.time_cleaner import categorize_time
from server.utils.preprocessing.species_cleaner import categorize_species
import pandas as pd


def clean_data() -> pd.DataFrame:
    """
    Cleans the data by applying various categorization functions to the relevant columns.

    Returns:
        pd.DataFrame: A cleaned DataFrame with categorized columns.
    """
    data_frame = get_data_frame()

    data_frame["Type"] = data_frame["Type"].apply(categorize_type)
    data_frame["Country"] = data_frame["Country"].apply(categorize_country)
    data_frame["Activity"] = data_frame["Activity"].apply(categorize_activity)
    data_frame["Gender"] = data_frame["Gender"].apply(categorize_gender)
    data_frame["Age"] = data_frame["Age"].apply(categorize_age)
    data_frame["Fatal"] = data_frame["Fatal"].apply(categorize_fatality)
    data_frame["Time"] = data_frame["Time"].apply(categorize_time)
    data_frame["Species"] = data_frame["Species"].apply(categorize_species)

    return data_frame


def generate_clean_csv():
    """
    Generates a cleaned CSV file from the raw data by applying the cleaning functions and saving the result to a specified path.
    """
    PROCESSED_DATA_PATH = "server/data/processed/attacks.csv"

    clean_data_frame = clean_data()
    clean_data_frame.to_csv(PROCESSED_DATA_PATH)


if __name__ == "__main__":
    generate_clean_csv()
