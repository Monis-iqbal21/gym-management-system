from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("aboutUs.html")

@app.route("/member")
def member():
    return render_template("Member.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.errorhandler(404)
def page_not_found(e):
    return "Page not found", 404


if __name__ == "__main__":
    app.run(debug=True)
