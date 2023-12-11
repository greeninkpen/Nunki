from flask import Flask, jsonify, request
from openai import OpenAI
from config import api_key
from db_utils import db_add_sentence, db_add_words

app = Flask(__name__)


@app.route("/")
def hello():
    return "it works!"


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
"""
had a non-subscriptable error, and fix was here: 
https://stackoverflow.com/questions/77444332/openai-python-package-error-chatcompletion-object-is-not-subscriptable
"""
print(generated_phrase)

@app.route('/save_phrase', methods=['POST'])
def save_phrase(generated_phrase):
    try:
        client = OpenAI(
            # defaults to os.environ.get("OPENAI_API_KEY")
            api_key=api_key,
        )
        # Get the message from the request
        data = request.get_json()
        user_message = data.get("user_message")

        # Call OpenAI API to get a response
        chat_completion = client.chat.completions.create(
         messages=[{"role": "user",
                    "content": "Give me an example of an A1 level sentence in English with the parts of speech notated"}],
         model="gpt-3.5-turbo",
        )

        # Extract words and parts of speech from the API response
        # generated_phrase = chat_completion["choices"][0]["message"]["content"]
        # Assuming the format is a list of dictionaries with "word" and "part_of_speech" keys
        words_and_pos = chat_completion.get("words_and_pos", [])

        # Save the words and parts of speech to the database
        db_add_words(generated_phrase, words_and_pos)

        return jsonify({"status": "success"})

    except Exception as e:
        print(f"Error processing message: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


# @app.route('/sentence', methods=['POST'])
# def save_sentence():
#     sentence_data = request.json()
#     sentence_text = sentence_data.get('sentence')
#     #   SAVE IT TO DB using connector
#
#     if sentence_text:
#         db_add_sentence(sentence_text)
#         return jsonify({'message': 'Sentence saved successfully'}), 200
#     else:
#         return jsonify({'error': "Missing 'sentence' in request data"}), 400
#
#
# @app.route('words', methods=['POST'])
# def save_words():
#     try:
#         data = request.get_json()
#         sentence_id = data.get('sentence_id')
#         words = data.get('words')
#
#         if not (sentence_id and words):
#             return jsonify({'error': 'Missing required data'}), 400
#
#         for word_data in words:
#             word_text = word_data.get('word')
#             part_of_speech = word_data.get('part_of_speech')
#
#             if word_text and part_of_speech:
#                 db_add_words(sentence_id, word_text, part_of_speech)
#
#             else:
#                 return jsonify({'error': 'Missing required word data'}), 400
#
#         return jsonify({'message':'Words and parts of speech saved successfully'}), 200
#
#     except Exception as e:
#         print(f'Error: {e}')
#         return jsonify({'error': 'Failed to save words and parts of speech'}), 500


# app.run must always go at the end of the file in order for the endpoints to 'exist'
if __name__ == '__main__':
    app.run(debug=True, port=5000)
