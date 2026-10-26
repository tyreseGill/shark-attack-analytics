import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

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