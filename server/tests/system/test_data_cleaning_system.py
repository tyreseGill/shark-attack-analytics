import pandas as pd
import subprocess
from server.utils.data_frame_utilities import get_processed_data


def test_data_cleaning_system():
    # Run data cleaner application
    result = subprocess.run(
        ["python", "-m", "server.pipelines.data_cleaner"],
        capture_output=True,
        text=True
    )

    # Verify successful application execution
    assert result.returncode == 0

    # Load generated CSV file
    data_frame = get_processed_data()

    # Verify CSV file is not empty
    assert not data_frame.empty

    # Verify expected columns exist
    assert "Date" in data_frame.columns
    assert "Type" in data_frame.columns
    assert "Country" in data_frame.columns
    assert "Area" in data_frame.columns
    assert "Location" in data_frame.columns
    assert "Activity" in data_frame.columns
    assert "Gender" in data_frame.columns
    assert "Age" in data_frame.columns
    assert "Fatal" in data_frame.columns
    assert "Time" in data_frame.columns
    assert "Species" in data_frame.columns
