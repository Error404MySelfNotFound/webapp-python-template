from flask import Flask, Response
import json

from frutta import frutta


app = Flask("frutta")

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/jquery-3.4.1.min.js')
def js():
    return app.send_static_file('jquery-3.4.1.min.js')

@app.route("/data")
def data():
    json_string = json.dumps([x for x in frutta])
    return Response(json_string, mimetype='application/json')
