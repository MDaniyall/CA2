from flask import Flask, render_template
import datetime

app = Flask(_name_)

@app.route('/')
def hello_world():
    return render_template('index.html', current_year=datetime.datetime.now().year)

@app.route('/about')
def about():
    return render_template('about.html')

if _name_ == '_main_':
    app.run(debug=True)