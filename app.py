# if running on windows include the following three lines
# from os.path import dirname
# from sys import path
# path.insert(0, dirname(__file__))

import json
from flask import Flask, jsonify, request
from openai import OpenAI
from config import api_key

from db_utils import db_add_sentence_and_words

app = Flask(__name__)

# Welcome endpoint
@app.route("/")
def hello():
    return "it works!"



if __name__ == '__main__':
    app.run(debug=True, port=5000)



# Class to handle the OpenAI API call
class APICall:
    def api_call(self):
        client = OpenAI(

         # defaults to os.environ.get("OPENAI_API_KEY")
         api_key=api_key,
        )

        prompt = """
        Give me an example of an A1 level sentence in English with the parts of speech notated.
        Return the result in a json following this format using lowercase for every part of speech:
        {
        "sentence": "THE FULL SENTENCE",
        "elements": [
            {"word": "element1",
            "part_of_speech": "Part of speech 1"},
            {"word": "element2",
            "part_of_speech": "Part of speech 2"},
            {"word": "elementN",
            "part_of_speech": "Part of speech N"},
            ]
        }
        """

        chat_completion = client.chat.completions.create(
         messages=[{"role": "user", "content": prompt}],
         response_format={"type": "json_object"},
         model="gpt-3.5-turbo-1106",

        )
        return chat_completion


"""
had a non-subscriptable error, and fix was here: 
https://stackoverflow.com/questions/77444332/openai-python-package-error-chatcompletion-object-is-not-subscriptable
"""


@app.route('/save_phrase', methods=['POST'])
def save_phrase():
    try:
        api_call_instance = APICall()
        result = api_call_instance.api_call()
        generated_phrase = result.choices[0].message.content

        print(generated_phrase)
        sentence_data = json.loads(generated_phrase)
        sentence = sentence_data["sentence"]
        pos = sentence_data["elements"]

        print("SENTENCE: ")
        print(sentence)

        print("WORDS AND PARTS OF SPEECH: ")
        print(pos)

        # Save the sentence and pos to db
        db_add_sentence_and_words(sentence, pos)

        return jsonify(sentence_data)

    except Exception as e:
        print(f"Error processing message: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


# app.run must always go at the end of the file in order for the endpoints to 'exist'
if __name__ == '__main__':
    app.run(debug=True, port=5000)


    return jsonify({"sentence": sentence})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
