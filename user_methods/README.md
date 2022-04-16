## Retornos Registro PF

| HTTP Status | Código | Mensagem | Descrição |
| ------ | ------ | ------ | ------ |
| 405 | 100 | METHOD_NOT_ALLOWED | Foi utilizado um método HTTP inválido |
| 400 | 101 | MISSING_INPUT | Nem todos os inputs foram enviados |
| 400 | 102 | INVALID_INPUT_NAME | O campo nome excedeu 40 caracteres |
| 400 | 103 | INVALID_INPUT_CPF | O campo cpf é menor ou maior do que 11 caracteres |
| 400 | 104 | INVALID_INPUT_EMAIL | O campo email é inválido |
| 400 | 105 | INVALID_INPUT_FONE | O campo fone é inválido |
| 400 | 106 | INVALID_INPUT_SENHA | O campo senha é inválido |
| 200 | 107 | REGISTER_SUCCESS | O registro foi efetuado com sucesso |
| 400 | 108 | EXIST_EMAIL | O email já está cadastrado |
| 400 | 109 | EXIST_CPF | O cpf já está cadastrado |
| 400 | 110 | REGISTER_FAILED | O registro falhou (Erro no DB) |

## Retornos Registro PJ

| HTTP Status | Código | Mensagem | Descrição |
| ------ | ------ | ------ | ------ |
| 405 | 100 | METHOD_NOT_ALLOWED | Foi utilizado um método HTTP inválido |
| 400 | 101 | MISSING_INPUT | Nem todos os inputs foram enviados |
| 400 | 102 | INVALID_INPUT_NAME | O campo nome excedeu 40 caracteres |
| 400 | 103 | INVALID_INPUT_CPF | O campo cpf é menor ou maior do que 11 caracteres |
| 400 | 104 | INVALID_INPUT_EMAIL | O campo email é inválido |
| 400 | 105 | INVALID_INPUT_FONE | O campo fone é inválido |
| 400 | 106 | INVALID_INPUT_SENHA | O campo senha é inválido |
| 400 | 107 | INVALID_USER_TYPE | O tipo de usuário especificado é inválido |
| 200 | 108 | REGISTER_SUCCESS | O registro foi efetuado com sucesso |
| 400 | 109 | EXIST_EMAIL | O email já está cadastrado |
| 400 | 110 | EXIST_CNPJ | O cnpj já está cadastrado |
| 400 | 111 | REGISTER_FAILED | O registro falhou (Erro no DB) |
