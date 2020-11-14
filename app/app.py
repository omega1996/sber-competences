from flask import Flask, render_template
import pandas as pd
import json

import os
app = Flask(__name__)

stat_tech_data = pd.read_csv('app/data/stat_tech_data.csv')
spec_stat = pd.read_csv('app/data/spec_stat.csv')


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/profession/<prof_name>')
def frontend(prof_name):
    tech_files = os.listdir(os.path.join(os.getcwd(), 'app', 'templates', prof_name, 'tech'))
    tech_files_path = [prof_name + '/tech/' + e for e in tech_files]
    prof_path = prof_name +'/'+prof_name+'.html'
    return render_template('profession'+'/index.html', prof_path=prof_path, prof_name=prof_name, tech_files=tech_files, tech_files_path=tech_files_path)


@app.route('/get_top_tech/<specialization>/<year>/<month>')
def get_top_tech(specialization, year, month):
    specialization = (specialization
                      .replace('admin', 'administrator')
                      .replace('gamedev', 'game developer')
                      .replace('ds', 'data science'))
    return stat_tech_data[
        (stat_tech_data.spec == specialization)
        & (stat_tech_data.year == int(year))
        & (stat_tech_data.month == int(month))
    ].tags.iloc[0]


@app.route('/get_spec_stat/<year>/<month>')
def get_spec_stat(year, month):
    month_stat = spec_stat[
        (spec_stat.year == int(year))
        & (spec_stat.month == int(month))
    ]
    return json.dumps(month_stat[['spec', 'freq']].to_dict('record'))


if __name__ == '__main__':
    app.run(debug=True)
