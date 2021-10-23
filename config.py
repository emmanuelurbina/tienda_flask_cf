from decouple import config
# Configuración básica de la aplicación
class Config:
    SECRET_KEY = "secret154546%Q^&>#213SA"


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""
    MYSQL_DB = "tienda_cf"
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587  # TLS Google
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'emmanuel.lucio.urbina@gmail.com'
    MAIL_PASSWORD = config('MAIL_PASSWORD')


class ProductionConfig(Config):
    DEBUG = False


config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'default': ProductionConfig
}
