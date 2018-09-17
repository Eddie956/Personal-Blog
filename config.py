import os

# Class-based application configuration


class Config:
    """
    General configuration parent class
    """
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://a:mango@localhost/blog'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD')
    ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME')

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SENDER_EMAIL = 'mutugieddie3@gmail.com'

    @staticmethod
    def init_app(app):
        pass

    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    BASIC_AUTH_USERNAME = 'Sarah'
    BASIC_AUTH_pASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('postgresql+psycopg2://a:mango@localhost/blog')
    
    DEBUG = True


class DevConfig(Config):
   
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://a:mango@localhost/blog'



class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://a:mango@localhost/blog'
    
    DEBUG = True



config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
