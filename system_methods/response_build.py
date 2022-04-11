from flask import jsonify

def message_response(status:int, cod:str, message:str):
    respJson = '[{"COD": "'+cod+'", "MSG": "'+message+'"}]'

    respJson = jsonify(
        COD=cod,
        MSG=message,
    )

    return respJson, status