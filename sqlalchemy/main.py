from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/<word>')
@app.route('/index/<word>')
def mars(word):
    return render_template('index.html', title=word)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')