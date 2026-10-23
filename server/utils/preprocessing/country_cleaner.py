import pandas as pd
import pycountry


def categorize_country(country_name: str) -> str:
    """
    Categorizes a country name string into a standardized format.

    Args:
        country_name (str): The string representing the country name to be categorized.
    
    Returns:
        str: The standardized country name if found, or "Unknown" if not found. Returns None for null values.
    """

    # Skip null values
    if pd.isna(country_name):
        return None

    try:
        if pycountry.countries.lookup(country_name).alpha_3:
            return country_name
    except LookupError:
        return "Unknown"
