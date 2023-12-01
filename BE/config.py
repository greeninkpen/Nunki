import os
from dotenv import load_dotenv

load_dotenv()

HOST = "127.0.0.1"
USER = "root"
PASSWORD = "PASSWORD"
API_KEY = os.getenv("API_KEY")
#REMEBER TO ADD YOUR OWN PASSWORD HERE!!! AND INCLUDE IN GIT IGNORE SO THAT NO SENSITIVE INFO IS SHARED!!