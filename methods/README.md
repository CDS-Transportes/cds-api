## Retornos de register

| HTTP Status | Código | Menssagem | Descrição |
| ------ | ------ | ------ | ------ |
| 400 | 101 | MISSING_INPUT | Nem todos os inputs foram enviados |
| 400 | 102 | INVALID_INPUT_NAME | O campo nome excedeu 40 caracteres |
| 400 | 103 | INVALID_INPUT_DOC | O campo doc é inválido  |
| 400 | 104 | INVALID_INPUT_EMAIL | O campo email é inválido |
| 400 | 105 | INVALID_INPUT_FONE | O campo fone é inválido |
| 400 | 106 | INVALID_INPUT_SENHA | O campo senha é inválido |
| 200 | 107 | INVALID_INPUT_TYPE | O tipo de usuário é inválido |
| 200 | 108 | REGISTER_SUCCESS | O registro foi efetuado com sucesso |
| 400 | 109 | EXIST_EMAIL | O email já está cadastrado |
| 400 | 110 | EXIST_CPF | O cpf já está cadastrado |
| 400 | 111 | EXIST_CNPJ | O cnpj já está cadastrado |
| 400 | 112 | REGISTER_FAILED | O registro falhou (Erro no DB) |


## Retornos de login

| HTTP Status | Código | Menssagem | Descrição |
| ------ | ------ | ------ | ------ |
| 400 | 201 | MISSING_INPUT | Nem todos os inputs foram enviados |
| 400 | 202 | INVALID_INPUT_EMAIL | O campo email é inválido |
| 400 | 203 | INVALID_INPUT_SENHA | O campo senha é inválido |
| 400 | 204 | INVALID_INPUT_TYPE | O tipo de usuário é inválido |
| 200 | 205 | USER_INFO | O login foi realizado com sucesso |
| 400 | 206 | WRONG_USER_PASSWORD | Email e/ou senha inválidos |
