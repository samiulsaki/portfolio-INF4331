from flask import Flask
app = Flask(__name__)
# users = {"sam" : "Samiul Saki",
#         "kari" : "Kari-Anette"}

# @app.route("/")
# def hello():
#     return "Hello World! Its me Sam"

# @app.route('/user')
# def show_user_overview():
#     users_str = "<br>".join(users.values())
#     return '<h1>Our Users</h1><br>{}'.format(users_str)


# @app.route('/user/<username>')
# def show_user_profile(username):
#     return 'User %s' % username


# @app.route('/login')
# def login():
#     return '''
# <html>
# <header><title>The title</title></header>
# <body>
# Hello world
# </body>
# </html>    
#     '''

from flask import render_template

@app.route('/post/')
@app.route('/post/<name>')
def post(name=None):
    return render_template('post.html', name=name)


if __name__ == "__main__":
    app.run(debug=True)
    