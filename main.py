from flask import Flask, render_template, redirect, request
from models.chamado import *
from database import get_db_connection

app = Flask(__name__)


@app.route("/")
def inicial():
    return render_template("index.html")


@app.route("/pedidos")
def pedidos():
    return render_template("pedidos.html", chamados=get_chamados_by_status(None))


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/tabela")
def tabela():
    return render_template("tabela.html", chamados=get_chamados_by_status(None))


@app.route('/pedidosO')
def pedidosO():
    return render_template('emAndamento.html', chamados=get_chamados_by_status('ongoing'))


@app.route('/pedidosMU')
def pedidosMU():
    return render_template('muitoUrgente.html', chamados=get_chamados_by_status('most-urgent'))


@app.route('/pedidosF')
def pedidosF():
    return render_template('finalizado.html', chamados=get_chamados_by_status('finished'))


@app.route('/pedidosU')
def pedidosU():
    return render_template('urgente.html', chamados=get_chamados_by_status('urgent'))


@app.route('/pedidosC')
def pedidosC():
    return render_template('comum.html', chamados=get_chamados_by_status('common'))


@app.route('/pedidosNS')
def pedidosNS():
    return render_template('semstatus.html', chamados=get_chamados_by_status('no-status'))


@app.route("/grafico")
def grafico():
    return render_template("grafico.html", chamados=get_chamados_by_status(None))


@app.route("/atualizarChamado/<pagina>", methods=["POST"])
def atualizarChamado(pagina):
    chamadoId = request.form['chamado_id']
    observacao = request.form['observacao']
    status = request.form['status']
    POSTChamado(chamadoId, observacao, status)
    if pagina == 'todos':
        return redirect("/pedidos")
    elif pagina == 'andamento':
        return redirect("/pedidosO")
    elif pagina == 'comum':
        return redirect("/pedidosC")
    elif pagina == 'finalizado':
        return redirect("/pedidosF")
    elif pagina == "muitoUrgente":
        return redirect("/pedidosMU")
    elif pagina == "semStatus":
        return redirect("/pedidosNS")
    elif pagina == "urgente":
        return redirect("/pedidosU")


if __name__ == '__main__':
    app.run(debug=True)
