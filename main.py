import sqlite3


def conectar():
    """Abre a conexão com o banco de dados SQLite."""
    return sqlite3.connect("clientes.db")


def criar_tabela():
    """Cria a tabela de clientes, se ela ainda não existir."""
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT,
            telefone TEXT
        )
    """)
    conexao.commit()
    conexao.close()


def cadastrar_cliente(nome, email, telefone):
    """Insere um novo cliente no banco de dados."""
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)",
        (nome, email, telefone),
    )
    conexao.commit()
    conexao.close()
    print(f"Cliente {nome} cadastrado com sucesso!")


def listar_clientes():
    """Mostra todos os clientes cadastrados."""
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, email, telefone FROM clientes")
    clientes = cursor.fetchall()
    conexao.close()

    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    print("\n--- Lista de clientes ---")
    for cliente in clientes:
        print(f"ID: {cliente[0]} | Nome: {cliente[1]} | E-mail: {cliente[2]} | Telefone: {cliente[3]}")


def menu():
    criar_tabela()
    while True:
        print("\n1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("E-mail: ")
            telefone = input("Telefone: ")
            cadastrar_cliente(nome, email, telefone)
        elif opcao == "2":
            listar_clientes()
        elif opcao == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
