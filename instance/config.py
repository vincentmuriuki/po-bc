import os

class Config(Object):
	os.getenviron('SECRET_KEY')
	CSRF_TOKEN = True

class Development(Config):
	DEBUG = True

class Production(Config):
	DEBUG = False

class Testing(Config):
	Debug = True

config = {
	Development: 'development',
	Production: 'production',
	Testing: 'testing'
}