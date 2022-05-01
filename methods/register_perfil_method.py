from flask import request

import system_methods.response_build as response_build
from system_methods.hash_string import get_hash
import system_methods.valid_jwt as jwt
from system_methods.upload_image import upload

from database_tables.perfil_table import Perfil_Prestador



def register_perfil(request):

    biografia    = request.form.get('bio')
    foto    = request.files.get('foto', '')
    uf      = request.form.get('uf')   
    cidade  = request.form.get('cidade')   
    token   = request.form.get('token')

    if(biografia == None or uf == None or cidade == None or token == None):
        return response_build.message_response(400, '301', 'MISSING_INPUT')
    


    isValidToeken, tokenData = jwt.valid(token)

    if(not isValidToeken):
        return response_build.message_response(401, '302', 'INVALID_TOKEN')

    if(tokenData['TYPE'] != 1):
        return response_build.message_response(401, '303', 'INVALID_USER_TYPE')


    
    if(foto == None or foto == ''):
        
        try:
            Perfil_Prestador(
                id_prestador = tokenData['ID'],
                biografia = biografia,
                uf        = uf,
                cidade    = cidade
            ).save()

            return response_build.message_response(201, '304', 'CREATED_PERFIL_SUCCESS')
        except:
            tempPerfil = Perfil_Prestador.update(
                biografia = biografia,
                uf        = uf,
                cidade    = cidade
            ).where(Perfil_Prestador.id_prestador == tokenData['ID']).execute()

            return response_build.message_response(201, '305', 'UPDATED_PERFIL_SUCCESS')

    else:
    
        isUploaded, link = upload(foto)

        
        if(not isUploaded):
            return response_build.message_response(400, '306', 'IMAGE_UPLOAD_FAILED')

        try:
            Perfil_Prestador(
                id_prestador = tokenData['ID'],
                biografia = biografia,
                uf        = uf,
                cidade    = cidade,
                foto      = link,
            ).save()

            return response_build.message_response(201, '307', 'CREATED_PERFIL_SUCCESS')
        except:
            Perfil_Prestador.update(
                biografia = biografia,
                uf        = uf,
                cidade    = cidade,
                foto      = link
            ).where(Perfil_Prestador.id_prestador == tokenData['ID']).execute()

            return response_build.message_response(201, '308', 'UPDATED_PERFIL_SUCCESS')

        

    