from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', current_year=datetime.datetime.now().year)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)