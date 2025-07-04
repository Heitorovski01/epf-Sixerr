from data.database import get_db_connection
from models.usuario import Usuario

class Freelancer(Usuario):
    def __init__(self, nome: str, email: str, id: int = None, saldo: float = 0.0, bio: str = None, 
                 habilidades: str = None, portfolio_url: str = None, telefone: str = None, cidade: str = None):
        super().__init__(nome, email, 'freelancer', id, saldo)
        self.bio = bio
        self.habilidades = habilidades
        self.portfolio_url = portfolio_url
        self.telefone = telefone
        self.cidade = cidade

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        if self.id is None:
           
            cursor.execute("INSERT INTO usuarios (nome, email, senha_hash, tipo, saldo) VALUES (?, ?, ?, ?, ?)",
                           (self.nome, self.email, self._senha_hash, self.tipo, self.saldo))
            self.id = cursor.lastrowid
            
            cursor.execute("""
                INSERT INTO freelancer_perfis (usuario_id, bio, habilidades, portfolio_url, telefone, cidade)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (self.id, self.bio, self.habilidades, self.portfolio_url, self.telefone, self.cidade))
        else:
            super().save() 
            
            cursor.execute("""
                UPDATE freelancer_perfis SET bio = ?, habilidades = ?, portfolio_url = ?, telefone = ?, cidade = ?
                WHERE usuario_id = ?
            """, (self.bio, self.habilidades, self.portfolio_url, self.telefone, self.cidade, self.id))

        conn.commit()
        conn.close()