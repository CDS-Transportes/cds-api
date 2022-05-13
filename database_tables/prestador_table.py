from peewee import Model, CharField, BooleanField

import system_methods.database_connection as database

db = database.make_connect()

class BaseModel(Model):
    class Meta:
        database = db

class Prestador(BaseModel):
    
    nome         = CharField(max_length=40)
    email        = CharField(max_length=40, unique=True)
    telefone     = CharField(max_length=13)
    cnpj         = CharField(max_length=14, unique=True)

    e_contratante= BooleanField(default=False)





   
   
