from flask import Flask, jsonify, request
from openai import OpenAI
from config import api_key

app = Flask(__name__)

@app.route("/")
def hello():
    return "it works!"

if __name__ == '__main__':
    app.run(debug=True, port=5000)



class APICall:
    def api_call(self):
        client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
        api_key=api_key,
        )

        chat_completion = client.chat.completions.create(
         messages=[{"role": "user", "content":
        "Write me a short sentense that contains at least three of the eight parts of speech for an A1 English learner"}],

        model="gpt-3.5-turbo",
        )
        return chat_completion


