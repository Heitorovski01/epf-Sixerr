from app import create_app
from data.database import init_db 

if __name__ == '__main__':
    print("--- INICIANDO APLICAÇÃO: Verificando banco de dados... ---")
    
    init_db() 
    
    print("--- BANCO DE DADOS PRONTO. Criando aplicação... ---")
    app = create_app()
    app.run(host='localhost', port=8080, debug=True, reloader=True)