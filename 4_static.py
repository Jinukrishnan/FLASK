from flask import Flask
from flask import render_template

app=Flask(__name__)


# @app.route('/')
# def home():
#     return '<h1>This Is First App</h1>'

@app.route('/')
def home():
    return render_template('index.html')
app.run(debug=True)

