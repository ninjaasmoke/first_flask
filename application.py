from flask import Flask, url_for, render_template, request
from markupsafe import escape

from login import log_the_user_in, valid_login

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/me")
def something_else():
    return "<h1>Nithin Sai is me</h1>"

# escaping from attacks
@app.route("/users/<name>")
def hello(name=None):
    return render_template('hello.html', name=name)

# @app.route('/users/<string:username>', methods=['GET'])
# def show_user(username):
#     print(username)
#     return f'hi {username}!'

# @app.route('/users/', defaults={'page': 1})
# @app.route('/users/page/<int:page>')
# def show_users(page):
#     return f'{page}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath: {escape(subpath)}'

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)