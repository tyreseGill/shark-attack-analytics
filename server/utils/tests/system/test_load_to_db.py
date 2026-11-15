import pandas as pd
import subprocess
import sys
import os
from sqlalchemy import create_engine, inspect, text


def remove_unnamed_column(expected_df, result_df):
    result_df = result_df.sort_values(
        by="Unnamed: 0"
    ).reset_index(drop=True)

    expected_df = expected_df.sort_values(
        by="Unnamed: 0"
    ).reset_index(drop=True)

    return expected_df, result_df


def test_load_to_db():
    DATABASE_CONNECTION_STR = os.getenv("DATABASE_CONNECTION_STRING")

    result = subprocess.run(
        [sys.executable, "-m", "server.utils.load_to_db"],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0, result.stderr

    # Connect to database
    engine = create_engine(
        DATABASE_CONNECTION_STR
    )

    try:
        # Verify table exists
        assert inspect(engine).has_table("shark_attacks")

        expected_df = pd.read_csv(
            "server/data/processed/processed_attacks.csv"
        )

        # Verify database records
        with engine.connect() as conn:
            result_df = pd.read_sql(
                text("SELECT * FROM shark_attacks"),
                conn
            )
        
        # Verify record count
        assert len(result_df) == len(expected_df)

        expected_df, result_df = remove_unnamed_column(expected_df, result_df)

        # Verify inserted data
        pd.testing.assert_frame_equal(
            result_df.reset_index(drop=True),
            expected_df.reset_index(drop=True),
            check_dtype=False
        )
    finally:
        engine.dispose()
