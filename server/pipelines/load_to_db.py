import pandas as pd
from server.utils.database_utilities import create_connection_engine
from server.utils.data_frame_utilities import get_processed_data


def load_data(table_name: str = "shark_attacks"):
    """
    Loads the processed data to the database.
    """
    try:
        engine = create_connection_engine()
        data_frame = get_processed_data()

        data_frame.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False
        )
    finally:
        engine.dispose()


if __name__ == "__main__":
    load_data()
