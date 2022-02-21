from flask import Flask

app = Flask(__name__)


@app.route('/training/<prof>')
def function(prof):
    pass