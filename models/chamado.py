from database import get_db_connection
from typing import List


class Chamado:
    def __init__(self, chamado_id, titulo, descricao, data, status,  local, observacao):
        self.chamado_id = chamado_id
        self.titulo = titulo
        self.descricao = descricao
        self.data = data
        self.status = status
        self.local = local
        self.observacao = observacao

def get_chamados_by_status(status) -> List[Chamado]:
    conn = get_db_connection()
    cursor = conn.cursor()

    if status == None:
        cursor.execute('SELECT * FROM chamados;')
    elif status == 'ongoing':
        cursor.execute("SELECT * FROM chamados WHERE status = 'ongoing';")
    elif status == 'finished':
        cursor.execute("SELECT * FROM chamados WHERE status = 'finished';")
    elif status == 'most-urgent':
        cursor.execute("SELECT * FROM chamados WHERE status = 'most-urgent';")
    elif status == 'urgent':
        cursor.execute("SELECT * FROM chamados WHERE status = 'urgent';")
    elif status == 'commom':
        cursor.execute("SELECT * FROM chamados WHERE status = 'commom';")
    elif status == 'no-status':
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
            local=result[5],
            observacao=result[6]
        )
        chamados.append(chamado)
    return chamados

def POSTChamado(chamado_id, observacao, status):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE chamados
        SET observacao = %s, status = %s
        WHERE id = %s
        """, (observacao, status, chamado_id)
    )
    conn.commit()
    conn.close()
