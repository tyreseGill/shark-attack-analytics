import pandas as pd

RECOGNIZED_SHARK_SPECIES = {
    "Great White Shark": {
        "great white",
        "white shark",
    },
    "Tiger Shark": {
        "tiger"
    },
    "Bull Shark": {
        "bull",
        "zambesi",
        "zambezi"
    },
    "Oceanic Whitetip Shark": {
        "oceanic whitetip"
    },
    "Whitetip Reef Shark": {
        "whitetip reef",
        "whtietip reef",
        "white-tipped"
    },
    "Sandbar Shark": {
        "sandbar"
    },
    "Sand Tiger Shark": {
        "sand tiger",
        "grey nurse shark",
        "raggedtooth"
    },
    "Sand Shark": {
        "sand"
    },
    "Nurse Shark": {
        "nurse shark"
    },
    "Longfin Mako Shark": {
        "longfin mako"
    },
    "Shortfin Mako Shark": {
        "mako",
        "blue pointer",
        "bonita"
    },
    "Lemon Shark": {
        "lemon"
    },
    "Sixgill shark": {
        "sixgill",
        "6-gill",
        "six-gill"
    },
    "Sevengill shark": {
        "sevengill",
        "7-gill",
        "seven-gill"
    },
    "Leopard Shark": {
        "leopard"
    },
    "Angel Shark": {
        "angel"
    },
    "Silky Shark": {
        "silky"
    },
    "Goblin Shark": {
        "goblin"
    },
    "Salmon Shark": {
        "salmon"
    },
    "Port Jackson Shark": {
        "port jackson"
    },
    "Hammerhead Shark": {
        "hammerhead"
    },
    "Carpet Shark": {
        "carpet"
    },
    "Grey Reef Shark": {
        "grey reef",
        "gray reef",
        "blacktail"
    },
    "Catshark": {
        "catshark"
    },
    "Silvertip Shark": {
        "silvertip"
    },
    "Porbeagle Shark": {
        "porbeagle"
    },
    "Spinner Shark": {
        "spinner"
    },
    "Copper Shark": {
        "copper shark",
        "whaler"
    },
    "Whale Shark": {
        "whale shark"
    },
    "Basking Shark": {
        "basking"
    },
    "Galapagos Shark": {
        "galapagos"
    },
    "Blue Shark": {
        "blue shark"
    },
    "Blacktip Shark": {
        "blacktip",
        "black-tip"
    },
    "Soupfin Shark": {
        "soupfin"
    },
    "Blackfin Shark": {
        "blackfin"
    },
    "Caribbean Reef Shark": {
        "caribbean reef"
    },
    "Unspecified Reef Shark": {
        "reef"
    },
    "Dusky Shark": {
        "dusky"
    },
    "Wobbegong Shark": {
        "wobbegong"
    },
    "Dogfish": {
        "dog",
        "hound"
    },
    "Thresher Shark": {
        "thresher"
    },
    "Cookiecutter Shark": {
        "cookiecutter"
    }
}


def normalize_txt(species_name: str) -> str:
    """
    Normalizes a string by capitalizing it, removing spaces, and replacing certain substrings.

    Args:
        species_name (str): The string to normalize.
    
    Returns:
        str: The normalized string.
    """
    species_name = species_name.lower().strip()
    return species_name


def categorize_species(species_name: str) -> str:
    """
    Categorizes a species string based on its content.

    Args:
        species_name (str): The string to categorize.
    
    Returns:
        str: The corresponding species if a fit is found, None otherwise.
    """

    # Skip null values
    if pd.isna(species_name):
        return None

    species_name = normalize_txt(species_name)

    # Check for keywords in the species string
    for species, names in RECOGNIZED_SHARK_SPECIES.items():
        if any(name in species_name for name in names):
            return species
    
    return "Unknown"
