import sqlite3
import hashlib
from data.database import get_db_connection

class Usuario:
    def __init__(self, nome: str, email: str, tipo: str, id: int = None, saldo: float = 0.0, telefone: str = None, cidade: str = None):
        self.id = id
        self.nome = nome
        self.email = email
        self.tipo = tipo
        self.saldo = saldo
        self.telefone = telefone
        self.cidade = cidade
        self._senha_hash = None

    def set_senha(self, senha: str):
        self._senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    def check_senha(self, senha: str) -> bool:
        hash_da_senha_digitada = hashlib.sha256(senha.encode()).hexdigest()
        return self._senha_hash == hash_da_senha_digitada

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("INSERT INTO usuarios (nome, email, senha_hash, tipo, saldo, telefone, cidade) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (self.nome, self.email, self._senha_hash, self.tipo, self.saldo, self.telefone, self.cidade))
            self.id = cursor.lastrowid
        else:
            cursor.execute("UPDATE usuarios SET nome=?, email=?, senha_hash=?, saldo=?, telefone=?, cidade=? WHERE id=?",
                           (self.nome, self.email, self._senha_hash, self.saldo, self.telefone, self.cidade, self.id))
        conn.commit()
        conn.close()
        return self
    
    def atualiza_saldo(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE usuarios SET saldo = ? WHERE id = ?", (self.saldo, self.id))
        conn.commit()
        conn.close()

    @classmethod
    def _find(cls, column: str, value):
        from models.freelancer import Freelancer
        from models.cliente import Cliente

        conn = get_db_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        query = f"""
            SELECT u.id, u.nome, u.email, u.senha_hash, u.tipo, u.saldo, u.telefone, u.cidade,
                   p.bio, p.habilidades, p.portfolio_url
            FROM usuarios u
            LEFT JOIN freelancer_perfis p ON u.id = p.usuario_id
            WHERE u.{column} = ?
        """
        cursor.execute(query, (value,))
        
        user_data = cursor.fetchone()
        conn.close()
        if not user_data: return None

        if user_data['tipo'] == 'freelancer':
            user = Freelancer(nome=user_data['nome'], email=user_data['email'], id=user_data['id'],
                              saldo=user_data['saldo'], bio=user_data['bio'], 
                              habilidades=user_data['habilidades'], portfolio_url=user_data['portfolio_url'],
                              telefone=user_data['telefone'], cidade=user_data['cidade'])
        else:
            user = Cliente(nome=user_data['nome'], email=user_data['email'], id=user_data['id'],
                           saldo=user_data['saldo'], telefone=user_data['telefone'], cidade=user_data['cidade'])
        
        user._senha_hash = user_data['senha_hash']
        return user

    @classmethod
    def find_by_id(cls, user_id: int):
        return cls._find('id', user_id)

    @classmethod
    def find_by_email(cls, email: str):
        return cls._find('email', email)
    @staticmethod
    def delete_by_id(user_id: int):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (user_id,))
        conn.commit()
        conn.close()