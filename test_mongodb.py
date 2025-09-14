from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

username = quote_plus(os.getenv("MONGO_USER"))
password = quote_plus(os.getenv("MONGO_PASSWORD"))
cluster = os.getenv("MONGO_CLUSTER")
db_name = os.getenv("MONGO_DB")

# Build URI with f-string
uri = f"mongodb+srv://{username}:{password}@{cluster}/?retryWrites=true&w=majority&appName={db_name}"

client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
