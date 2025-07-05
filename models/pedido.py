import sqlite3
from data.database import get_db_connection

class Pedido:
    def __init__(self, preco_pago: float, cliente_id: int, servico_id: int, id: int = None, data_contratacao=None):
        self.id = id
        self.data_contratacao = data_contratacao
        self.preco_pago = preco_pago
        self.cliente_id = cliente_id
        self.servico_id = servico_id

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO pedidos (preco_pago, cliente_id, servico_id) VALUES (?, ?, ?)",
            (self.preco_pago, self.cliente_id, self.servico_id)
        )
        self.id = cursor.lastrowid
        conn.commit()
        conn.close()

    @staticmethod
    def find_by_cliente(cliente_id: int):
        conn = get_db_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT p.*, s.titulo as servico_titulo, s.freelancer_id
            FROM pedidos p
            JOIN servicos s ON p.servico_id = s.id
            WHERE p.cliente_id = ?
            ORDER BY p.data_contratacao DESC
        """, (cliente_id,))
        
        pedidos = cursor.fetchall()
        conn.close()
        return pedidos

    @staticmethod
    def find_by_freelancer(freelancer_id: int):
        conn = get_db_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT p.*, s.titulo as servico_titulo, c.nome as cliente_nome, c.id as cliente_id
            FROM pedidos p
            JOIN servicos s ON p.servico_id = s.id
            JOIN usuarios c ON p.cliente_id = c.id
            WHERE s.freelancer_id = ?
            ORDER BY p.data_contratacao DESC
        """, (freelancer_id,))
        
        pedidos = cursor.fetchall()
        conn.close()
        return pedidos