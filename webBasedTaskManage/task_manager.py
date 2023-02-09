from flask import Flask, request, render_template



app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Simple Task Manager!"

@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        task = request.form["task"]
        # Add the task to your database or file
        return "Task added successfully!"
    return render_template("add_task.html")

if __name__ == "__main__":
    app.run()
