# API CDS Transportes

- API em Flask (Python), para utilização na aplicação CDS Transporte

## Features


- Registro de usuário (PF) - Em progresso
- Update de informações do usuário (PF) - Em progresso
- Autenticação de usuário (PF) - Em progresso

- Registro de usuário (PJ) - Em progresso


## Instalação

Requer [Python](https://www.python.org/downloads/) v3.9+ para ser executado.


```sh
git clone https://github.com/CDS-Transportes/cds-api.git
pip install -r requirements.txt
python main.py
```

## Observações

- Para fins de testes, está sendo utilizado o SQLite como SGBD

## Retornos Sistema 0XX

| HTTP Status | Código | Menssagem | Descrição |
| ------ | ------ |
| 404 | 000 | METHOD_NOT_FOUND | O método solicitado não foi encontrado |


## Retornos Método Register 1XX (PF)

| HTTP Status | Código | Menssagem | Descrição |
| ------ | ------ |
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


