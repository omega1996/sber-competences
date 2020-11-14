from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/frontend')
def frontend():
    return render_template('frontend/index.html')


if __name__ == '__main__':
    app.run(debug=True)
