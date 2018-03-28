class Config(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:cxYv23gm9PjYfMLtWd@livelyrics.cnfthxsaxcoe.us-east-2.rds.amazonaws.com/livelyrics'


class Development(Config):
    DEBUG = False
    SQLALCHEMY_ECHO = False
    CLIENT_URL = "http://127.0.0.1:5000"


class Production(Config):
    DEBUG = False
    SQLALCHEMY_ECHO = False
    CLIENT_URL = "http://18.188.140.44"


app_config = {
    'development': Development,
    'production': Production
}
