from flask import Flask, jsonify, request
from flask_cors import CORS
import re

import rake
import sumrise


app = Flask(__name__)
CORS(app)
extractor = rake.RakeKeywordExtractor()

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'It works!'})


@app.route('/keywords/', methods=['POST'])
def resp_keyword():
    url = request.json['search']
    resp = jsonify(extractor.extract(url, incl_scores=True))
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp

@app.route('/summary/', methods=['POST'])
def resp_sum():
    url = request.json['search']
    summary = sumrise.sumrise(url, 7)
    summary = re.sub(r'\s*Sentence:\s*|[<>()]', '', summary)
    resp = jsonify(summary)
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp



if (__name__ == '__main__'):
    app.run(host='192.168.0.101', port=6166, debug=False)
