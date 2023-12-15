import os
from dotenv import load_dotenv

load_dotenv()

HOST = "127.0.0.1"
USER = "root"

PASSWORD = os.getenv("PASSWORD")
#REMEBER TO ADD YOUR OWN PASSWORD HERE!!! AND INCLUDE IN GIT IGNORE SO THAT NO SENSITIVE INFO IS SHARED!!

api_key = os.getenv("OPENAI_API_KEY")
#Add your OpenAI password here

