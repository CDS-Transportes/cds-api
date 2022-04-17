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
