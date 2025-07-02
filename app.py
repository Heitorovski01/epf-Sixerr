# app.py (Versão Completa e Correta para colar)

import sqlite3
from bottle import Bottle, static_file, request, redirect, template

def create_app():
    """Cria e configura a instância da aplicação Bottle."""
    app = Bottle()

    # --- Importações dos Controllers ---
    from controllers.user_controller import UserController
    from controllers.servico_controller import ServicoController
    
    # --- Instâncias dos Controllers ---
    user_ctrl = UserController()
    servico_ctrl = ServicoController()

    # --- Chave Secreta (deve vir do config.py no futuro) ---
    SECRET_KEY = "sua-chave-secreta-muito-longa-e-aleatoria"

    # --- Decorator de Autenticação (Ponto Extra) ---
    def login_required(fn):
        def wrapper(*args, **kwargs):
            user_id = request.get_cookie("user_id", secret=SECRET_KEY)
            if user_id:
                # Passa o user_id para a função, se ela precisar
                kwargs['user_id'] = int(user_id)
                return fn(*args, **kwargs)
            redirect("/login")
        return wrapper

    # --- Rotas Estáticas ---
    @app.route('/static/<filepath:path>')
    def server_static(filepath):
        return static_file(filepath, root='./static')

    # --- Rotas de Autenticação ---
    @app.route('/login', method='GET')
    def login_page(): return user_ctrl.login()

    @app.route('/login', method='POST')
    def do_login(): return user_ctrl.do_login()

    @app.route('/register', method='GET')
    def register_page(): return user_ctrl.register()

    @app.route('/register', method='POST')
    def do_register(): return user_ctrl.do_register()

    @app.route('/logout')
    @login_required
    def do_logout(**kwargs): return user_ctrl.logout()

    # --- Rota Principal (Página Inicial Pública) ---
    from models.servico import Servico
    from models.usuario import Usuario
    @app.route('/')
    def home():
        servicos = Servico.find_all()
        user_id = request.get_cookie("user_id", secret=SECRET_KEY)
        usuario = Usuario.find_by_id(int(user_id)) if user_id else None
        return template('home.tpl', servicos=servicos, usuario=usuario)

    # --- ROTAS DE SERVIÇOS (PROTEGIDAS) ---
    
    # Lista os serviços do freelancer logado
    @app.route('/servicos/meus')
    @login_required
    def meus_servicos(user_id):
        return servico_ctrl.list_my_services(user_id)

    # Mostra o formulário para adicionar um novo serviço
    @app.route('/servicos/novo', method='GET')
    @login_required
    def novo_servico_form(**kwargs): 
        return servico_ctrl.add_service_form()

    # Mostra o formulário para editar um serviço existente
    @app.route('/servicos/editar/<servico_id:int>', method='GET')
    @login_required
    def editar_servico_form(servico_id, **kwargs): 
        return servico_ctrl.edit_service_form(servico_id)

    # Salva o serviço (novo ou editado) no banco de dados
    @app.route('/servicos/salvar', method='POST')
    @login_required
    def salvar_servico(user_id):
        return servico_ctrl.save_service(user_id)

    # Apaga um serviço
    @app.route('/servicos/deletar/<servico_id:int>')
    @login_required
    def deletar_servico(servico_id, **kwargs): 
        return servico_ctrl.delete_service(servico_id)

    # --- Retorna a aplicação configurada ---
    return app