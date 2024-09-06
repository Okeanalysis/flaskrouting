from flask import Flask
from flask import request
from flask import redirect
from flask import make_response
from flask import abort
app= Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World</h1>'

@app.route('/bur')
def bur():
    user_agent= request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)

@app.route('/user/<name>')
def user(name):
    return '<h1> Hello {}!</h1>'.format(name)

@app.route('/acct')
def jae():
    response= make_response('<h1>this document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/car')
def boy():
    return redirect('https://www.example.com')

@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, {}</h1>'.format(user.name)
if __name__== "__main__":
    app.run(debug=True)
