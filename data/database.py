# data/database.py

import sqlite3

DB_NAME = 'data/marketplace.sqlite'

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn

def init_db():
    print("--- EXECUTANDO init_db() para criar tabelas... ---")
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha_hash TEXT NOT NULL,
            tipo TEXT NOT NULL CHECK(tipo IN ('freelancer', 'cliente')),
            saldo REAL NOT NULL DEFAULT 0.0
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

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_contratacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            preco_pago REAL NOT NULL,
            cliente_id INTEGER NOT NULL,
            servico_id INTEGER NOT NULL,
            FOREIGN KEY (cliente_id) REFERENCES usuarios (id),
            FOREIGN KEY (servico_id) REFERENCES servicos (id)
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS freelancer_perfis (
            id INTEGER PRIMARY KEY,
            usuario_id INTEGER UNIQUE NOT NULL,
            bio TEXT,
            habilidades TEXT,
            portfolio_url TEXT,
            telefone TEXT,
            cidade TEXT,
            FOREIGN KEY (usuario_id) REFERENCES usuarios (id) ON DELETE CASCADE
        );
    ''')
    print("--- Tabela 'freelancer_perfis' verificada/criada com sucesso. ---")

    conn.commit()
    conn.close()