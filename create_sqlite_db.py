import sqlite3
import zipfile
import argparse
from pathlib import Path

import pandas as pd


def create_sqlite_db(zip_path: Path, db_name: str):
    if not zipfile.is_zipfile(zip_path):
        print('File is not a vaild zipfile')
        exit(1)
    else:
        with zipfile.ZipFile(zip_path, 'r') as zip_file:
            connection = sqlite3.connect(db_name)
            for csv_file in zip_file.namelist():
                if csv_file.endswith('.txt') or csv_file.endswith('.csv'):
                    table_name = csv_file.replace('.csv', '').replace('.txt', '')
                    with zip_file.open(csv_file, 'r') as f:
                        for chunk in pd.read_csv(f, chunksize=1000):
                            df = pd.DataFrame(chunk)
                            df.to_sql(table_name, connection, if_exists='append', index=False)


def main():
    parser = argparse.ArgumentParser(description='loads zip file of csvs into sqlite database')
    parser.add_argument('zipfile_name', metavar='zipfile_name', type=str, help='enter a zip file name')
    parser.add_argument('db_name', metavar='db_name', type=str, help='enter a database name')

    args = parser.parse_args()
    zipfile_name = args.zipfile_name
    db_name = args.db_name
    
    zip_path = Path.cwd().joinpath(zipfile_name)
    create_sqlite_db(zip_path, db_name)
    
    
if __name__ == '__main__':
    main()