"""Module used to load data into database."""

from fileinput import filename
import os

from pathlib import Path

import pandas as pd
import sqlalchemy


def get_db_engine():
    try:
        url = sqlalchemy.engine.URL.create(
            drivername="mysql+pymysql",
            username=os.environ["DB_USER"],
            password=os.environ["DB_PASS"],
            host=os.environ["DB_HOST"],
            port=os.environ["DB_PORT"],
            database=os.environ["DB_NAME"],
        )
    except KeyError as ke:
        print("You are missing a database connection env var.")
        print(ke.args)

    engine = sqlalchemy.create_engine(url)
    return engine


def upload_csv(filename, engine):
    df = pd.read_csv(filename)

    if "spotify_dataset.csv" in filename:
        df = df.drop(columns=["Index"])

    table_name = Path(filename).stem
    table_name = table_name.replace("-of-", "_")
    print(f"Inserting contents of {filename} into table {table_name}")
    result = df.to_sql(table_name, con=engine, if_exists="replace")
    print(f"{result} rows have been affected.")


def load_sql(table):
    assert table in (
        "dataset_60s",
        "dataset_70s",
        "dataset_80s",
        "dataset_90s",
        "dataset_00s",
        "dataset_10s",
        "spotify_dataset",
    )
    engine = get_db_engine()
    df = pd.read_sql(table, engine, index_col="index")
    return df


def main():
    engine = get_db_engine()
    filenames = (
        filename for filename in os.listdir("./data") if filename.endswith(".csv")
    )
    for filename in filenames:
        upload_csv(f"./data/{filename}", engine)


if __name__ == "__main__":
    main()
