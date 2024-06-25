import pandas as pd
from pymango import MongoClient
from config import MONGODB_URI, MONGODB_DB_NAME, MONGODB_COLLECTION_NAME


def save_to_mongodb(df):
    """
    Saves the DataFrame to MongoDB.
    """
    client = MongoClient(MONGODB_URI)
    db = client[MONGODB_DB_NAME]
    collection = db[MONGODB_COLLECTION_NAME]

    collection.delete_many({})  # Clear existing data
    collection.insert_many(df.to_dict('records'))


if __name__ == "__main__":
    df = pd.read_csv('../data/cleaned_census_data.csv')
    save_to_mongodb(df)
