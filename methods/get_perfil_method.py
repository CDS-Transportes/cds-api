import imp
from flask import request

import system_methods.response_build as response_build
import system_methods.valid_jwt as jwt
from system_methods.upload_image import upload

from database_tables.perfil_table import Perfil_Prestador



def get_perfil(request):
    token = request.args.get('token')

    if(token == None):
        return response_build.message_response(400, '401', 'MISSING_INPUT')

    isValidToeken, tokenData = jwt.valid(token)

    if(not isValidToeken):
        return response_build.message_response(401, '402', 'INVALID_TOKEN')

    if(tokenData['TYPE'] != 1):
        return response_build.message_response(401, '403', 'INVALID_USER_TYPE')

    try:
        tempPerfil = Perfil_Prestador.select().where(Perfil_Prestador.id_prestador == tokenData['ID']).get()

        return response_build.pefil_success('404', tempPerfil.biografia, tempPerfil.uf, tempPerfil.cidade, tempPerfil.foto)


    except:
        return response_build.message_response(404, '405', 'NON-EXISTENT_PROFILE')