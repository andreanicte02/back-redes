from flask import Flask, request
from flask_cors import CORS
import simplejson as json
import os

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origin": "*"}})


@app.route('/', methods=['GET'])
def check():
    return "perros :v"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True, use_reloader=True)

