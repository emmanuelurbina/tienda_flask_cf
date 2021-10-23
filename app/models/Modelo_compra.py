from .entities.Compra import Compra
from .entities.Libro import Libro


class ModeloCompra():

    @classmethod
    def registrar_compra(self, db, compra):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO compra (uuid, libro_isbn, usuario_id) 
                        VALUES (uuid(), '{}', '{}')""". format(compra.libro.isbn, compra.usuario.id)
            cursor.execute(sql)
            db.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def listar_compras_user(cls, db, usuario):
        try:
            cursor = db.connection.cursor()
            sql = """ SELECT COM.fecha, LIB.isbn, LIB.titulo, LIB.precio FROM compra COM 
            JOIN Libro LIB
            ON COM.libro_isbn = LIB.isbn
            WHERE COM.usuario_id = '{0}'
            """.format(usuario.id)
            cursor.execute(sql)
            data=cursor.fetchall()
            compras = []

            for row in data:
                lib = Libro(row[1], row[2], None, None,  row[3])
                com = Compra(None, lib, usuario, row[0])
                compras.append(com)

            return compras
        except Exception as ex:
            raise Exception(ex)