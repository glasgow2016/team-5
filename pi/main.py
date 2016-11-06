from flask import Flask
from flask import render_template
from RouteCreator import CreateRoute
from RouteTracker import UpdateRoute


app = Flask(__name__)

#renders the home page of the webapp
@app.route("/")
def hello():
    return render_template("home.html")

#renders webpage detaling the Main Canal Loop Route
@app.route("/route/mainCanalLoop")
def mainCanalLoop():
    CreateRoute("route1")
    return render_template("route1.html")

#renders webpage detailing the Lagoon Route
@app.route("/route/lagoon")
def lagoon():
    CreateRoute("route2")
    return render_template("route2.html")

#renders page delivered to user when they check in at kelpie signpost
@app.route("/posts/kelpie/<float:time>")
def kelpie(time):
    finished = UpdateRoute(time, "kelpie")
    return render_template("kelpie.html")

#renders page delivered to user when they check in at visitor centre
@app.route("/posts/visitorCentre/<float:time>")
def visitorCentre(time):
    finished = UpdateRoute(time, "visitorCentre")
    return render_template("vistor.html")

#renders page delivered to user when they check in at visitor centre
@app.route("/posts/lagoon?time=<float:time>")
def Lagoon(time):
    finished = UpdateRoute(time, "lagoon")
    return render_template("lagoon.html")


#runs the web app
if __name__ == "__main__":
    app.run()
    app.jinja_env.line_statement_prefix = '%'
