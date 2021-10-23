class Libro():

    def __init__(self, isbn, titulo, autor, edicion_a, precio):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.edicion_a = edicion_a
        self.precio = precio
        self.unidades_vendidas = 0