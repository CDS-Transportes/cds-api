from flask import request

import system_methods.response_build as response_build
from system_methods.valid_jwt import valid
from database_tables.perfil_table import Perfil_Prestador


def get_index(request):
    
    token = request.args.get('token')
    page  = request.args.get('page')
    
    if(token == None):
        return response_build.message_response(400, '601', 'MISSING_INPUT')
    
    isValidToken, decoded = valid(token)
    
    if(not isValidToken):
        return response_build.message_response(401, '602', 'INVALID_TOKEN')
    
    
    if(page == None):
        page = 1
        
    pageStart = 0
    pageFinal = 0    
        
    if(page == 1):
        pageStart = 1
        pageFinal = 10
    else:
        pageStart = int(str((int(page)-1))+"1")
        pageFinal = (int(page)*10)

    tempPerfil = Perfil_Prestador.select().order_by(Perfil_Prestador.id).paginate(pageStart, pageFinal) 
    
    for perfil in tempPerfil:
        print(perfil)
    
    return response_build.index_response(tempPerfil, page)