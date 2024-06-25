from sqlalchemy import create_engine
import pandas as pd
from config import MYSQL_DB_URI

def upload_to_sql(df, table_name):
    """
    Uploads the DataFrame to a MySQL database.
    """
    engine = create_engine(MYSQL_DB_URI)
    df.to_sql(table_name, engine, if_exists='replace', index=False)

if __name__ == "__main__":
    df = pd.read_csv('../data/cleaned_census_data.csv')
    upload_to_sql(df, 'census')
