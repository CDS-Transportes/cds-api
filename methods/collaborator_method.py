from flask import request

from database_tables.usuarios_tables import Usuarios

import system_methods.response_build as response_build

from system_methods.valid_jwt import valid
from system_methods.hash_string import get_hash

METHOD_AVAILABLE = ['create','delete','update','list']


def create_method(request, tokenDecoded):
    if(request.method != 'POST'):
        return response_build.message_response(405, '704', 'HTTP_METHOD_NOT_ALLOWED')


    try:
        nome  = request.json[0]['nome']
        email = request.json[0]['email']
        senha = request.json[0]['senha']
        nivel = request.json[0]['nivel']
    except:
        nome  = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        nivel = request.form.get('nivel')

    
    if(nome == None or email == None or senha == None or nivel == None):
        return response_build.message_response(400, '708', 'MISSING_INPUT')
    if(len(nome) > 40):
        return response_build.message_response(400, '709', 'INVALID_INPUT_NAME')
    if(len(email) > 40):
        return response_build.message_response(400, '710', 'INVALID_INPUT_EMAIL')
    if(len(senha) < 8):
        return response_build.message_response(400, '711', 'INVALID_INPUT_SENHA')
    if(nivel != '0' and nivel != '1' and nivel != '2'):
        return response_build.message_response(400, '712', 'INVALID_INPUT_NIVEL')
    if(tokenDecoded['NIVEL'] != 0):
        return response_build.message_response(401, '713', 'USER_NOT_AUTHORIZED')


    try:
        tmpAuthUser = (
                Usuarios
                .select()
                .where(Usuarios.email == email)
                .get()
            )
        
        inUse = True
    except:
        inUse = False
 
    if(inUse):
        return response_build.message_response(400, '714', 'EMAIL_IN_USE')

    tmpAuthUser = Usuarios(
        nome  = nome,
        email = email,
        senha = get_hash(senha),
        nivel = nivel,
        pj_id = tokenDecoded['ID'],
        type  = tokenDecoded['TYPE']
    ).save()

    return response_build.message_response(201, '715', 'COLLABORATOR_CREATED')


def delete_method(request, tokenDecoded):

    if(request.method != 'GET'):
        return response_build.message_response(405, '705', 'HTTP_METHOD_NOT_ALLOWED')

    email = request.args.get('email')

    if(email == None):
        return response_build.message_response(400, '716', 'MISSING_INPUT')

    if(tokenDecoded['NIVEL'] != 0):
        return response_build.message_response(401, '717', 'USER_NOT_AUTHORIZED')


    tmpDeletedUser = Usuarios.delete().where(Usuarios.pj_id == tokenDecoded['ID']).where(Usuarios.email == email)
    tmpDeletedUser = tmpDeletedUser.execute()

    if(tmpDeletedUser > 0):
        return response_build.message_response(200, '718', 'COLLABORATOR_DELETED')
    else:
        return response_build.message_response(400, '719', 'COLLABORATOR_NOT_EXIST')
    

def update_method(request, tokenDecoded):
    if(request.method != 'POST'):
        return response_build.message_response(405, '706', 'HTTP_METHOD_NOT_ALLOWED')
    
    try:
        email = request.json[0]['email']
    except:
        email = request.form.get('email')

    try:
        nivel = request.json[0]['nivel']
    except:
        nivel = request.form.get('nivel')

    try:
        nome = request.json[0]['nome']
    except:
        nome = request.form.get('nome')

    try:
        senha = request.json[0]['senha']
    except:
        senha = request.form.get('senha')


    if(email == None):
        return response_build.message_response(400, '720', 'MISSING_INPUT')

    if(tokenDecoded['NIVEL'] != 0):
        return response_build.message_response(401, '721', 'USER_NOT_AUTHORIZED')

    try:
        tmpAuthUser = Usuarios.select().where(Usuarios.email == email).where(Usuarios.pj_id == tokenDecoded['ID']).get()
    except:
        return response_build.message_response(400, '722', 'COLLABORATOR_NOT_EXIST')

    if(senha != None):

        if(len(senha) < 8):
            return response_build.message_response(400, '723', 'INVALID_INPUT_SENHA')

        Usuarios.update(senha = get_hash(senha)).where(Usuarios.id == tmpAuthUser.id).execute()
    
    if(nivel != None):

        if(nivel != '0' and nivel != '1' and nivel != '2'):
            return response_build.message_response(400, '724', 'INVALID_INPUT_NIVEL')

        Usuarios.update(nivel = nivel).where(Usuarios.id == tmpAuthUser.id).execute()

    if(nome != None):
        if(len(nome) > 40):
            return response_build.message_response(400, '725', 'INVALID_INPUT_NAME')

        Usuarios.update(nome = nome).where(Usuarios.id == tmpAuthUser.id).execute()
    
    return response_build.message_response(200, '726', 'COLLABORATOR_UPDATED')

def list_method(request, tokenDecoded):
    if(request.method != 'GET'):
        return response_build.message_response(405, '707', 'HTTP_METHOD_NOT_ALLOWED')

    if(tokenDecoded['NIVEL'] != 0):
        return response_build.message_response(401, '727', 'USER_NOT_AUTHORIZED')

    tmpUsers = Usuarios.select().where(Usuarios.pj_id == tokenDecoded['ID']).execute()

    return response_build.collaborators_response(tmpUsers)

def direct_collaborator_method(request):

    if(request.method == 'POST'):
        try:
            token  = request.json[0]['token']
            method = request.json[0]['method']
        except:
            token  = request.form.get('token')
            method = request.form.get('method')

    else:
        token  = request.args.get('token')
        method = request.args.get('method')

    
    if(token == None or method == None):
        return response_build.message_response(400, '701', 'MISSING_INPUT')
    
    if(method.lower() not in METHOD_AVAILABLE):
        return response_build.message_response(404, '702', 'METHOD_NOT_FOUND')

    isValid, tokenDecoded = valid(token)

    if(not isValid):
        return response_build.message_response(401, '703', 'INVALID_TOKEN')


    if(method == 'create'):
        return create_method(request, tokenDecoded)

    elif(method == 'delete'):
        return delete_method(request, tokenDecoded)

    elif(method == 'update'):
        return update_method(request, tokenDecoded)

    elif(method == 'list'):
        return list_method(request, tokenDecoded)


    return 'a'