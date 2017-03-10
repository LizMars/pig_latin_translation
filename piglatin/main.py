"""Pig Latin Translation Microservice."""

from flask import render_template, request, Response
from piglatin import app, cross_origin
import converter

@app.route('/', methods=['POST'])
@cross_origin()
def index():
    if request.method == 'POST':
        body = request.json
        resp = converter.convert_text(body["body"])
    return Response(resp, mimetype="text/plain")
