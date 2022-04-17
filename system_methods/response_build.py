from flask import jsonify

def message_response(status:int, cod:str, message:str):

    respJson = jsonify(
        COD=cod,
        MSG=message,
    )

    return respJson, status

def login_success(cod, id, nome, telefone, doc, nivel):
    
    respJson = jsonify(
        {"COD": cod, "USER_INFO": {"ID": id, "NOME": nome, "FONE": telefone, "DOC": doc, "NIVEL": nivel}}

    )

    return respJson, 200
