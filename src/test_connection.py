import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Read env variables from .env
load_dotenv()

def get_connection():
    # Get information from .env
    user = os.getenv("AACT_USER")
    password = os.getenv("AACT_PASSWORD")
    host = os.getenv("AACT_HOST")
    port = os.getenv("AACT_PORT")
    dbname = os.getenv("AACT_DBNAME")

    # Construct connection string
    connection_string = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"

    # Create the sql engine
    engine = create_engine(connection_string)
    return engine

def test_query():
    try:
        engine = get_connection()

        query = "SELECT nct_id, brief_title, overall_status, start_date FROM studies LIMIT 5;"

        df = pd.read_sql(query, engine)

        print("Connection successful!")
        print(df)

    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    test_query()