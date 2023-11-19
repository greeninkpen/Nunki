from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "it works!"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
