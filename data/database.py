import sqlite3

DB_NAME = 'data/marketplace.sqlite'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha_hash TEXT NOT NULL,
            tipo TEXT NOT NULL CHECK(tipo IN ('freelancer', 'cliente'))
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS servicos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT NOT NULL,
            preco REAL NOT NULL,
            freelancer_id INTEGER NOT NULL,
            FOREIGN KEY (freelancer_id) REFERENCES usuarios (id) ON DELETE CASCADE
        );
    ''')
    conn.commit()
    conn.close()