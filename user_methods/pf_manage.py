from flask import request
import system_methods.response_build as response_build


"""
    Sumário:
        Métodos voltados ao gerenciamento de pessoas físicas do app CDS

    Métodos disponíves:
        register: Registra um novo usuário
        update: Atualiza informações de um usuário
        auth: autenticação de pessoa fisica na plataforma

    Códigos de retorno:
        register: 1XX
        update: 2XX
        auth: 3XX

"""


VALID_METHODS = ['register', 'update', 'auth']

class PFManage():

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

        elif(self.request_method == 'update'):

            if(self.http_method != 'POST'):
                return response_build.message_response(405, '200', 'METHOD_NOT_ALLOWED')
            else:
                return response_build.message_response(202, '002', 'METHOD_UPDATE')

        elif(self.request_method == 'auth'): 

            if(self.http_method != 'GET'):
                return response_build.message_response(405, '300', 'METHOD_NOT_ALLOWED')
            else:
                return response_build.message_response(202, '003', 'METHOD_AUTH')
        

    def register_method(self):

        self.nome     = self.request.form.get('nome')
        self.cpf      = self.request.form.get('cpf')
        self.email    = self.request.form.get('email')
        self.telefone = self.request.form.get('fone')


        if(self.nome == None or self.cpf == None or self.email == None or self.telefone == None):
            return response_build.message_response(406, '101', 'MISSING_INPUT')
        
        if(len(self.nome) > 40):
            return response_build.message_response(406, '102', 'INVALID_INPUT_NAME')
        
        if(len(self.cpf) != 11):
            return response_build.message_response(406, '103', 'INVALID_INPUT_CPF')
        
        if(len(self.email) > 40 or '@' not in self.email or '.' not in self.email):
            return response_build.message_response(406, '104', 'INVALID_INPUT_EMAIL')
        
        if(len(self.telefone) < 12 or len(self.telefone) > 13):
            return response_build.message_response(406, '105', 'INVALID_INPUT_FONE')


        return response_build.message_response(200, '106', 'REGISTER_SUCCESS')






    


