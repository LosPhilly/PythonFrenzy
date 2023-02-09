from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, PySocial!"



@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # add user to database
        return "User created!"
    return '''
        <form action="/signup" method="post">
            <p><input type name="username"></p>
            <p><input type="password" name="password"></p>
            <p><button type="submit">Sign Up</button></p>
        </form>
    '''

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # check if username and password are correct
        # if yes, log the user in
        return "Logged In!"
    return '''
        <form action="/login" method="post">
            <p><input type name="username"></p>
            <p><input type="password" name="password"></p>
            <p><button type="submit">Login</button></p>
        </form>
    '''



@app.route("/profile/<username>")
def profile(username):
    # get user's information from database
    return "Welcome to {}'s profile!".format(username)


@app.route("/feed", methods=["GET", "POST"])
def feed():
    if request.method == "POST":
        post = request.form["post"]
        # add post to database
        return "Post added to feed!"
    # get all posts from database
    return '''
        <form action="/feed" method="post">
            <p><textarea name="post"></textarea></p>
            <p><button type="submit">Post</button></p>
        </form>
    '''












if __name__ == "__main__":
    app.run()
