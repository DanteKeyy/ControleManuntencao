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
(
    "Problema 16",
    "Sistema de alarme disparando falsamente durante a noite. Inspecionar sensores e recalibrar.",
    "2024-09-13 08:30:00",
    "ongoing",
    "Sistema de Segurança"
),
(
    "Problema 17",
    "Falta de energia na ala leste do edifício. Identificar causa e restaurar serviço.",
    "2024-09-13 10:45:00",
    "ongoing",
    "Energia Elétrica"
),
(
    "Problema 18",
    "Vazamento de água no encanamento do 3º andar. Verificar origem e efetuar reparo.",
    "2024-09-13 14:15:00",
    "ongoing",
    "Hidráulica"
)
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