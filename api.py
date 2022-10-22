import json
import os
import time
from urllib import response
from flask import Flask, jsonify,request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
 
@app.route('/', methods=['GET'])
 
def index():
    return jsonify({'message': 'Hello World'})


app.run(port=9000,host='0.0.0.0',debug=True)