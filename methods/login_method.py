import system_methods.response_build as response_build
from system_methods.hash_string import get_hash
import system_methods.create_jwt as jwt

from database_tables.contratante_table import Contratante
from database_tables.prestador_table import Prestador
from database_tables.usuarios_tables import initAllTables, Usuarios


initAllTables()

def auth_prestador(email, senha):
    try:
        tmpUser = (
            Usuarios
            .select()
            .where(Usuarios.email == email).where(Usuarios.senha == get_hash(senha))
            .get()
            )

        nivel = tmpUser.nivel
        user_id = tmpUser.pj_id


        print(tmpUser.email)    
        
        tmpUser = (
            Prestador
            .select()
            .where(Prestador.id == tmpUser.pj_id)
            .get()
        )

        userJwt = jwt.create(str(user_id), tmpUser.email, tmpUser.nome, 1)

        return response_build.login_success('205', tmpUser.nome, nivel, userJwt, 1)

    except Exception as e:

        return response_build.message_response(401, '206', 'WRONG_USER_PASSWORD')

def auth_contratante(email, senha):
    try:
        tmpUser = (
            Usuarios
            .select(Usuarios.pf_id, Usuarios.nivel)
            .where(Usuarios.email == email and Usuarios.senha == get_hash(senha))
            .get()
            )

        nivel   = tmpUser.nivel
        user_id = tmpUser.pf_id

        tmpUser = (
            Contratante
            .select()
            .where(Contratante.id == tmpUser.pf_id)
            .get()
        )

        userJwt = jwt.create(str(user_id), tmpUser.email, tmpUser.nome, 0)

        return response_build.login_success('205', tmpUser.nome, nivel, userJwt, 0)

    except Exception as e:
        return response_build.message_response(401, '206', 'WRONG_USER_PASSWORD')


def login_method(request):
    email    = request.args.get('email')
    senha    = request.args.get('senha')
    type     = request.args.get('type')

    

    if(email == None or senha == None or type == None):
        return response_build.message_response(400, '201', 'MISSING_INPUT')


    if(len(email) > 40 or '@' not in email or '.' not in email):
        return response_build.message_response(400, '202', 'INVALID_INPUT_EMAIL')

    if(len(senha) < 8):
        return response_build.message_response(400, '203', 'INVALID_INPUT_SENHA')

    if(type != '0' and type != '1'):
            return response_build.message_response(400, '204', 'INVALID_INPUT_TYPE')

    
    if(type == '0'):
        return auth_contratante(email, senha)

    else:
        return auth_prestador(email, senha)
