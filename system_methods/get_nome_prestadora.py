from database_tables.prestador_table import Prestador


def get_nome(id):

    nome = Prestador.select().where(Prestador.id == id).get().nome

    return str(nome)