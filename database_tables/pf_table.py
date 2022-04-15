from peewee import Model, CharField, DateTimeField
from datetime import datetime

import system_methods.database_connection as database

db = database.make_connect()

class BaseModel(Model):
    class Meta:
        database = db

class PessoaFisca(BaseModel):

    nome         = CharField(max_length=40)
    email        = CharField(max_length=40)
    senha        = CharField(max_length=32)
    telefone     = CharField(max_length=13)
    cpf          = CharField(max_length=11)

    data_cadastro= DateTimeField(default=datetime.now)
   
