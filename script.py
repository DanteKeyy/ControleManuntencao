from database import get_db_connection

conn = get_db_connection()

conn.autocommit = True  # Necessário para criar uma nova tabela
cur = conn.cursor()


# create_table_query = """
# CREATE TABLE funcionario (
#     id SERIAL PRIMARY KEY,
#     nome VARCHAR(50) NOT NULL,
#     login VARCHAR(50) NOT NULL,
#     senha VARCHAR(50) NOT NULL
# );
# """

# Execute o comando SQL
# try:
#     cur.execute(create_table_query)
#     print("Tabela 'chamados' criada com sucesso.")
# except Exception as e:
#     print(f"Erro ao criar a tabela: {e}")
# finally:
#     # Feche a comunicação com o banco de dados
#     cur.close()
#     conn.close()

registros = [
    ("TESTETESTE", "1234", "1234"),
]

# Comando SQL para inserir registros
insert_query = """
INSERT INTO funcionario (nome, login, senha)
VALUES (%s, %s, %s);
"""

try:
    cur.executemany(insert_query, registros)
    print("Registros inseridos com sucesso.")
except Exception as e:
    print(f"Erro ao inserir registros: {e}")
finally:
    # Feche a comunicação com o banco de dados
    cur.close()
    conn.close()