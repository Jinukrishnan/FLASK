from flask import Flask

app=Flask(__name__)
@app.route('/home')
def home():
    return '<h1>This Is First App</h1>'
@app.route('/user/<name>')
def user(name):
    return '<h1>hello,%s'+name+'</h1>'
@app.route('/profile/<int:id>')
def profile(id):
    return 'your id is %d'%id
# add_url_rule
# There is one more approach to perform routing for the flask web application that can be done by using the add_url() function of the Flask class. The syntax to use this function is given below.
def about():
    return 'this is aboout page'

app.add_url_rule('/about','about',about)
app.run(debug=True)

