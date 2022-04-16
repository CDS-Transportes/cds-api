from peewee import Model, CharField, ForeignKeyField, TextField

from database_tables.prestador_table import Prestador

import system_methods.database_connection as database

db = database.make_connect()

class BaseModel(Model):
    class Meta:
        database = db

class Perfil_Prestador(BaseModel):

    id_prestador = ForeignKeyField(Prestador, backref='idpj')
    biografia    = TextField(null=True)
    foto         = CharField(max_length=32, null=True)
    uf           = CharField(max_length=2, null=True)
    cidade       = CharField(max_length=20, null=True)



   
