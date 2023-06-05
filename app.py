from flask import Flask, request
from carterSearch import *

app = Flask(__name__)

carter_search = CarterSearch()

# Two webhooks
# Raw answers
# Cleaned answers

@app.route('/raw', methods=['POST'])
def get_raw():
    data = request.json  # Assuming the request body is in JSON format

    try:
        response = carter_search.ask_raw(data['query'])
        return response
    except Exception as e:
        return f"Error: {e}"


@app.route('/answer', methods=['POST'])
def get_answer():
    try:
        data = request.json  # Assuming the request body is in JSON format

        query = data['input']
        response = carter_search.ask_answer(query)
        return response
    except Exception as e:
        return f"Error: {e}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5001")





