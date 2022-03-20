"""Module used to load data into database."""

import os

import pandas as pd
import sqlalchemy


def get_db_engine():
    try:
        url = sqlalchemy.engine.URL.create(
            drivername='mysql+pymysql',
            username=os.environ['DB_USER'],
            password=os.environ['DB_PASS'],
            host=os.environ['DB_HOST'],
            port=os.environ['DB_PORT'],
            database=os.environ['DB_NAME']
        )
    except KeyError as ke:
        print('You are missing a database connection env var.')
        print(ke.args)

    engine = sqlalchemy.create_engine(url)
    return engine


def main():
    engine = get_db_engine()


if __name__ == '__main__':
    main()
