from flask import Flask, request
from kheiron import calculate_prefix, calculate_infix

app = Flask(__name__)

@app.route('/')
def index():
    return 'Prefix and Infix Calculator'

@app.route('/prefix', methods=["GET"])
def prefix_calculator():
    # storing the input in a json file
    request_input = request.get_json()
    # json is formatted as "input" : "prefix"
    prefix = request_input['input']

    # must be returned as a string
    return str(calculate_prefix(prefix))


@app.route('/infix', methods=["GET"])
def infix_calculator():
    # storing the input in a json file
    request_input = request.get_json()
    # json is formatted as "input" : "infix"
    infix = request_input['input']

    # must be returned as a string
    return str(calculate_infix(infix))


if __name__ == '__main__':
    app.run()