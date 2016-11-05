from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home.html", name="Kerry")

if __name__ == "__main__":
    app.run()
    app.jinja_env.line_statement_prefix = '%'
