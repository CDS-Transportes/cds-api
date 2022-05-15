import system_methods.response_build as response_build
from system_methods.hash_string import get_hash
import system_methods.create_jwt as jwt

from database_tables.contratante_table import Contratante
from database_tables.prestador_table import Prestador
from database_tables.usuarios_tables import initAllTables, Usuarios


initAllTables()

def auth(email, senha):
    try:
        tmpAuthUser = (
            Usuarios
            .select()
            .where(Usuarios.email == email).where(Usuarios.senha == get_hash(senha))
            .get()
        )

        user_type = tmpAuthUser.type

        if(user_type == 0):
            tmpUser = (
            Contratante
                .select()
                .where(Contratante.id == tmpAuthUser.pf_id_id)
                .get()
            )
        elif(user_type == 1):
            tmpUser = (
            Prestador
                .select()
                .where(Prestador.id == tmpAuthUser.pj_id_id)
                .get()
            )
        else:
            tmpUser = (
                Contratante
                .select()
                .where(Contratante.id == tmpAuthUser.pj_id_id)
                .get()
            )

        user_id = tmpUser.id

        userJwt = jwt.create(str(user_id), tmpAuthUser.email, tmpAuthUser.nome, tmpAuthUser.type, tmpAuthUser.nivel)

        return response_build.login_success('201', tmpAuthUser.nome, tmpAuthUser.nivel, userJwt, tmpAuthUser.type)

    except Exception as e:
        return response_build.message_response(401, '205', 'WRONG_USER_PASSWORD')


def login_method(request):
    email    = request.args.get('email')
    senha    = request.args.get('senha')

    if(email == None or senha == None):
        return response_build.message_response(400, '201', 'MISSING_INPUT')


    if(len(email) > 40 or '@' not in email or '.' not in email):
        return response_build.message_response(400, '202', 'INVALID_INPUT_EMAIL')

    if(len(senha) < 8):
        return response_build.message_response(400, '203', 'INVALID_INPUT_SENHA')

    return auth(email, senha)



def login_system(email, senha):
    return auth(email, senha)

