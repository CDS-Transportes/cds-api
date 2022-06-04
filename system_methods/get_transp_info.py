from database_tables.prestador_table import Prestador


def get_transp_info(id):

    prestadora = Prestador.select().where(Prestador.id == id).get()
    nome       = prestadora.nome
    id         = prestadora.id

    return str(nome), str(id)