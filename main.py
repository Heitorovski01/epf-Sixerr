# main.py

from app import create_app
from data.database import init_db

if __name__ == '__main__':
    
    init_db()
    
    app = create_app()
    app.run(host='localhost', port=8080, debug=True, reloader=True)