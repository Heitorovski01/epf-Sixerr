# models/servico.py
import sqlite3
from data.database import get_db_connection

class Servico:
    def __init__(self, titulo: str, descricao: str, preco: float, freelancer_id: int, id: int = None):
        self.id, self.titulo, self.descricao, self.preco, self.freelancer_id = id, titulo, descricao, preco, freelancer_id

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("INSERT INTO servicos (titulo, descricao, preco, freelancer_id) VALUES (?, ?, ?, ?)",
                           (self.titulo, self.descricao, self.preco, self.freelancer_id))
            self.id = cursor.lastrowid
        else:
            cursor.execute("UPDATE servicos SET titulo=?, descricao=?, preco=?, freelancer_id=? WHERE id=?",
                           (self.titulo, self.descricao, self.preco, self.freelancer_id, self.id))
        conn.commit()
        conn.close()
        return self

    @staticmethod
    def find_all():
        conn = get_db_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM servicos")
        servicos_data = cursor.fetchall()
        conn.close()
        return [Servico(**data) for data in servicos_data]

    @staticmethod
    def find_by_id(servico_id: int):
        conn = get_db_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM servicos WHERE id = ?", (servico_id,))
        data = cursor.fetchone()
        conn.close()
        return Servico(**data) if data else None

    @staticmethod
    def find_by_freelancer_id(freelancer_id: int):
        conn = get_db_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM servicos WHERE freelancer_id = ?", (freelancer_id,))
        servicos_data = cursor.fetchall()
        conn.close()
        return [Servico(**data) for data in servicos_data]

    @staticmethod
    def delete_by_id(servico_id: int):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM servicos WHERE id = ?", (servico_id,))
        conn.commit()
        conn.close()