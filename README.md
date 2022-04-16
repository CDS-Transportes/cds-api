# API CDS Transportes

- API em Flask (Python), para utilização na aplicação CDS Transporte

## Features


- Registro de usuário Contratante (PF) - Concluido
- Update de informações do usuário (PF) - Em progresso
- Autenticação de usuário (PF) - Em progresso

- Registro de usuário Contratante (PJ) - Concluido
- Registro de usuário Prestador (PJ) - Em progresso


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

| HTTP Status | Código | Mensagem | Descrição |
| ------ | ------ | ------ | ------ |
| 404 | 000 | METHOD_NOT_FOUND | O método solicitado não foi encontrado |


## [Retornos Método Register 1XX](https://github.com/CDS-Transportes/cds-api/tree/main/user_methods)



