class Autor():
    def __init__(self, id, nombres, apellidos, fecha_nacimiento=None):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento

    def nombre_completo(self):
        nombre_completo = "{0}, {1}".format(self.apellidos, self.nombres)
        return nombre_completo

