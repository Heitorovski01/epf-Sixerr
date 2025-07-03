# data/database.py
import sqlite3

DB_NAME = 'data/marketplace.sqlite'

def get_db_connection():
    """Cria e retorna uma conexão com o banco de dados."""
    conn = sqlite3.connect(DB_NAME)
    return conn

def init_db():
    """Inicializa o banco de dados, criando as tabelas se elas não existirem."""
    conn = get_db_connection()
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