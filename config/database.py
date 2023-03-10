from pymongo import MongoClient, DESCENDING, ASCENDING
from dotenv import load_dotenv
import os
import urllib

load_dotenv(".env")
_host = urllib.parse.quote(os.getenv("host"))
_port = urllib.parse.quote(os.getenv("port"))
_username = urllib.parse.quote(os.getenv("user"))
_password = urllib.parse.quote(os.getenv("password"))
_database = urllib.parse.quote(os.getenv("database"))

client = MongoClient("mongodb://" + _username + ":" + _password + "@" + _host + ":" + _port + "/" + _database)

# client = MongoClient("localhost", port=27017)
