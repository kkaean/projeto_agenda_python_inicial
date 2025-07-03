import sqlite3

# Conectar (ou criar) o banco de dados
conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()

# Criar a tabela de clientes
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT NOT NULL,
    email TEXT NOT NULL,
    data_nascimento TEXT,
    endereco TEXT,
    cpf TEXT
)
""")

conexao.commit()
conexao.close()

def menu():
    print("\nAGENDA DE CLIENTES")
    print("1 - Adicionar cliente")
    print("2 - Listar clientes")
    print("3 - Atualizar cliente")
    print("4 - Deletar cliente")
    print("5 - Sair")

def adicionar_cliente():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
    endereco = input("Endereço: ")
    cpf = input("CPF: ")

    conexao = sqlite3.connect("agenda.db")
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO clientes (nome, telefone, email, data_nascimento, endereco, cpf) VALUES (?, ?, ?, ?, ?, ?)",
                   (nome, telefone, email, data_nascimento, endereco, cpf))

    conexao.commit()
    conexao.close()

    print("Cliente adicionado com sucesso!")


def listar_clientes():
    conexao = sqlite3.connect("agenda.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    if not clientes:
        print("Nenhum cliente encontrado.")
    else:
        for cliente in clientes:
            print(f"ID: {cliente[0]} | Nome: {cliente[1]} | Telefone: {cliente[2]} | E-mail: {cliente[3]} | Data: {cliente[4]} | Endereço: {cliente[5]} | CPF: {cliente[6]}")

    conexao.close()


def atualizar_cliente():
    id_cliente = input("ID do cliente a ser atualizado: ")

    # Verificar se o cliente existe
    conexao = sqlite3.connect("agenda.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM clientes WHERE id = ?", (id_cliente,))
    cliente = cursor.fetchone()

    if not cliente:
        print(f"Cliente com ID {id_cliente} não encontrado.")
        conexao.close()
        return

    # Solicitar novos dados
    novo_nome = input("Novo nome: ")
    novo_telefone = input("Novo telefone: ")
    novo_email = input("Novo e-mail: ")
    novo_data_nascimento = input("Nova data de nascimento (DD/MM/AAAA): ")
    novo_endereco = input("Novo endereço: ")
    novo_cpf = input("Novo CPF: ")

    # Atualizar os dados no banco
    cursor.execute("""
    UPDATE clientes 
    SET nome = ?, telefone = ?, email = ?, data_nascimento = ?, endereco = ?, cpf = ? 
    WHERE id = ?
    """, (novo_nome, novo_telefone, novo_email, novo_data_nascimento, novo_endereco, novo_cpf, id_cliente))

    conexao.commit()
    conexao.close()

    print("Cliente atualizado com sucesso!")


def deletar_cliente():
    id_cliente = input("ID do cliente a ser deletado: ")

    # Verificar se o cliente existe
    conexao = sqlite3.connect("agenda.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM clientes WHERE id = ?", (id_cliente,))
    cliente = cursor.fetchone()

    if not cliente:
        print(f"Cliente com ID {id_cliente} não encontrado.")
        conexao.close()
        return

    cursor.execute("DELETE FROM clientes WHERE id = ?", (id_cliente,))
    conexao.commit()
    conexao.close()

    print("Cliente deletado com sucesso!")


while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_cliente()
    elif opcao == "2":
        listar_clientes()
    elif opcao == "3":
        atualizar_cliente()
    elif opcao == "4":
        deletar_cliente()
    elif opcao == "5":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
