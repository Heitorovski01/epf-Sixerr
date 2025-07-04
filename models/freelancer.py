# models/freelancer.py (Versão Corrigida)

from data.database import get_db_connection
from models.usuario import Usuario

class Freelancer(Usuario):
    def __init__(self, nome: str, email: str, id: int = None, saldo: float = 0.0, bio: str = None, habilidades: str = None, portfolio_url: str = None):
        super().__init__(nome, email, 'freelancer', id, saldo)
        self.bio = bio
        self.habilidades = habilidades
        self.portfolio_url = portfolio_url

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        # --- Lógica de Criação (INSERT) ---
        if self.id is None:
            # CORREÇÃO 1: Adicionado o 5º '?' para o saldo
            cursor.execute("INSERT INTO usuarios (nome, email, senha_hash, tipo, saldo) VALUES (?, ?, ?, ?, ?)",
                           (self.nome, self.email, self._senha_hash, self.tipo, self.saldo))
            self.id = cursor.lastrowid

            cursor.execute("""
                INSERT INTO freelancer_perfis (usuario_id, bio, habilidades, portfolio_url)
                VALUES (?, ?, ?, ?)
            """, (self.id, self.bio, self.habilidades, self.portfolio_url))
        
        # --- Lógica de Atualização (UPDATE) ---
        else:
            # CORREÇÃO 2: Adicionado o 'saldo' à atualização
            cursor.execute("UPDATE usuarios SET nome=?, email=?, senha_hash=?, saldo=? WHERE id=?",
                           (self.nome, self.email, self._senha_hash, self.saldo, self.id))
            
            cursor.execute("""
                UPDATE freelancer_perfis SET bio = ?, habilidades = ?, portfolio_url = ?
                WHERE usuario_id = ?
            """, (self.bio, self.habilidades, self.portfolio_url, self.id))

        conn.commit()
        conn.close()