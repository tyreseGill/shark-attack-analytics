import pandas as pd
import subprocess
import sys
from server.utils.database_utilities import create_connection_engine, check_table_exists, generate_df_from_db_records
from server.utils.data_frame_utilities import get_processed_data


def remove_unnamed_column(expected_df: pd.DataFrame, actual_df: pd.DataFrame):
    """
    Removes unnamed column from dataframe.

    Returns:
        pd.DataFrame: Clean dataframe without unnamed column.
    """
    actual_df = actual_df.sort_values(
        by="Unnamed: 0"
    ).reset_index(drop=True)

    expected_df = expected_df.sort_values(
        by="Unnamed: 0"
    ).reset_index(drop=True)

    return expected_df, actual_df


def test_load_to_db():
    TABLE_NAME = "test_shark_attacks"

    # Executes load_to_db.py
    result = subprocess.run(
        [sys.executable, "-m", "server.pipelines.load_to_db", "--table", TABLE_NAME],
        capture_output=True,
        text=True
    )

    # Verify output was returned without issue
    assert result.returncode == 0, result.stderr

    engine = create_connection_engine()

    try:
        # Verify table exists
        assert check_table_exists(engine, TABLE_NAME)

        # Fetches processed data from generated CSV and data loaded to database for comparison
        expected_df = get_processed_data()
        actual_df = generate_df_from_db_records(engine, TABLE_NAME)
        
        # Verify record count
        assert len(actual_df) == len(expected_df)

        expected_df, actual_df = remove_unnamed_column(expected_df, actual_df)

        # Verify inserted data
        pd.testing.assert_frame_equal(
            actual_df.reset_index(drop=True),
            expected_df.reset_index(drop=True),
            check_dtype=False
        )
    finally:
        engine.dispose()
