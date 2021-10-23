import datetime
class Compra():

    def __init__(self, uuid, libro, usuario, fecha=None):
        self.uuid = uuid
        self.libro = libro
        self.usuario = usuario
        self.fecha = fecha

    def formated_date(self):
        return datetime.datetime.strftime(self.fecha, '%d/%m/%Y - %H:%M:%S')