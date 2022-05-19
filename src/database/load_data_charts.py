from database.load_data import get_db_engine
import pandas as pd
import os


def upload_charts(root_path: str):
    conn = get_db_engine()

    res = [[root, file] for root, _, file in os.walk(root_path)][1:]
    for root, files in res[:2]:
        country = root.split('\\')[-1]
        dfs = []
        for file in files:
            path = f'{root}/{file}'.replace('\\', '/')
            df = pd.read_csv(path, sep=';')
            df['country'] = country
            df['date'] = file.rstrip('.csv')
            dfs.append(df)
        df_all = pd.concat(dfs, ignore_index=True)
        result = df_all.to_sql(f'dataset_{country}', con=conn, if_exists="replace")
        print(f"{result} rows have been affected.")


if __name__ == '__main__':
    upload_charts('../charts')
    print('done')
