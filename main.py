# main.py

from app import create_app
from data.database import init_db

if __name__ == '__main__':
    # Inicializa o banco de dados (cria as tabelas se não existirem)
    init_db()
    
    # Cria e Roda a aplicação a partir da nossa "fábrica" em app.py
    app = create_app()
    app.run(host='localhost', port=8080, debug=True, reloader=True)