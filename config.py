# import os

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    DEBUG = True
    PORT = 5000

class ProductionConfig(Config):
    DEBUG = False
    ASSETS_DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
    ASSETS_DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    ASSETS_DEBUG = True


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    ASSETS_DEBUG = True