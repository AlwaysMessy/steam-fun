

class BaseConfig(object):
    pass

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:Bindanzuizui123.@localhost:3306/steam-fun'

class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:Bindanzuizui123.@localhost:3306/steam-fun'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}