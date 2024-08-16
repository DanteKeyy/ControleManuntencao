from database import get_db_connection

conn = get_db_connection()

conn.autocommit = True  # Necessário para criar uma nova tabela
cur = conn.cursor()

# Defina o comando SQL para criar a tabela
# create_table_query = """
# CREATE TABLE chamados (
#     id SERIAL PRIMARY KEY,
#     titulo VARCHAR(255) NOT NULL,
#     descricao TEXT NOT NULL,
#     data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     status VARCHAR(50),
#     local VARCHAR(255) NOT NULL
# );
# """
#
# # Execute o comando SQL
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
    ("Primeiro chamado", "Descrição do primeiro chamado", "2024-08-16 10:00:00", "Aberto",  "Sala 101"),
    ("Segundo chamado", "Descrição do segundo chamado", "2024-08-16 11:00:00", "Em progresso",  "Sala 102"),
    ("Terceiro chamado", "Descrição do terceiro chamado", "2024-08-16 12:00:00", "Fechado",  "Sala 103")
]

# Comando SQL para inserir registros
insert_query = """
INSERT INTO chamados (titulo, descricao, data, status,  local)
VALUES (%s, %s, %s, %s, %s);
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