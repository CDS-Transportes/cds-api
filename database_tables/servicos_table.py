from peewee import Model, CharField, IntegerField, AutoField, ForeignKeyField

from database_tables.prestador_table import Prestador

import system_methods.database_connection as database

db = database.make_connect()

class BaseModel(Model):
    class Meta:
        database = db

class Servicos(BaseModel):
    
    serv_cod       = AutoField(unique=True)
    id_contratante = IntegerField()
    id_prestador   = ForeignKeyField(Prestador, backref='idpj')
    status         = CharField(max_length=12)






   
   
