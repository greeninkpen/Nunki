import os
from dotenv import load_dotenv

load_dotenv()

HOST = "127.0.0.1"
USER = "root"

PASSWORD = os.getenv("PASSWORD")
#Remember to add your mysql workbench PASSWORD to the .env PASSWORD variable

api_key = os.getenv("OPENAI_API_KEY")
#Add your personal OpenAI API KEY to the .env OPENAI_API_KEY variable

#REMEMBER TO CREATE THE .ENV FILE WITH THESE TWO VARIABLE
#AND INCLUDE THE .ENV IN .GITIGNORE SO THAT NO SENSITIVE INFO IS SHARED!!
