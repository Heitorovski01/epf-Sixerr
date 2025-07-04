# models/freelancer.py
from data.database import get_db_connection
from models.usuario import Usuario

class Freelancer(Usuario):
    def __init__(self, nome: str, email: str, id: int = None, bio: str = None, habilidades: str = None, portfolio_url: str = None):
        super().__init__(nome, email, 'freelancer', id)
        self.bio = bio
        self.habilidades = habilidades
        self.portfolio_url = portfolio_url

    def save(self):
        
        super().save()

        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        
        cursor.execute("SELECT * FROM freelancer_perfis WHERE usuario_id = ?", (self.id,))
        perfil_existente = cursor.fetchone()

        if perfil_existente:
            cursor.execute("""
                UPDATE freelancer_perfis SET bio = ?, habilidades = ?, portfolio_url = ?
                WHERE usuario_id = ?
            """, (self.bio, self.habilidades, self.portfolio_url, self.id))
        else:
            cursor.execute("""
                INSERT INTO freelancer_perfis (usuario_id, bio, habilidades, portfolio_url)
                VALUES (?, ?, ?, ?)
            """, (self.id, self.bio, self.habilidades, self.portfolio_url))

        conn.commit()
        conn.close()