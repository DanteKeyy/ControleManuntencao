from flask import Flask, render_template
from models.chamado import get_chamados

app = Flask(__name__)

@app.route("/")
def inicial():
    return render_template("index.html")


@app.route("/pedidos")
def pedidos():
    return render_template("pedidos.html", chamados=get_chamados())

@app.route("/home")
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)