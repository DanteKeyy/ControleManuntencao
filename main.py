from flask import Flask, render_template
from models.chamado import *
from database import get_db_connection

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


@app.route('/pedidosO')
def pedidosO():
    return render_template('emAndamento.html', chamados=get_chamados_O())


@app.route('/pedidosMU')
def pedidosMU():
    return render_template('muitoUrgente.html', chamados=get_chamados_MU())


@app.route('/pedidosF')
def pedidosF():
    return render_template('finalizado.html', chamados=get_chamados_F())


@app.route('/pedidosU')
def pedidosU():
    return render_template('urgente.html', chamados=get_chamados_U())


@app.route('/pedidosC')
def pedidosC():
    return render_template('comum.html', chamados=get_chamados_C())


@app.route('/pedidosNS')
def pedidosNS():
    return render_template('semstatus.html', chamados=get_chamados_NS())


if __name__ == '__main__':
    app.run(debug=True)
