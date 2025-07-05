# app.py (Versão Final com Permissões Corrigidas)

import os
import sqlite3
from bottle import Bottle, static_file, request, redirect, template, TEMPLATE_PATH, response, abort

def create_app():
    app = Bottle()

    project_root = os.path.dirname(os.path.abspath(__file__))
    views_path = os.path.join(project_root, 'views')
    TEMPLATE_PATH.insert(0, views_path)

    from controllers.user_controller import UserController
    from controllers.servico_controller import ServicoController
    
    user_ctrl = UserController()
    servico_ctrl = ServicoController()

    SECRET_KEY = "uma-chave-secreta-muito-forte-e-dificil"

    # --- DECORATORS ---
    def login_required(fn):
        def wrapper(*args, **kwargs):
            user_id = request.get_cookie("user_id", secret=SECRET_KEY)
            if user_id:
                kwargs['user_id'] = int(user_id)
                return fn(*args, **kwargs)
            redirect("/login")
        return wrapper

    def role_required(role_requerido):
        def decorator(fn):
            def wrapper(*args, **kwargs):
                user_id = request.get_cookie("user_id", secret=SECRET_KEY)
                if not user_id:
                    redirect("/login")
                    return
                
                usuario = Usuario.find_by_id(int(user_id))
                if usuario and usuario.tipo == role_requerido:
                    kwargs['user_id'] = int(user_id)
                    return fn(*args, **kwargs)
                
                abort(403, "Acesso Negado: Você não tem permissão para visualizar esta página.")
            return wrapper
        return decorator
    
    # --- ROTA DE ERRO ---
    @app.error(403)
    def error403(error):
        user_id = request.get_coo_cookie("user_id", secret=SECRET_KEY)
        usuario = Usuario.find_by_id(int(user_id)) if user_id else None
        return template('error.tpl', error=error, usuario=usuario)

    # --- ROTAS ---
    from models.servico import Servico
    from models.usuario import Usuario

    @app.route('/static/<filepath:path>')
    def server_static(filepath): return static_file(filepath, root='./static')

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

    @app.route('/freelancer/<freelancer_id:int>')
    def perfil_publico_freelancer(freelancer_id):
        return user_ctrl.show_public_profile(freelancer_id)
    @app.route('/login', method='GET')
    def login_page(): return user_ctrl.login()

    @app.route('/login', method='POST')
    def do_login():
        usuario = user_ctrl.do_login()
        if usuario:
            response.set_cookie("user_id", str(usuario.id), secret=SECRET_KEY, path='/')
            redirect('/')
        else:
            return template('login.tpl', error="Email ou senha inválidos.")

    @app.route('/register', method='GET')
    def register_page(): return user_ctrl.register()

    @app.route('/register', method='POST')
    def do_register():
        sucesso = user_ctrl.do_register()
        if sucesso:
            redirect('/login')
        else:
            return

    @app.route('/logout')
    @login_required
    def do_logout(**kwargs):
        user_ctrl.logout()
        redirect('/')

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
        user_ctrl.save_profile(user_id)
        redirect('/perfil')

    @app.route('/usuario/deletar')
    @login_required
    def deletar_usuario_self(user_id):
        user_ctrl.delete_self(user_id)
        redirect('/')

    
    @app.route('/carteira', method='GET')
    @login_required
    def carteira_page(user_id): return user_ctrl.show_wallet(user_id)

    @app.route('/carteira', method='POST')
    @login_required
    def processar_transacao(user_id): return user_ctrl.process_transaction(user_id)

    @app.route('/meus-pedidos')
    @role_required('cliente') 
    def meus_pedidos(user_id):
        return user_ctrl.show_my_orders(user_id)

    @app.route('/servicos/contratar/<servico_id:int>', method='POST')
    @role_required('cliente') 
    def contratar(servico_id, user_id):
        return servico_ctrl.contratar_servico(servico_id, user_id)

    @app.route('/servicos/meus')
    @role_required('freelancer') 
    def meus_servicos(user_id): return servico_ctrl.list_my_services(user_id)

    @app.route('/servicos/novo', method='GET')
    @role_required('freelancer') 
    def novo_servico_form(user_id): return servico_ctrl.add_service_form(user_id)

    @app.route('/servicos/editar/<servico_id:int>', method='GET')
    @role_required('freelancer') 
    def editar_servico_form(servico_id, user_id): return servico_ctrl.edit_service_form(servico_id, user_id)

    @app.route('/servicos/salvar', method='POST')
    @role_required('freelancer') 
    def salvar_servico(user_id): return servico_ctrl.save_service(user_id)

    @app.route('/servicos/deletar/<servico_id:int>')
    @role_required('freelancer')
    def deletar_servico(servico_id, **kwargs): return servico_ctrl.delete_service(servico_id)

    @app.route('/minhas-vendas')
    @role_required('freelancer')
    def minhas_vendas(user_id):
        return user_ctrl.show_my_sales(user_id)
    
    @app.route('/cliente/<cliente_id:int>')
    @login_required
    def perfil_publico_cliente(cliente_id, **kwargs):
        return user_ctrl.show_public_client_profile(cliente_id)
    
    return app