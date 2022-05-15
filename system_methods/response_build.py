from flask import jsonify

def message_response(status:int, cod:str, message:str):

    respJson = jsonify(
        COD=cod,
        MSG=message,
    )

    return respJson, status

def login_success(cod, nome, nivel, jwt, type):
    
    respJson = jsonify(
        {"COD": cod, "USER_INFO": {"TYPE": type,"NOME": nome, "NIVEL": nivel, "TOKEN": jwt}}

    )

    return respJson, 200


def pefil_success(cod, bio, uf, cidade, foto):
    
    respJson = jsonify(
        {"COD": cod, "PERFIL_INFO": {"BIO": bio,"UF": uf, "CIDADE": cidade, "FOTO": foto}}

    )

    return respJson, 200


def index_response(perfis, page):
    
    respJson = '[{"COD": "603", "PERFIS":{'
    
    for perfil in perfis:

        respJson += '{"BIO": "'+perfil.biografia+'", "FOTO": "'+perfil.foto+'", "UF": "'+perfil.uf+'", "CIDADE": "'+perfil.cidade+'"},'
        
    respJson += '}]'
    
    respJson = respJson.replace(',}]', '}]')
    
    return respJson, 200

def collaborators_response(collaborators):
    respJson = '[{"COD": "728", "COLABORADORES":{'

    for colab in collaborators:

        respJson += '{"NOME": "'+str(colab.nome)+'", "NIVEL": "'+str(colab.nivel)+'", "EMAIL": "'+str(colab.email)+'"},'

    respJson += '}]'

    respJson = respJson.replace(',}]', '}]')

    return respJson, 200