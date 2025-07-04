# app.py (Versão com lógica de autenticação corrigida)

import os
import sqlite3
from bottle import Bottle, static_file, request, redirect, template, TEMPLATE_PATH, response

def create_app():
    """Cria e configura a instância da aplicação Bottle."""
    app = Bottle()

    # Configuração do caminho para os templates (views)
    project_root = os.path.dirname(os.path.abspath(__file__))
    views_path = os.path.join(project_root, 'views')
    TEMPLATE_PATH.insert(0, views_path)

    # --- Importações dos Controllers ---
    from controllers.user_controller import UserController
    from controllers.servico_controller import ServicoController
    
    # --- Instâncias dos Controllers ---
    user_ctrl = UserController()
    servico_ctrl = ServicoController()

    # --- Chave Secreta ---
    SECRET_KEY = "uma-chave-secreta-muito-forte-e-dificil"

    # --- Decorator de Autenticação ---
    def login_required(fn):
        def wrapper(*args, **kwargs):
            user_id = request.get_cookie("user_id", secret=SECRET_KEY)
            if user_id:
                kwargs['user_id'] = int(user_id)
                return fn(*args, **kwargs)
            redirect("/login")
        return wrapper

    # --- ROTAS ---

    # -- Rota Estática --
    @app.route('/static/<filepath:path>')
    def server_static(filepath):
        return static_file(filepath, root='./static')

    # -- Rotas Públicas --
    from models.servico import Servico
    from models.usuario import Usuario

    @app.route('/')
    def home():
        servicos = Servico.find_all()
        user_id = request.get_cookie("user_id", secret=SECRET_KEY)
        usuario = Usuario.find_by_id(int(user_id)) if user_id else None
        return template('home.tpl', servicos=servicos, usuario=usuario)

    @app.route('/servicos/detalhe/<servico_id:int>')
    def detalhe_servico(servico_id):
        user_id = request.get_cookie("user_id", secret=SECRET_KEY)
        return servico_ctrl.show_service_details(servico_id, user_id)

    # -- Rotas de Autenticação (Com Lógica Corrigida) --
    @app.route('/login', method='GET')
    def login_page(): 
        return user_ctrl.login()

    @app.route('/login', method='POST')
    def do_login():
        # 1. Controller apenas valida e retorna o utilizador
        usuario = user_ctrl.do_login()
        if usuario:
            # 2. A Rota cria o cookie e redireciona
            response.set_cookie("user_id", str(usuario.id), secret=SECRET_KEY, path='/')
            redirect('/')
        else:
            # 3. A Rota mostra a página de erro
            return template('login.tpl', error="Email ou senha inválidos.")

    @app.route('/register', method='GET')
    def register_page(): 
        return user_ctrl.register()

    @app.route('/register', method='POST')
    def do_register():
        # Controller tenta registar e retorna True/False
        sucesso = user_ctrl.do_register()
        if sucesso:
            # Rota redireciona em caso de sucesso
            redirect('/login')
        else:
            # Se der erro, o próprio controller já devolve a página de registo com a mensagem
            return

    @app.route('/logout')
    @login_required
    def do_logout(**kwargs):
        user_ctrl.logout()
        redirect('/')

    # -- Rotas de Perfil (Protegidas) --
    @app.route('/perfil')
    @login_required
    def perfil(user_id):
        return user_ctrl.show_profile(user_id)

    @app.route('/perfil/editar', method='GET')
    @login_required
    def editar_perfil_form(user_id):
        return user_ctrl.edit_profile_form(user_id)

    @app.route('/perfil/editar', method='POST')
    @login_required
    def salvar_perfil(user_id):
        # Chama o controller para salvar os dados
        sucesso = user_ctrl.save_profile(user_id)
        
        # Se o save foi bem-sucedido, redireciona para a página de perfil
        if sucesso:
            redirect('/perfil')

    @app.route('/usuario/deletar')
    @login_required
    def deletar_usuario_self(user_id):
        user_ctrl.delete_self(user_id)
        redirect('/')

    # -- Rotas de Serviços do Freelancer (Protegidas) --
    @app.route('/servicos/meus')
    @login_required
    def meus_servicos(user_id): return servico_ctrl.list_my_services(user_id)

    @app.route('/servicos/novo', method='GET')
    @login_required
    def novo_servico_form(user_id): return servico_ctrl.add_service_form(user_id)

    @app.route('/servicos/editar/<servico_id:int>', method='GET')
    @login_required
    def editar_servico_form(servico_id, user_id): return servico_ctrl.edit_service_form(servico_id, user_id)

    @app.route('/servicos/salvar', method='POST')
    @login_required
    def salvar_servico(user_id): return servico_ctrl.save_service(user_id)

    @app.route('/carteira', method='GET')
    @login_required
    def carteira_page(user_id):
        return user_ctrl.show_wallet(user_id)

    @app.route('/carteira', method='POST')
    @login_required
    def processar_transacao(user_id):
        return user_ctrl.process_transaction(user_id)

    @app.route('/servicos/deletar/<servico_id:int>')
    @login_required
    def deletar_servico(servico_id, **kwargs): return servico_ctrl.delete_service(servico_id)
    
    @app.route('/servicos/contratar/<servico_id:int>', method='POST')
    @login_required
    def contratar(servico_id, user_id):
        cliente = Usuario.find_by_id(user_id)
        if cliente.tipo != 'cliente':
            return redirect(f"/servicos/detalhe/{servico_id}?error=Apenas clientes podem contratar serviços.")
        
        return servico_ctrl.contratar_servico(servico_id, user_id)

    @app.route('/meus-pedidos')
    @login_required
    def meus_pedidos(user_id):
        # Verificação para garantir que só clientes acedam
        cliente = Usuario.find_by_id(user_id)
        if cliente.tipo != 'cliente':
            return redirect('/')
        return user_ctrl.show_my_orders(user_id)

    return app