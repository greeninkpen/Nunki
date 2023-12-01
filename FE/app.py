from flask import Flask, jsonify, request
import openai
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

from BE.config import API_KEY

client = OpenAI(api_key=API_KEY,
                )
# openai.api_key = "OPENAI_API_KEY"

app = Flask(__name__)


@app.route("/")
def index():
    return


output = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user",
         "content": "Please give me an example of an A1 \
          level English sentence with the corresponding \
          parts of speech"
         }
    ]
)

print(output)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
