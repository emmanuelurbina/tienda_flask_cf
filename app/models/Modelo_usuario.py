from .entities.Usuario import Usuario
from .entities.Tipo_usuario import TipoUsuario


class ModeloUsuario():

    @classmethod
    def login(cls, db, usuario):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, usuario, password 
                        FROM usuario 
                        WHERE usuario='{0}'""".format(usuario.usuario)
            cursor.execute(sql)
            data = cursor.fetchone()
            if data != None: # valida que la consulta tenga valores
                coincide = Usuario.valid_password(data[2], usuario.password)
                if coincide:
                    usuario_logeado = Usuario(data[0], data[1], None, None)
                    return usuario_logeado
                else:
                    return None
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(cls, db, id):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT USU.id, USU.usuario, TIP.id, TIP.nombre
                        FROM usuario USU
                        JOIN tipousuario TIP
                        ON USU.tipo_usuario_id = TIP.id
                        WHERE USU.id='{0}' """.format(id)
            cursor.execute(sql)
            data = cursor.fetchone()
            tipo_usuario = TipoUsuario(data[2], data[3])
            usuario_logeado = Usuario(data[0], data[1], None, tipo_usuario)
            return usuario_logeado
        except Exception as ex:
            raise Exception(ex)
