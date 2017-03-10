from flask import render_template, request, Response
from piglatin import app, cross_origin


@app.route('/', methods=['GET','POST'])
@cross_origin()
def index():
    txt = None
    if request.method == 'POST':
        body = request.json
        txt = body["body"]
        print body["body"]
    return render_template('result.html', text= txt)
