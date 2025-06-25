from app import create_app
from bottle import run, default_app

import controllers.user_controller

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)