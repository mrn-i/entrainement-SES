import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    # Psycopg : Python adapter of PostgreSQSL database
    # Adapt Python types to PostgreSQSL types.
    # While doing so, database will be connected to the application.
    # This will occure into models.py.

'''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format( \
        dbuser=os.environ['DBUSER'],
        dbpass=os.environ['DBPASS'],
        dbhost=os.environ['DBHOST'],
        dbname=os.environ['DBNAME'])
    print(SQLALCHEMY_DATABASE_URI)
'''

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    #SQLALCHEMY_DATABASE_URI = 'postgres://zfjgsayxgjeago:a46aab50bd8ff8d9585a5c3aae90143e4ff93f9e993b7c1c31524b84748175af@ec2-54-247-169-129.eu-west-1.compute.amazonaws.com:5432/dohirlotb7iqt'
    os.environ['DBUSER'] = "zfjgsayxgjeago"
    os.environ['DBPASS'] = "a46aab50bd8ff8d9585a5c3aae90143e4ff93f9e993b7c1c31524b84748175af"
    os.environ['DBHOST'] = "ec2-54-247-169-129.eu-west-1.compute.amazonaws.com"
    os.environ['DBNAME'] = "dohirlotb7iqt"
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format( \
        dbuser=os.environ['DBUSER'],
        dbpass=os.environ['DBPASS'],
        dbhost=os.environ['DBHOST'],
        dbname=os.environ['DBNAME'])



class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:azeR1234@localhost/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEVELOPMENT = True
    DEBUG = True

    os.environ['DBUSER'] = "postgres"
    os.environ['DBPASS'] = "azeR1234"
    os.environ['DBHOST'] = "localhost"
    os.environ['DBNAME'] = "postgres"
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format( \
        dbuser=os.environ['DBUSER'],
        dbpass=os.environ['DBPASS'],
        dbhost=os.environ['DBHOST'],
        dbname=os.environ['DBNAME'])


class TestingConfig(Config):
    TESTING = True
