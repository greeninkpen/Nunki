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
        "Give me an example of an A1 level sentence in English with the parts of speech notated"}],

        model="gpt-3.5-turbo",
        )
        return chat_completion

api_call_instance = APICall()
result = api_call_instance.api_call()
generated_phrase = result.choices[0].message.content
#had a non-subsriptable error, and fix was here: https://stackoverflow.com/questions/77444332/openai-python-package-error-chatcompletion-object-is-not-subscriptable
print (generated_phrase)

