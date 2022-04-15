from peewee import Model, CharField, DateTimeField, BooleanField, ForeignKeyField, IntegerField
from datetime import datetime

import system_methods.database_connection as database

db = database.make_connect()

class BaseModel(Model):
    class Meta:
        database = db

class PessoaJuridica(BaseModel):
    
    nome         = CharField(max_length=40)
    email        = CharField(max_length=40)
    senha        = CharField(max_length=32)
    telefone     = CharField(max_length=13)
    cnpj         = CharField(max_length=14)

    data_cadastro= DateTimeField(default=datetime.now)

    e_contratante= BooleanField()


class SubPessoaJuridica(BaseModel):
    
    id_pj     = ForeignKeyField(PessoaJuridica, backref='idpj')

    nome         = CharField(max_length=40)
    email        = CharField(max_length=40)
    senha        = CharField(max_length=32)

    papel        = IntegerField()
    
    data_cadastro= DateTimeField(default=datetime.now)

   
   
