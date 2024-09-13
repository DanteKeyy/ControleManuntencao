from database import get_db_connection
from typing import List


class Chamado:
    def __init__(self, chamado_id, titulo, descricao, data, status,  local):
        self.chamado_id = chamado_id
        self.titulo = titulo
        self.descricao = descricao
        self.data = data
        self.status = status
        self.local = local

def get_chamados() -> List[Chamado]:
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM chamados;')
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    chamados = []

    for result in results:
        chamado = Chamado(
            chamado_id=result[0],
            titulo=result[1],
            descricao=result[2],
            data=result[3],
            status=result[4],
            local=result[5]
        )
        chamados.append(chamado)
    return chamados

def get_chamados_O() -> List[Chamado]:
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM chamados WHERE status = 'ongoing';")
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    chamados = []

    for result in results:
        chamado = Chamado(
            chamado_id=result[0],
            titulo=result[1],
            descricao=result[2],
            data=result[3],
            status=result[4],
            local=result[5]
        )
        chamados.append(chamado)
    return chamados

def get_chamados_MU() -> List[Chamado]:
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM chamados WHERE status = 'most-urgent';")
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    chamados = []

    for result in results:
        chamado = Chamado(
            chamado_id=result[0],
            titulo=result[1],
            descricao=result[2],
            data=result[3],
            status=result[4],
            local=result[5]
        )
        chamados.append(chamado)
    return chamados

def get_chamados_U() -> List[Chamado]:
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM chamados WHERE status = 'urgent';")
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    chamados = []

    for result in results:
        chamado = Chamado(
            chamado_id=result[0],
            titulo=result[1],
            descricao=result[2],
            data=result[3],
            status=result[4],
            local=result[5]
        )
        chamados.append(chamado)
    return chamados
def get_chamados_C() -> List[Chamado]:
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM chamados WHERE status = 'common';")
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    chamados = []

    for result in results:
        chamado = Chamado(
            chamado_id=result[0],
            titulo=result[1],
            descricao=result[2],
            data=result[3],
            status=result[4],
            local=result[5]
        )
        chamados.append(chamado)
    return chamados
def get_chamados_NS() -> List[Chamado]:
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM chamados WHERE status = 'no-status';")
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    chamados = []

    for result in results:
        chamado = Chamado(
            chamado_id=result[0],
            titulo=result[1],
            descricao=result[2],
            data=result[3],
            status=result[4],
            local=result[5]
        )
        chamados.append(chamado)
    return chamados
