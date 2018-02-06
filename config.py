class Config(object):
    	DEBUG = False
    	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:cxYv23gm9PjYfMLtWd@livelyrics.cnfthxsaxcoe.us-east-2.rds.amazonaws.com/livelyrics'


class LocalDevelopment(Config):
    	DEBUG = True
    	SQALCHEMY_ECHO = True


class Production(Config):
    	DEBUG = False
    	SQALCHEMY_ECHO = False


class ServerDevelopment(Config):
	DEBUG = True
    	SQALCHEMY_ECHO = True


app_config = {
    	'local': LocalDevelopment,
	'server': ServerDevelopment,
	'production': Production
}
