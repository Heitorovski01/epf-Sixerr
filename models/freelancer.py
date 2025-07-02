# models/freelancer.py
from models.usuario import Usuario

class Freelancer(Usuario):
    def __init__(self, nome: str, email: str, id: int = None):
        super().__init__(nome, email, 'freelancer', id)