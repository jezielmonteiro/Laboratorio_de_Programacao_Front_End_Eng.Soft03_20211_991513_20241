from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/biografia")
def biografia():
    return render_template("biografia.html")

@app.route("/discografia")
def discografia():
    return render_template("discografia.html")

@app.route("/turnes")
def turnes():
    return render_template("turnes.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/redes-sociais")
def redes_sociais():
    return render_template("socialmedia.html")