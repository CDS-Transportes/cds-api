from peewee import Model, CharField, DateTimeField, BooleanField, ForeignKeyField, IntegerField
from datetime import datetime

import system_methods.database_connection as database

db = database.make_connect()

class BaseModel(Model):
    class Meta:
        database = db

class PessoaJuridica(BaseModel):
    
    nome         = CharField(max_length=40)
    telefone     = CharField(max_length=13)
    cnpj         = CharField(max_length=14)

    e_contratante= BooleanField()





   
   
