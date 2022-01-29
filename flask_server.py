from flask import Flask, render_template, jsonify, request, redirect, url_for
from test import testFunc
from plaluvs_face import start

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/test')
def home2():
    return str(testFunc(10, 20))

#https://plaluvs-image.s3.ap-northeast-2.amazonaws.com/static/sample.jpg
@app.route('/image')
def home3():
    url = request.args.get("url")
    return start(url)


if __name__ == '__main__':
    app.run(debug=True)
