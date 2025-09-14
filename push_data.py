import os
import sys
import json
from urllib.parse import quote_plus
from dotenv import load_dotenv
import certifi
import pandas as pd
import pymongo

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

# Load environment variables
load_dotenv()


class NetworkDataExtract:
    def __init__(self):
        """
        Initialize MongoDB client using credentials from environment variables.
        """
        try:
            username = quote_plus(os.getenv("MONGO_USER"))
            password = quote_plus(os.getenv("MONGO_PASSWORD"))
            cluster = os.getenv("MONGO_CLUSTER")
            db_name = os.getenv("MONGO_DB")

            # Build connection URI
            uri = f"mongodb+srv://{username}:{password}@{cluster}/?retryWrites=true&w=majority&appName={db_name}"

            # Setup MongoDB client with SSL cert
            self.mongo_client = pymongo.MongoClient(uri, tlsCAFile=certifi.where())
            self.db_name = db_name

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_converter(self, file_path):
        """
        Converts CSV file to list of JSON-like records.
        """
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, records, database=None, collection=None):
        """
        Insert records into MongoDB collection.
        """
        try:
            db_name = database if database else self.db_name
            db = self.mongo_client[db_name]

            if not collection:
                raise ValueError("Collection name must be provided.")

            col = db[collection]
            col.insert_many(records)
            return len(records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)

if __name__=='__main__':
    FILE_PATH="Network_Data/phisingData.csv"
    DATABASE="karan0701"
    Collection="NetworkData"
    networkobj=NetworkDataExtract()
    records=networkobj.csv_to_json_converter(file_path=FILE_PATH)
    print(records)
    no_of_records=networkobj.insert_data_mongodb(records, DATABASE, Collection)
    print(no_of_records)