import email
from flask import request

import system_methods.response_build as response_build
from system_methods.hash_string import get_hash

from database_tables.contratante_table import Contratante
from database_tables.prestador_table import Prestador
from database_tables.usuarios_tables import initAllTables, Usuarios

"""
    Sumário:
        Métodos voltados ao gerenciamento de jurificas do app CDS

    Métodos disponíves:
        register: Registra um novo usuário
        update: Atualiza informações de um usuário
        auth: autenticação de pessoa fisica na plataforma

    Códigos de retorno:
        register: 1XX


"""

initAllTables()

VALID_METHODS = ['register']

class PJManage():

    def __init__(self, request:request):

        self.methods        = VALID_METHODS
        self.http_method    = request.method
        self.request        = request

        if(self.http_method == 'POST'):
            self.request_method = self.request.form.get('method')
        else:
            self.request_method = self.request.args.get('method')


    def direct_method(self):

        if(self.request_method not in self.methods):
            return response_build.message_response(404, '000', 'METHOD_NOT_FOUND')

        if(self.request_method == 'register'):

            if(self.http_method != 'POST'):
                return response_build.message_response(405, '100', 'METHOD_NOT_ALLOWED')
            else:
                return self.register_method()

        

    def register_method(self):

        self.nome     = self.request.form.get('nome')
        self.cnpj     = self.request.form.get('cnpj')
        self.email    = self.request.form.get('email')
        self.telefone = self.request.form.get('fone')
        self.senha    = self.request.form.get('senha')
        self.type  = self.request.form.get('type')

        if(self.nome == None or self.cnpj == None or self.email == None or self.telefone == None or self.senha == None or self.type == None):
            return response_build.message_response(400, '101', 'MISSING_INPUT')
        
        if(len(self.nome) > 40):
            return response_build.message_response(400, '102', 'INVALID_INPUT_NAME')
        
        if(len(self.cnpj) != 14):
            return response_build.message_response(400, '103', 'INVALID_INPUT_CNPJ')
        
        if(len(self.email) > 40 or '@' not in self.email or '.' not in self.email):
            return response_build.message_response(400, '104', 'INVALID_INPUT_EMAIL')
        
        if(len(self.telefone) < 12 or len(self.telefone) > 13):
            return response_build.message_response(400, '105', 'INVALID_INPUT_FONE')

        if(len(self.senha) < 8):
            return response_build.message_response(400, '106', 'INVALID_INPUT_SENHA')

        if(self.type != '0' and self.type != '1'):
            return response_build.message_response(400, '107', 'INVALID_USER_TYPE')
        
        if(self.type == '0'):
            self.type = False
        
        if(self.type == '1'):
            self.type = True

        try:
            tempUser = Prestador(
                nome          = self.nome,
                email         = self.email,
                telefone      = self.telefone,
                cnpj          = self.cnpj,
                e_contratante = self.type
            )
            tempUser.save()


            tempAuthUser = Usuarios(
                pj_id   = tempUser.id,
                email   = self.email,
                senha   = get_hash(self.senha)
            )
            tempAuthUser.save()
            
            return response_build.message_response(200, '108', 'REGISTER_SUCCESS')

        except  Exception as e:
            if(("UNIQUE" in str(e) and "email" in str(e)) or ("Duplicate" in str(e) and "email" in str(e))):
                return response_build.message_response(400, '109', 'EXIST_EMAIL')
            if(("UNIQUE" in str(e) and "cnpj" in str(e)) or ("Duplicate" in str(e) and "cnpj" in str(e))):
                return response_build.message_response(400, '110', 'EXIST_CNPJ')

            return response_build.message_response(400, '111', 'REGISTER_FAILED')

    

        






    


