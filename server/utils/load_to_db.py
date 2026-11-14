import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


def load_data():
    """
    Loads the processed data to the database.
    """
    try:
        load_dotenv()

        DATABASE_CONNECTION_STR = os.getenv("DATABASE_CONNECTION_STRING")

        data_frame = pd.read_csv(
            "server/data/processed/processed_attacks.csv"
        )

        engine = create_engine(
            DATABASE_CONNECTION_STR
        )

        data_frame.to_sql(
            "shark_attacks",  # table name
            engine,
            if_exists="replace",
            index=False
        )
    finally:
        engine.dispose()

if __name__ == "__main__":
    load_data()
