from flask import Flask, render_template, request

app = Flask(__name__)

jobs = [
    {"title": "Software Engineer", "company": "Google"},
    {"title": "Data Scientist", "company": "Facebook"},
    {"title": "DevOps Engineer", "company": "Amazon"},
    {"title": "Product Manager", "company": "Apple"},
]

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        title = request.form["title"]
        company = request.form["company"]
        jobs.append({"title": title, "company": company})
    return render_template("home.html", jobs=jobs)

if __name__ == "__main__":
    app.run(debug=True)
