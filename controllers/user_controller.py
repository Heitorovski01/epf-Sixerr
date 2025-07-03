# controllers/user_controller.py
from bottle import request, response, redirect, template
from models.usuario import Usuario
from models.freelancer import Freelancer
from models.cliente import Cliente

class UserController:
    def register(self): return template('register.tpl', error=None)
    def login(self): return template('login.tpl', error=None)

    def do_register(self):
        nome, email, senha, tipo = request.forms.get('nome'), request.forms.get('email'), request.forms.get('senha'), request.forms.get('tipo_usuario')
        if not all([nome, email, senha, tipo]): return template('register.tpl', error="Todos os campos são obrigatórios.")
        if Usuario.find_by_email(email): return template('register.tpl', error="Este e-mail já está em uso.")
        
        UserClass = Freelancer if tipo == 'freelancer' else Cliente
        novo_usuario = UserClass(nome=nome, email=email)
        novo_usuario.set_senha(senha)
        novo_usuario.save()
        redirect('/login')

    def do_login(self):
        email, senha = request.forms.get('email'), request.forms.get('senha')
        if not all([email, senha]): return template('login.tpl', error="Email e senha são obrigatórios.")
        
        usuario = Usuario.find_by_email(email)
        if usuario and usuario.check_senha(senha):
            response.set_cookie("user_id", str(usuario.id), secret="troque-por-uma-frase-muito-longa-e-segura-depois", path='/')
            redirect('/')
        else:
            return template('login.tpl', error="E-mail ou senha inválidos.")

    def logout(self):
        response.delete_cookie("user_id", path='/')
        redirect('/login')