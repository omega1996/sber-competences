from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

stat_tech_data = pd.read_csv('stat_tech_data.csv')

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/frontend')
def frontend():
    return render_template('frontend/index.html')


@app.route('/get_top_tech/<specialization>/<year>/<month>')
def get_top_tech(specialization, year, month):
    return stat_tech_data[
        (stat_tech_data.spec == specialization)
        & (stat_tech_data.year == int(year))
        & (stat_tech_data.month == int(month))
    ].tags.iloc[0]


if __name__ == '__main__':
    app.run(debug=True)
