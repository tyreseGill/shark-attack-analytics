import pandas as pd
import subprocess


def test_data_cleaning_system():
    # Run data cleaner application
    result = subprocess.run(
        ["python", "-m", "server.utils.data_cleaner"],
        capture_output=True,
        text=True
    )

    # Verify successful application execution
    assert result.returncode == 0

    # Load generated CSV file
    df = pd.read_csv("server/data/processed/attacks.csv")

    # Verify CSV file is not empty
    assert not df.empty

    # Verify expected columns exist
    assert "Date" in df.columns
    assert "Type" in df.columns
    assert "Country" in df.columns
    assert "Area" in df.columns
    assert "Location" in df.columns
    assert "Activity" in df.columns
    assert "Gender" in df.columns
    assert "Age" in df.columns
    assert "Fatal" in df.columns
    assert "Time" in df.columns
    assert "Species" in df.columns
