import json
from pymongo import MongoClient

def load_quotes(file_path):
    client = MongoClient('your_mongo_db_connection_string')
    db = client['your_database_name']
    quotes_collection = db['quotes']

    with open(file_path, 'r', encoding='utf-8') as file:
        quotes = json.load(file)
        quotes_collection.insert_many(quotes)

def load_authors(file_path):
    client = MongoClient('your_mongo_db_connection_string')
    db = client['your_database_name']
    authors_collection = db['authors']

    with open(file_path, 'r', encoding='utf-8') as file:
        authors = json.load(file)
        authors_collection.insert_many(authors)
