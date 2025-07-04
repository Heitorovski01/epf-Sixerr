# models/freelancer.py (Versão Corrigida Definitiva)

from data.database import get_db_connection
from models.usuario import Usuario

class Freelancer(Usuario):
    def __init__(self, nome: str, email: str, id: int = None, bio: str = None, habilidades: str = None, portfolio_url: str = None):
        super().__init__(nome, email, 'freelancer', id)
        self.bio = bio
        self.habilidades = habilidades
        self.portfolio_url = portfolio_url

    def save(self):
        # Inicia a conexão com o banco
        conn = get_db_connection()
        cursor = conn.cursor()

        # --- Lógica de Criação (INSERT) ---
        if self.id is None:
            # 1. Insere na tabela 'usuarios' primeiro
            cursor.execute("INSERT INTO usuarios (nome, email, senha_hash, tipo) VALUES (?, ?, ?, ?)",
                           (self.nome, self.email, self._senha_hash, self.tipo))
            self.id = cursor.lastrowid # 2. Pega o novo ID gerado

            # 3. Usa o novo ID para inserir na tabela 'freelancer_perfis'
            cursor.execute("""
                INSERT INTO freelancer_perfis (usuario_id, bio, habilidades, portfolio_url)
                VALUES (?, ?, ?, ?)
            """, (self.id, self.bio, self.habilidades, self.portfolio_url))
        
        # --- Lógica de Atualização (UPDATE) ---
        else:
            # Atualiza a tabela 'usuarios'
            cursor.execute("UPDATE usuarios SET nome=?, email=?, senha_hash=? WHERE id=?",
                           (self.nome, self.email, self._senha_hash, self.id))
            
            # Atualiza a tabela 'freelancer_perfis'
            cursor.execute("""
                UPDATE freelancer_perfis SET bio = ?, habilidades = ?, portfolio_url = ?
                WHERE usuario_id = ?
            """, (self.bio, self.habilidades, self.portfolio_url, self.id))

        # Finaliza a transação e fecha a conexão
        conn.commit()
        conn.close()