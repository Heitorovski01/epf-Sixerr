# models/cliente.py
from models.usuario import Usuario

class Cliente(Usuario):
    def __init__(self, nome: str, email: str, id: int = None):
        super().__init__(nome, email, 'cliente', id)