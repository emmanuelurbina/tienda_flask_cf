from app import inicializar_app
from config import config

#se inicializa la aplicacion flask
configuration = config['development']
app = inicializar_app(configuration)

# comentario de vs en linea
if __name__ == '__main__':
    """
    se corre la aplicacion flask en un puerto y host 
    personalziado
    """
    app.run(host='0.0.0.0', port=3000)