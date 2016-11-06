from flask import Flask
from flask import render_template


app = Flask(__name__)

#renders the home page of the webapp
@app.route("/")
def hello():
    return render_template("home.html", name="Jane Smith")

#renders webpage detaling the Main Canal Loop Route
@app.route("/route/mainCanalLoop")
def mainCanalLoop():
    return render_template("route1.html")

#renders webpage detailing the Lagoon Route
@app.route("/route/lagoon")
def lagoon():
    return render_template("route2.html")

#renders page delivered to user when they check in at kelpie signpost
@app.route("/posts/kelpie")
def kelpie():
    return render_template("kelpie.html")

#runs the web app
if __name__ == "__main__":
    app.run()
    app.jinja_env.line_statement_prefix = '%'
