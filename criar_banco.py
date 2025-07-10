import sqlite3


conexao = sqlite3.connect('database.db')
cursor = conexao.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS carrinho (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produto TEXT NOT NULL,
        quantidade INTEGER NOT NULL DEFAULT 1
    )
''')


conexao.commit()
conexao.close()

print("Banco de dados criado com sucesso.")