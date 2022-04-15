from peewee import Model, CharField, DateTimeField, ForeignKeyField, IntegerField
from datetime import datetime

import system_methods.database_connection as database

from database_tables.pf_table import PessoaFisca
from database_tables.pj_tables import PessoaJuridica

db = database.make_connect()

class BaseModel(Model):
    class Meta:
        database = db

class UsuariosPF(BaseModel):

    pf_id        = ForeignKeyField(PessoaFisca, backref='idpf')

    email        = CharField(max_length=40, unique=True)
    senha        = CharField(max_length=32)

    nivel        = IntegerField(default=0)

    data_cadastro= DateTimeField(default=datetime.now)



class UsuariosPJ(BaseModel):

    pj_id        = ForeignKeyField(PessoaJuridica, backref='idpj')

    email        = CharField(max_length=40, unique=True)
    senha        = CharField(max_length=32)

    nivel        = IntegerField()

    data_cadastro= DateTimeField(default=datetime.now)



def initAllTables():
    db.create_tables([PessoaFisca, PessoaJuridica, UsuariosPF, UsuariosPJ])
   
