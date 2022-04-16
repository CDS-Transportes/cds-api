from peewee import Model, CharField, DateTimeField, ForeignKeyField, IntegerField
from datetime import datetime

import system_methods.database_connection as database

from database_tables.contratante_table import Contratante
from database_tables.prestador_table import Prestador
from database_tables.perfil_table import Perfil_Prestador
from database_tables.servicos_table import Servicos


db = database.make_connect()

class BaseModel(Model):
    class Meta:
        database = db

class Usuarios(BaseModel):

    pf_id        = ForeignKeyField(Contratante, backref='idpf', null=True)
    pj_id        = ForeignKeyField(Prestador, backref='idpj', null=True)

    email        = CharField(max_length=40, unique=True)
    senha        = CharField(max_length=32)

    nivel        = IntegerField(default=0)

    data_cadastro= DateTimeField(default=datetime.now)





def initAllTables():
    db.create_tables([Contratante, Prestador, Usuarios, Servicos, Perfil_Prestador])
   
