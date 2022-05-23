from database_tables.servicos_table import Servicos

from system_methods.valid_jwt import valid

import system_methods.response_build as response_build

METHOD_AVAILABLE = ['request','create','update','list','accept','cancel']

def request_method(request, token):

    if(token['NIVEL'] != 0 and token['NIVEL'] != 2):
        return response_build.message_response(401, '511', 'USER_NOT_AUTHORIZED')


    try:
        transportadora = request.json[0]['transportadora']
        endr_inicial   = request.json[0]['endr_inicial']
        endr_final     = request.json[0]['endr_final']
        altura         = request.json[0]['altura']
        largura        = request.json[0]['largura']
        comprimento    = request.json[0]['comprimento']
        peso           = request.json[0]['peso']
    except:
        return response_build.message_response(400, '512', 'MISSING_INPUT')

    try:
        tempServico = Servicos(
            id_contratante = token['ID'],
            id_prestador   = transportadora,
            endr_inical    = endr_inicial,
            endr_final     = endr_final,
            altura         = altura,
            largura        = largura,
            comprimento    = comprimento,
            peso           = peso,
            status         = 0
        ).save()
    except Exception as e:
        return response_build.message_response(500, '513', 'REQUEST_ERROR')

    return response_build.message_response(201, '514', 'SERVICE_REQUESTED')



def list_method(request, token):
    if(token['NIVEL'] != 0 and token['NIVEL'] != 2):
        return response_build.message_response(401, '515', 'USER_NOT_AUTHORIZED')

    if(token['TYPE'] == 1):
        tempServicos = (
            Servicos.select()
            .where(Servicos.id_prestador == token['ID'])
        )
    else:
        tempServicos = (
            Servicos.select()
            .where(Servicos.id_contratante == token['ID'])
        )

    return response_build.services_response(tempServicos)


def create_method(request, token):
    return 'a'


def update_method(request):
    return 'a'


def accept_method(request):
    return 'a'


def cancel_method(request):
    return 'a'

def direct_services_method(request):

    if(request.method == 'POST'):
        try:
            method = request.json[0]['method']
            token  = request.json[0]['token']
        except:
            method = request.form.get('method')
            token  = request.form.get('token')

    else:
        method = request.args.get('method')
        token  = request.args.get('token')


    if(method == None or token == None):
        return response_build.message_response(400, '501', 'MISSING_INPUT')


    if(method not in METHOD_AVAILABLE):
        return response_build.message_response(404, '502', 'METHOD_NOT_FOUND')


    isValid, tokenDecoded = valid(token)
    if(not isValid):
        return response_build.message_response(401, '503', 'INVALID_TOKEN')


    if(method == 'create'):
        if(request.method != 'POST'):
            return response_build.message_response(405, '504', 'METHOD_NOT_ALLOWED')
        
        return create_method(request, tokenDecoded)

    elif(method == 'update'):
        if(request.method != 'POST'):
            return response_build.message_response(405, '505', 'METHOD_NOT_ALLOWED')

        return update_method(request)

    elif(method == 'list'):
        if(request.method != 'GET'):
            return response_build.message_response(405, '506', 'METHOD_NOT_ALLOWED')

        return list_method(request, tokenDecoded)


    elif(method == 'request'):
        if(request.method != 'POST'):
            return response_build.message_response(405, '508', 'METHOD_NOT_ALLOWED')

        return request_method(request, tokenDecoded)

    elif(method == 'accept'):
        if(request.method != 'GET'):
            return response_build.message_response(405, '509', 'METHOD_NOT_ALLOWED')

        return accept_method(request)

    elif(method == 'cancel'):
        if(request.method != 'GET'):
            return response_build.message_response(405, '510', 'METHOD_NOT_ALLOWED')

        return cancel_method(request)
