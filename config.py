class Config(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:cxYv23gm9PjYfMLtWd@livelyrics.cnfthxsaxcoe.us-east-2.rds.amazonaws.com/livelyrics'


class Development(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True


class Production(Config):
    DEBUG = False
    SQLALCHEMY_ECHO = False


app_config = {
    'development': Development,
    'production': Production
}
