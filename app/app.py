from flask import Flask, render_template, Markup
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
@app.route('/index')
def index():
    all_spec = Markup('a')
    return render_template('index.html')

@app.route('/firsttry')
def firsttry():
    return render_template('second.html')

if __name__ == '__main__':
    app.run(debug=True)