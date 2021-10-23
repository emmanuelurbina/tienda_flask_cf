from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask import render_template, request, redirect, url_for, flash, jsonify
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from .models.Modelo_libro import ModeloLibro
from .models.entities.Usuario import Usuario
from .models.entities.Libro import Libro
from .models.entities.Compra import Compra
from .models.Modelo_usuario import ModeloUsuario
from .models.Modelo_compra import ModeloCompra

from flask_mail import Mail

from .const import *
from .emails import confirmar_compra

app = Flask(__name__)
csrf = CSRFProtect(app)
db = MySQL(app)
login_manager = LoginManager(app)
mail = Mail(app)

@login_manager.user_loader
def load_user(id):
    return ModeloUsuario.get_by_id(db, id)


@app.route('/')
@login_required
def index():
    if current_user.is_authenticated:
        if current_user.tipo_usuario.id == 1:
            try:
                listar_libros = ModeloLibro.listar_libros_vendidos(db)
                data = {
                    'titulo': 'Libros vendidos',
                    'libros_vendidos': listar_libros
                }
                return render_template('index.html', data=data)
            except Exception as ex:
                print(ex)
                return render_template("errores/error.html", mensaje=format(ex))
        else:
            try:
                compras = ModeloCompra.listar_compras_user(db, current_user)
                data = {
                    'titulo': 'Mis Compras',
                    'compras': compras
                }
                return render_template('index.html', data=data)
            except Exception as ex:
                return render_template("errores/error.html", mensaje=format(ex))
       
    else:
        return redirect(url_for('login'))


@app.route('/libros')
@login_required
def listar_libros():
    if current_user.tipo_usuario.id == 2:
        # Solo clientes pueden acceder a la ruta
        try:
            libros = ModeloLibro.listar_libros(db)
            data = {
                'titulo': 'Listado de libros',
                'libros': libros,
            }
            return render_template("libros/listado_libros.html", data=data)
        except Exception as ex:
            return render_template("errores/error.html", mensaje=format(ex))
    else:
        return redirect(url_for('index'))


@app.route("/comprar_libro", methods=['POST'])
@login_required
def comprar_libro():
    data_request = request.get_json()
    data = {}
    try:
        libro = ModeloLibro.leer_libro(db, data_request['isbn'])
        compra = Compra(None, libro, current_user)
        confirmar_compra(app,mail, current_user, libro)
        data['exito'] = ModeloCompra.registrar_compra(db, compra)
        
    except Exception as ex:
        print(ex)
        data['msg'] = format(ex)
        data['exito'] = False

    return jsonify(data)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = Usuario(
            None, request.form['username'], request.form['password'], None)
        usuario_logeado = ModeloUsuario.login(db, usuario)
        if usuario_logeado != None:
            flash(LOGIN_SUCCESS, "success")
            login_user(usuario_logeado)
            return redirect(url_for('index'))
        else:
            flash(LOGIN_INVALID_CREDENTIALS, "error")
            return render_template('auth/login.html')
    return render_template('auth/login.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    flash(LOGOUT, "success")
    return redirect(url_for('login'))


@app.errorhandler(404)
def page_not_found(error):
    """
    Maneja error 404
    """
    return render_template('errors/404.html'), 404


@login_manager.unauthorized_handler
def unauthorized_callback():
    flash(LOGIN_REQUIRED, 'error')
    return redirect(url_for('login'))


def inicializar_app(config):
    """
    Funcion inicia app flask 
    toma un diccionaio de configuracion para
    aplicarlo a la hora de ejecutarlo
    """
    app.config.from_object(config)
    mail.init_app(app)
    csrf.init_app(app)
    return app
