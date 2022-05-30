from flask import Flask, render_template
from helper import start
app = Flask(__name__)


@app.route("/")
def main_menu():
  return render_template("home.html")

@app.route("/<string:id>")
def main(id):
  return render_template("start.html")

template_start=start