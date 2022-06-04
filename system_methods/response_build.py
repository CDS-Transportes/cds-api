from flask import jsonify
from system_methods.get_transp_info import get_transp_info

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

    isReturned = False
    
    respJson = '{"COD": "603", "PERFIS":['
    
    for perfil in perfis:

        nome, id = get_transp_info(perfil.id_prestador_id)

        isReturned = True

        respJson += '{"BIO": "'+perfil.biografia+'", "FOTO": "'+perfil.foto+'", "UF": "'+perfil.uf+'", "CIDADE": "'+perfil.cidade+'", "NOME": "'+nome+'", "ID": "'+id+'"},'
        

    if(isReturned):
        respJson += ']'
        respJson = respJson.replace(',]', ']}')
            
    else:
        respJson = respJson.replace("603", "604")
        respJson += ']}'

    return respJson, 200




def collaborators_response(collaborators):

    isReturned = False

    respJson = '{"COD": "728", "COLABORADORES":['

    for colab in collaborators:

        isReturned = True

        respJson += '{"NOME": "'+str(colab.nome)+'", "NIVEL": "'+str(colab.nivel)+'", "EMAIL": "'+str(colab.email)+'"},'

    if(isReturned):
        respJson += ']'
        respJson = respJson.replace(',]', ']}')
            
    else:
        respJson = respJson.replace("728", "729")
        respJson += ']}'


    return respJson, 200


def services_response(services):

    isReturned = False

    respJson = '[{"COD": "516", "SERVICOS":['

    for servico in services:

        isReturned = False

        respJson += '{"SERV_COD": "'+str(servico.serv_cod)+'", "ID_PRESTADOR": "'+str(servico.id_prestador)+'", "ENDR_INICIAL": "'+str(servico.endr_inical)+'", "ENDR_FINAL": "'+str(servico.endr_final)+'", "STATUS": "'+str(servico.status)+'"},'


    if(isReturned):
        respJson += ']'
        respJson = respJson.replace(',]', ']}')
            
    else:
        respJson = respJson.replace("516", "517")
        respJson += ']}'

    return respJson, 200