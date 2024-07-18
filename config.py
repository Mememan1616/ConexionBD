import os 
from sqlalchemy import create_engine
import urllib

#Se encarga de enviar los datos encriptados, y evitar que cierre la sesion
class Config(object):
    SECRET_KEY ='Clave Unica'
    SESION_COOKIE_SECURE=False


#hacemos la conexion a la base de datos y se actualiza constamente los cambios en la vista
class DevelopmentConfig(Config):
    DEBUG=True 
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://Alex:Rodriguez.10@127.0.0.1/bdhumani'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
