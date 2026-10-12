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


if __name__ == "__main__":
    criar_tabela()
    print("Banco de dados e tabela criados com sucesso!")
