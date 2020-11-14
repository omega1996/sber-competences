from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/profession/<prof_name>')
def frontend(prof_name):
    return render_template(prof_name+'/index.html')


if __name__ == '__main__':
    app.run(debug=True)
