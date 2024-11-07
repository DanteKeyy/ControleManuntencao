from database import get_db_connection

conn = get_db_connection()

conn.autocommit = True  # Necessário para criar uma nova tabela
cur = conn.cursor()


create_table_query = """
CREATE TABLE chamados (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    nome_solicitante VARCHAR(255) NOT NULL,
    email_solicitante VARCHAR(255) NOT NULL,
    descricao TEXT NOT NULL,
    data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    local VARCHAR(55),
    status VARCHAR(50),
    observacao VARCHAR(255)

);
"""

# create_table_query = """
# DROP TABLE chamados;
# """
#
# # Execute o comando SQL
try:
    cur.execute(create_table_query)
    print("Tabela 'chamados' criada com sucesso.")
except Exception as e:
    print(f"Erro ao criar a tabela: {e}")
finally:
    pass
    # Feche a comunicação com o banco de dados
    # cur.close()
    # conn.close()



registros = [
    ("Chamado 2", "Fernando Vieira", "fernandofv2@gmail.com", "Fiação elétrica exposta no corredor principal. Precisa de inspeção imediata para evitar riscos de choque.", "2024-08-22 09:00:00", "most-urgent", "Corredor Principal"),
    ("Chamado 3", "José Fagundes", "josefagundes@hotmail.com", "Vazamento na tubulação do banheiro. Verificar e reparar a tubulação para evitar danos maiores.", "2024-08-22 10:00:00", "urgent", "Banheiro"),
    ("Chamado 4", "Pedro Carrilho", "c.pedro23@gmail.com", "Janela do escritório com problema de fechamento. Substituir ou ajustar o mecanismo de fechamento.", "2024-08-22 11:00:00", "common", "Escritório"),
    ("Chamado 5", "Ana Xavier", "xavierana2219@outlook.com", "Interruptor de luz não funcionando na sala de reunião. Substituir o interruptor.", "2024-08-22 12:00:00", "no-status", "Sala de Reunião"),
    ("Chamado 6", "Claudio Tavares", "tavaresclaudio22@gmail.com", "Sistema de alarme de incêndio desativado. Verificar e garantir que o sistema esteja operacional.", "2024-08-22 13:00:00", "finished", "Corredor Principal"),
    ("Chamado 7", "Manuela Gomes", "gomesmanuela@yahoo.com", "Porta de entrada com fechadura defeituosa. Precisa de reparo ou substituição da fechadura.", "2024-08-22 14:00:00", "most-urgent", "Entrada"),
    ("Chamado 8", "Julia Pedroso", "pedroso.ju2@gmail.com", "Sistema de irrigação do jardim não está funcionando. Verificar bombas e tubulações.", "2024-08-22 15:00:00", "urgent", "Jardim"),
    ("Chamado 9", "Claudia Fernandes", "fernandes.clau2@gmail.com", "Luminárias do corredor precisam de substituição. Substituir lâmpadas queimadas e verificar circuitos.", "2024-08-22 16:00:00", "common", "Corredor"),
    ("Chamado 10", "Daniel Souza", "d.souza21@gmail.com", "Computador do servidor com falha de hardware. Realizar diagnóstico e substituição de peças defeituosas.", "2024-08-22 17:00:00", "no-status", "Sala de Servidores"),
    ("Chamado 11", "Deyvid Assis", "deyvid.assis@outlook.com", "Ar condicionado do escritório central está inoperante. Agendar manutenção ou reparo urgente.", "2024-08-22 18:00:00", "finished", "Escritório Central"),
    ("Chamado 12", "Iris Ferreira", "ferreirairis@gmail.com", "Fugas de gás detectadas na cozinha. Contatar serviços de emergência e reparar vazamento.", "2024-08-22 19:00:00", "most-urgent", "Cozinha"),
    ("Chamado 13", "Moises Olimpo", "moises.olimpo@gmail.com", "Piso da área de armazenamento está danificado. Reparo necessário para evitar acidentes.", "2024-08-22 20:00:00", "urgent", "Área de Armazenamento"),
    ("Chamado 14", "Amanda Costa", "costaamanda268@hotmail.com", "Equipamentos de TI na sala de servidores estão superaquecendo. Verificar sistemas de ventilação.", "2024-08-22 21:00:00", "common", "Sala de Servidores"),
    ("Chamado 15", "Sophia Colovati", "so.colovati@gmail.com", "Porta de saída de emergência com mecanismo de travamento defeituoso. Verificar e reparar.", "2024-08-22 22:00:00", "no-status", "Saída de Emergência")
]



# Comando SQL para inserir registros
insert_query = """
INSERT INTO chamados (titulo, nome_solicitante, email_solicitante, descricao, data, status, local)
VALUES (%s, %s, %s,%s, %s, %s, %s);
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