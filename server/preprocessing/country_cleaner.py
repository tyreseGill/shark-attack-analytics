import pandas as pd
import pycountry

ALIASES = {
    "ENGLAND": "GBR",
    "SCOTLAND": "GBR",
    "REUNION ISLAND": "REU",
    "CEYLON": "LKA",
    "CEYLON (SRI LANKA)": "LKA",
    "BURMA": "MMR",
    "FALKLAND ISLANDS": "FLK",
    "UNITED ARAB EMIRATES": "UAE",
    "TURKS & CAICOS": "TCA",
    "COLUMBIA": "COL",
    "NEVIS": "KNA",
    "GRAND CAYMAN": "CYM",
    "MEXICO": "MEX",
    "RUSSIA": "RUS",
    "MICRONESIA": "FSM",
    "TONGA": "TON",
    "WESTERN SAMOA": "WSM",
    "OKINAWA": "JPN",
    "TURKEY": "TUR",
    "NEW BRITAIN": "PNG",
    "MALDIVE ISLANDS": "MDV",
    "ANDAMAN / NICOBAR ISLANDAS": "IND",
    "NICARAGUA": "NIC",
    "CURACAO": "CUW",
    "TRINIDAD & TOBAGO": "TTO",
    "CAPE VERDE": "CPV",
    "YEMEN": "YEM",
    "EGYPT": "EGY",
    "CRETE": "GRC",
    "BRITISH NEW GUINEA": "PNG",
    "TOBAGO": "TTO",
    "ANTIGUA": "ATG",
    "ROATAN": "HND",
    "BAHREIN": "BHR",
    "Azores": "PRT",
    "REUNION": "REU",
}

NON_COUNTRIES = {
    "PERSIAN GULF", "WEST INDIES", "AFRICA",
}


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

    country_name = country_name.strip()

    is_body_of_water = country_name.endswith(("OCEAN", "SEA"))

    if country_name in NON_COUNTRIES or country_name.endswith("?") or is_body_of_water:
        return "Unknown"
    
    if country_name in ALIASES:
        return ALIASES[country_name]

    try:
        if pycountry.countries.lookup(country_name).alpha_3:
            return country_name
    except LookupError:
        return "Unknown"
