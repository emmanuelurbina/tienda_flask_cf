from .entities.Autor import Autor
from .entities.Libro import Libro


class ModeloLibro():

    @classmethod
    def listar_libros(cls, db):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT LIB.isbn, LIB.titulo, LIB.edicion_a, LIB.precio, AUT.nombres, AUT.apellidos 
                    FROM libro LIB 
                    JOIN autor AUT
                    ON LIB.autor_id = AUT.id
                    ORDER BY LIB.titulo ASC"""
            cursor.execute(sql)
            data = cursor.fetchall()
            libros = []
            for row in data:
                aut = Autor(0, row[4], row[5])
                lib = Libro(row[0], row[1], aut, row[2], row[3])
                libros.append(lib)
            return libros

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def listar_libros_vendidos(cls, db):
        try:
            cursor = db.connection.cursor()
            sql = """ SELECT COM.libro_isbn, LIB.titulo, LIB.precio, COUNT(COM.libro_isbn) AS unidades_vendidas FROM compra COM 
            JOIN libro LIB
            ON COM.libro_isbn = LIB.isbn
            GROUP BY COM.libro_isbn
            ORDER BY 4 DESC, 2 ASC
            """
            cursor.execute(sql)
            data = cursor.fetchall()
            ventas = []

            for row in data:
                lib = Libro(row[0], row[1], None, None, row[2])
                lib.unidades_vendidas = int(row[3])
                ventas.append(lib)
            return ventas
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def leer_libro(cls, db, isbn):
        try:
            cursor = db.connection.cursor()
            sql = """ SELECT isbn, titulo, edicion_a, precio  FROM libro WHERE isbn = '{0}' """.format(
                isbn)
            cursor.execute(sql)
            data = cursor.fetchone()
            libro = Libro(data[0], data[1], None, data[2], data[3])
            return libro
        except Exception as ex:
            raise Exception(ex)
