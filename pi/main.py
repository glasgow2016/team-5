from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home.html", name="Kerry")

@app.route("/route/mainCanalLoop")
def mainCanalLoop():
    return render_template("route1.html")

@app.route("/route/lagoon")
def lagoon():
    return render_template("route2.html")

@app.route("/posts/kelpie")
def kelpie():
    return render_template("kelpie.html")
t
if __name__ == "__main__":
    app.run()
    app.jinja_env.line_statement_prefix = '%'
