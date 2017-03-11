"""Pig Latin Translation Microservice."""

from flask import render_template, request, Response
from piglatin import app, cross_origin
import converter

@app.route('/', methods=['POST'])
@cross_origin()
def index():
    if request.method == 'POST':
        resp = converter.convert_text(request.data)
    return Response(resp, mimetype="text/plain")
