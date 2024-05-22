from flask import Flask, render_template, send_file
import pandas as pd
import os

app = Flask(__name__, template_folder='web')

@app.route('/')
def index():
    df = pd.read_csv('results.csv')
    return render_template('index.html', table=df.to_html(classes='table table-striped'))

@app.route('/export_csv')
def export_csv():
    df = pd.read_csv('results.csv')
    csv_filename = 'exported_data.csv'
    df.to_csv(csv_filename, index=False)

    return send_file(csv_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
