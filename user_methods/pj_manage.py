from flask import request

"""
    Sumário:
        Métodos voltados ao gerenciamento de pessoas júridicas do app CDS

    Métodos disponíves:
        register: Registra um novo usuário PJ

    Códigos de retorno:
        register: 1XX

"""


VALID_METHODS = ['register']

class PJManage():

    def __init__(self, request:request):
        
        self.methods        = VALID_METHODS
        self.http_method    = request.method
        self.request        = request

        if(self.http_method == 'POST'):
            self.method = self.request.form.get('method')
        else:
            self.method = self.request.form.get('method')

        