import sqlite3

conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()

cursor.execute("""ALTER TABLE clientes ADD data_nascimento TEXT""")
cursor.execute("""ALTER TABLE clientes ADD endereco TEXT""")
cursor.execute("""ALTER TABLE clientes ADD cpf TEXT""")


conexao.commit()
conexao.close()