import pandas as pd


ACTIVITY_KEYWORDS = {
    "Interacting with Sharks": {
        "feeding", "petting",
        "spearing", "hunting",
        "petting", "tagging",
        "teasing", "grab",
        "pull", "killing",
        "picking", "rescue",
        "removing", "reviving"
        "shooting", "watching",
        "harassing", "dragging",
        "restraining", "holding",
        "stuffing", "hauling",
        "cutting", "finning",
        "catching", "helping",
        "attempting", "attacked shark"
        "measuring", "chumming",
        "observing", "filming",
        "investigating", "gaffing",
        "hunt", "examining",
        "feeling", "harpooned",
        "restraining", "photographing",
        "hoisted", "slapped",
        "net"
    },

    "Boating": {
        "boat",
        "boating",
        "kayak",
        "canoe",
        "sailing",
        "sculling",
        "rowing",
        "yacht",
        "dinghy",
        "jet ski",
        "water-skiing",
        "paddleski",
        "on board",
        "aboard"
    },

    "Fishing": {
        "fishing", "fisherman", "angler",
        "trawling", "seining", "net",
        "angling", "oystering", "clamming",
        "hunting", "catching", "collecting fish",
        "crabbing", "collecting", "spearing",
        "spearfishing", "dynamit", "shrimping"
    },

    "Surfing": {
        "surf", "body boarding", "bodyboarding",
        "boogie", "body-boarding", "paddleski", "skimboarding",
        "kite", "paddling", "paddle boarding",
        "paddleboarding", "sup", "paddle-boarding",
    },

    "Floating/Treading Water": {
        "treading water", "floating",
        "inner tube", "raft"
    },

    "Diving": {
        "diving", "scuba",
        "dived", "dive", "diver"
    },

    "Swimming": {
        "swimming", "bathing", "bather",
    },

    "Snorkeling": {
        "snorkel"
    },

    "Wading in Shallow Water": {
        "walking", "standing",
        "wading", "treading",
        "sitting"
    },
}


def normalize_activity(activity: str) -> str:
    """
    Normalizes a string by converting it to lowercase and stripping leading/trailing whitespace.

    Args:
        activity (str): The string to normalize.
    
    Returns:
        str: The normalized string.
    """
    activity = activity.lower().strip()
    return activity


def categorize_activity(activity: str) -> str:
    """
    Categorizes an activity string into one of the predefined categories based on keywords.

    Args:
        activity (str): The activity string to categorize.

    Returns:
        str: The category of the activity, or "Other" if it doesn't match any predefined
    """

    # Skip null values
    if pd.isna(activity):
        return None

    activity = normalize_activity(activity)

    # Check for keywords in the activity string
    for category, keywords in ACTIVITY_KEYWORDS.items():
        if any(keyword in activity for keyword in keywords):
            if category == "Interacting with Sharks":
                if "shark" in activity:
                    return "Interacting with Sharks"
                else:
                    continue

            return category
            
    # if activity != "":
        # print(f"Encountered unexpected string: \"{activity}\"")

    
    return "Other"
