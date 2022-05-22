from peewee import Model, CharField, IntegerField, AutoField, ForeignKeyField, TextField, FloatField

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
    endr_inical    = TextField()
    endr_final     = TextField()
    altura         = FloatField()
    largura        = FloatField()
    comprimento    = FloatField()
    peso           = FloatField()
    status         = CharField(max_length=12)






   
   
