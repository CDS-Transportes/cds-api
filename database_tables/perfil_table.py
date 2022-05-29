from enum import unique
from peewee import Model, CharField, ForeignKeyField, TextField

from database_tables.prestador_table import Prestador

import system_methods.database_connection as database

db = database.make_connect()

class BaseModel(Model):
    class Meta:
        database = db

class Perfil_Prestador(BaseModel):

    id_prestador = ForeignKeyField(Prestador, backref='idpj', unique=True)
    biografia    = TextField(null=True)
    foto         = CharField(max_length=160, default="http://127.0.0.1:5000/public/perfil/default.webp")
    uf           = CharField(max_length=2, null=True)
    cidade       = CharField(max_length=20, null=True)



   
