#run a flask app and publish index.html to the web

from flask import Flask, render_template, send_from_directory
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/style.css')
def style():
    return send_from_directory('./styles/', 'style.css')

if __name__ == "__main__":
    app.run(threaded=True)