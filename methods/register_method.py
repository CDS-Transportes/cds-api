from flask import request

import system_methods.response_build as response_build
from system_methods.hash_string import get_hash

from database_tables.contratante_table import Contratante
from database_tables.prestador_table import Prestador
from database_tables.usuarios_tables import initAllTables, Usuarios

initAllTables()

#Método para registro de usuários prestadores
def register_prestador(nome, email, telefone, doc, senha):
    try:
            tempUser = Prestador(
                nome          = nome,
                email         = email,
                telefone      = telefone,
                cnpj          = doc,
            )
            tempUser.save()


            tempAuthUser = Usuarios(
                pj_id   = tempUser.id,
                email   = email,
                senha   = get_hash(senha)
            )
            tempAuthUser.save()
            
            return response_build.message_response(200, '108', 'REGISTER_SUCCESS')

    except  Exception as e:

        if(("UNIQUE" in str(e) and "email" in str(e)) or ("Duplicate" in str(e) and "email" in str(e))):
            return response_build.message_response(400, '109', 'EXIST_EMAIL')

        if(("UNIQUE" in str(e) and "doc" in str(e)) or ("Duplicate" in str(e) and "doc" in str(e))):
            return response_build.message_response(400, '111', 'EXIST_CNPJ')

        return response_build.message_response(400, '112', 'REGISTER_FAILED')



#Método para registro de usuários contratantes
def register_contratante(nome, email, telefone, doc, senha):
    try:
            tempUser = Contratante(
                nome    = nome,
                email   = email,
                telefone= telefone,
                doc     = doc
            )
            tempUser.save()

            tempAuthUser = Usuarios(
                pf_id   = tempUser.id,
                email   = email,
                senha   = get_hash(senha)
            )
            tempAuthUser.save()
            
            return response_build.message_response(200, '108', 'REGISTER_SUCCESS')

    except  Exception as e:

        if(("UNIQUE" in str(e) and "email" in str(e)) or ("Duplicate" in str(e) and "email" in str(e))):
            return response_build.message_response(400, '109', 'EXIST_EMAIL')

        if(("UNIQUE" in str(e) and "doc" in str(e)) or ("Duplicate" in str(e) and "doc" in str(e))):
            return response_build.message_response(400, '110', 'EXIST_CPF')

        return response_build.message_response(400, '112', 'REGISTER_FAILED')




def register_method(request):

        nome     = request.form.get('nome')
        doc      = request.form.get('doc')
        email    = request.form.get('email')
        telefone = request.form.get('fone')
        senha    = request.form.get('senha')
        type     = request.form.get('type')

        if(nome == None or doc == None or email == None or telefone == None or senha == None or type == None):
            return response_build.message_response(400, '101', 'MISSING_INPUT')
        
        if(len(nome) > 40):
            return response_build.message_response(400, '102', 'INVALID_INPUT_NAME')
        
        if(len(doc) != 11 and len(doc) != 14):
            return response_build.message_response(400, '103', 'INVALID_INPUT_DOC')
        
        if(len(email) > 40 or '@' not in email or '.' not in email):
            return response_build.message_response(400, '104', 'INVALID_INPUT_EMAIL')
        
        if(len(telefone) < 12 or len(telefone) > 13):
            return response_build.message_response(400, '105', 'INVALID_INPUT_FONE')

        if(len(senha) < 8):
            return response_build.message_response(400, '106', 'INVALID_INPUT_SENHA')

        if(type != '0' and type != '1'):
            return response_build.message_response(400, '107', 'INVALID_INPUT_TYPE')

        if(type == '0'):
            return register_contratante(nome, email, telefone, doc, senha)
        else:
            return register_prestador(nome, email, telefone, doc, senha)       

        