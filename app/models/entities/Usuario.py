from flask_login.mixins import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Usuario(UserMixin):
    def __init__(self, id, usuario, password, tipo_usuario):
        self.id = id
        self.usuario = usuario
        self.password = password
        self.tipo_usuario = tipo_usuario

    @classmethod
    def valid_password(cls,encriptado, password):
        coincide = check_password_hash(encriptado, password)
        return coincide
