import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect, text, Engine


def get_db_connection_str() -> str:
    """
    Fetches database connection string from .env file.

    Returns:
        str: The key used to connect to a database.
    """
    load_dotenv()
    DATABASE_CONNECTION_STR = os.getenv("DATABASE_CONNECTION_STRING")

    if DATABASE_CONNECTION_STR is None:
        raise KeyError("Could not find `DATABASE_CONNECTION_STRING` in .env file.")

    return DATABASE_CONNECTION_STR


def create_connection_engine() -> Engine:
    """
    Creates an instance of the sqlalchemy engine.

    Returns:
        Engine: The engine to manage connections between the Python application and a database.
    """
    engine = create_engine(
        get_db_connection_str()
    )

    return engine


def check_table_exists(engine: Engine, table_name: str) -> bool:
    """
    Verifies if the specified table exists in the database.

    Returns:
        bool: True, if table exists. Else, False.
    """
    return inspect(engine).has_table(table_name)


def generate_df_from_db_records(engine: Engine, table_name: str) -> pd.DataFrame:
    """
    Generates a data frame based on the data from the specified table in the database.

    Returns:
        pd.DataFrame: A DataFrame containing all the records from the records from the database table.
    """
    with engine.connect() as conn:
        data_frame = pd.read_sql(
            text(f"SELECT * FROM {table_name}"),
            conn
        )
    
    return data_frame
    

