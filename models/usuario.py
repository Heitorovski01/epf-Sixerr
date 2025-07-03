# models/usuario.py (versão corrigida)

import sqlite3
import hashlib
from data.database import get_db_connection

class Usuario:
    def __init__(self, nome: str, email: str, tipo: str, id: int = None):
        self.id, self.nome, self.email, self.tipo = id, nome, email, tipo
        self._senha_hash = None

    def set_senha(self, senha: str):
        self._senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    def check_senha(self, senha: str) -> bool:
        return self._senha_hash == hashlib.sha256(senha.encode()).hexdigest() if self._senha_hash else False
    
    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("INSERT INTO usuarios (nome, email, senha_hash, tipo) VALUES (?, ?, ?, ?)",
                           (self.nome, self.email, self._senha_hash, self.tipo))
            self.id = cursor.lastrowid
        else:
            cursor.execute("UPDATE usuarios SET nome=?, email=?, senha_hash=?, tipo=? WHERE id=?",
                           (self.nome, self.email, self._senha_hash, self.tipo, self.id))
        conn.commit()
        conn.close()
        return self

    @classmethod
    def find_by_email(cls, email: str):
        # --- CORREÇÃO AQUI ---
        # A importação foi movida para dentro do método
        from models.freelancer import Freelancer
        from models.cliente import Cliente

        conn = get_db_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
        user_data = cursor.fetchone()
        conn.close()
        if not user_data: return None
        
        UserClass = Freelancer if user_data['tipo'] == 'freelancer' else Cliente
        
        user = UserClass(nome=user_data['nome'], email=user_data['email'], id=user_data['id'])
        user._senha_hash = user_data['senha_hash']
        return user
    
    @classmethod
    def find_by_id(cls, user_id: int):
        # --- CORREÇÃO AQUI ---
        # A importação foi movida para dentro do método
        from models.freelancer import Freelancer
        from models.cliente import Cliente

        conn = get_db_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE id = ?", (user_id,))
        user_data = cursor.fetchone()
        conn.close()
        if not user_data: return None

        UserClass = Freelancer if user_data['tipo'] == 'freelancer' else Cliente
        user = UserClass(nome=user_data['nome'], email=user_data['email'], id=user_data['id'])
        user._senha_hash = user_data['senha_hash']
        return user