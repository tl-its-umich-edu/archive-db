# standard libraries
import json, logging, os
from datetime import datetime

# third-party libraries
import pandas as pd
from sqlalchemy import create_engine

logger = logging.getLogger(__name__)
logging.basicConfig()

# Load config file
try:
    with open('config/env.json') as f:
        ENV = json.load(f)
except FileNotFoundError as fnfe:
    logger.error('No configuration file was found; add env.json to the config directory.')

# Initialize settings and global variables
logger.setLevel(ENV.get('LOG_LEVEL', 'DEBUG'))

OUT_DIR = ENV.get('OUT_DIR', "data")

db_params = ENV['MYSQL_DATABASE']
ENGINE = create_engine(
    f"mysql://{db_params['USER']}" + 
    f":{db_params['PASSWORD']}" + 
    f"@{db_params['HOST']}:" + 
    f"{db_params['PORT']}" + 
    f"/{db_params['DATABASE']}?charset=utf8"
)
logger.info(f"Created engine for communicating with {db_params['DATABASE']} database")


# Function(s)

def write_tables_as_csvs(out_path):
    table_names_series = pd.read_sql('SHOW TABLES', ENGINE).iloc[:, 0]
    logger.debug(table_names_series)
    for table_name in table_names_series.to_list():
        table_df = pd.read_sql(table_name, ENGINE)
        logger.debug(table_df.head())
        csv_file_path = f'{out_path}/{table_name}.csv'
        table_df.to_csv(csv_file_path, index=False)
        logger.info(f'Wrote {table_name} table to {csv_file_path}')


# Main Program

if __name__ == '__main__':
    current_str_time = datetime.now().isoformat()
    archive_dir_name = f"archive-{ENV['MYSQL_DATABASE']['DATABASE']}-{current_str_time}"
    archive_path = f'{OUT_DIR}/{archive_dir_name}'
    os.mkdir(archive_path)
    write_tables_as_csvs(archive_path)