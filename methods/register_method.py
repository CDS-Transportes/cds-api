from flask import request
import json

import system_methods.response_build as response_build
from system_methods.hash_string import get_hash

from database_tables.contratante_table import Contratante
from database_tables.prestador_table import Prestador
from database_tables.usuarios_tables import initAllTables, Usuarios

from methods.login_method import login_system


initAllTables()

#Método para registro de usuários prestadores
def register_prestador(nome, email, telefone, doc, senha):
    try:    

            try:
                tempUser = Prestador(
                    nome    = nome,
                    email   = email,
                    telefone= telefone,
                    cnpj     = doc
                )
                tempUser.save()
            except  Exception as e:

                login_attemp = login_system(email, senha)
                if(", 200" in str(login_attemp)):
                    return response_build.message_response(400, '110', 'EXIST_USER')
                        

                tempUser = Prestador.select(Prestador.id).where(Prestador.cnpj == doc).get()
                tempAuthUser = Usuarios.select().where(Usuarios.pj_id == tempUser.id).get()
    
                if(tempAuthUser.type == 1):
                    return response_build.message_response(400, '111', 'EXIST_USER_DOC_TYPE')
                else:

                    tempAuthUser = Usuarios(
                    pj_id   = tempUser.id,
                    email   = email,
                    nome    = nome,
                    senha   = get_hash(senha),
                    type    = 1
                    )
                    tempAuthUser.save()
             
                return response_build.message_response(200, '112', 'REGISTER_SUCCESS')
            try:
                login_attemp = login_system(email, senha)

                if(", 200" in str(login_attemp)):
                    return response_build.message_response(400, '110', 'EXIST_USER')

                tempAuthUser = Usuarios(
                    pj_id   = tempUser.id,
                    email   = email,
                    nome    = nome,
                    senha   = get_hash(senha),
                    type    = 1
                )
                tempAuthUser.save()
            except:
                return response_build.message_response(400, '110', 'EXIST_USER')
        
            return response_build.message_response(200, '112', 'REGISTER_SUCCESS')

    except  Exception as e:
    
        if(("UNIQUE" in str(e) and "doc" in str(e)) or ("Duplicate" in str(e) and "doc" in str(e))):
            return response_build.message_response(400, '113', 'EXIST_CNPJ')

        return response_build.message_response(400, '114', 'REGISTER_FAILED')



def register_contratante_pj(nome, email, telefone, doc, senha):
    try:    

            try:
                tempUser = Contratante(
                    nome    = nome,
                    email   = email,
                    telefone= telefone,
                    doc     = doc
                )
                tempUser.save()
            except  Exception as e:

                login_attemp = login_system(email, senha)
                if(", 200" in str(login_attemp)):
                    return response_build.message_response(400, '110', 'EXIST_USER')
                        

                tempUser = Contratante.select().where(Contratante.doc == doc).get()
                tempAuthUser = Usuarios.select().where(Usuarios.type == 2).where(Usuarios.pj_id == tempUser.id).get()


                if(tempAuthUser.type == 2):
                    return response_build.message_response(400, '111', 'EXIST_USER_DOC_TYPE')
                else:

                    tempAuthUser = Usuarios(
                    pj_id   = tempUser.id,
                    email   = email,
                    nome    = nome,
                    senha   = get_hash(senha),
                    type    = 2
                    )
                    tempAuthUser.save()
                return response_build.message_response(200, '112', 'REGISTER_SUCCESS')
            try:
                login_attemp = login_system(email, senha)

                if(", 200" in str(login_attemp)):
                    return response_build.message_response(400, '110', 'EXIST_USER')

                tempAuthUser = Usuarios(
                    pj_id   = tempUser.id,
                    email   = email,
                    nome    = nome,
                    senha   = get_hash(senha),
                    type    = 2
                )
                tempAuthUser.save()
            except:
                return response_build.message_response(400, '110', 'EXIST_USER')
            return response_build.message_response(200, '112', 'REGISTER_SUCCESS')

    except  Exception as e:

        if(("UNIQUE" in str(e) and "doc" in str(e)) or ("Duplicate" in str(e) and "doc" in str(e))):
            return response_build.message_response(400, '113', 'EXIST_CNPJ')

        return response_build.message_response(400, '114', 'REGISTER_FAILED')

#Método para registro de usuários contratantes pf
def register_contratante_pf(nome, email, telefone, doc, senha):
    try:
            tempUser = Contratante(
                nome    = nome,
                email   = email,
                telefone= telefone,
                doc     = doc
            )
            tempUser.save()

            try:
                tempAuthUser = Usuarios(
                    pf_id   = tempUser.id,
                    email   = email,
                    nome    = nome,
                    senha   = get_hash(senha),
                    type    = 0
                )
                tempAuthUser.save()
            except:
                Usuarios.update({Usuarios.pf_id: tempUser.id}).where(Usuarios.email == email).execute()
     

            return response_build.message_response(200, '112', 'REGISTER_SUCCESS')

    except  Exception as e:

        if(("UNIQUE" in str(e) and "email" in str(e)) or ("Duplicate" in str(e) and "email" in str(e))):
            return response_build.message_response(400, '115', 'EXIST_EMAIL')

        if(("UNIQUE" in str(e) and "doc" in str(e)) or ("Duplicate" in str(e) and "doc" in str(e))):
            return response_build.message_response(400, '116', 'EXIST_CPF')

        return response_build.message_response(400, '114', 'REGISTER_FAILED')




def register_method(request):
        
        try:                        
            nome     = request.json[0]['nome']
            doc      = request.json[0]['doc']
            email    = request.json[0]['email']
            telefone = request.json[0]['fone']           
            type     = request.json[0]['type']
            senha    = request.json[0]['senha']
            
        except:
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

        if(type != '0' and type != '1' and type != '2'):
            return response_build.message_response(400, '107', 'INVALID_INPUT_TYPE')

        if(type == '0'):
            if(len(doc) == 11):
                return register_contratante_pf(nome, email, telefone, doc, senha)
            else:
                return response_build.message_response(400, '108', 'INVALID_DOC_FORMAT')
        else:
            if(len(doc) != 14):
                return response_build.message_response(400, '109', 'INVALID_DOC_FORMAT') 
  
            if(type == '1'):
                return register_prestador(nome, email, telefone, doc, senha)  
            else:
                return register_contratante_pj(nome, email, telefone, doc, senha)
            

        