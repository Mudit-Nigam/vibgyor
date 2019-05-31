from flask import Flask, request, jsonify
from flask_cors import CORS
from neural_api import API

# Initialize the Flask application
app = Flask(__name__)
CORS(app) # allow everything by default
neural_api = API()


# default
@app.route('/')
def index():
    return "Home page."


# HTTP Errors handlers
@app.errorhandler(404)
def url_error(e):
    return """
    Error resource not found. Check the URL.
    <pre>{}</pre>""".format(e), 404


@app.errorhandler(500)
def server_error(e):
    return """
    An internal server error occurred: <pre>{}</pre>
    Check the logs (if any?) for issues.
    """.format(e), 500


# Captions
@app.route('/caption', methods=['POST'])
def caption():
    """
    """
    input_file = request.files['image']
    # print(type(input_file), input_file)
    output = neural_api.apply_model(input_file)
    return jsonify(output)


# Captions
@app.route('/caption_b64', methods=['POST'])
def caption_b64():
    """
    """
    input_file = request.form['img']
    output = neural_api.apply_model_b64(input_file)
    return jsonify(output)

app.run(host="0.0.0.0", port=5000, debug=False)
