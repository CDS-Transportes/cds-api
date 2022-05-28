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
| 400 | 108 | INVALID_DOC_FORMAT | O formtado do documento PF é invalido |
| 400 | 109 | INVALID_DOC_FORMAT | O formtado do documento PJ é invalido |
| 400 | 110 | EXIST_USER | Usuário e senha já cadastrados |
| 400 | 111 | EXIST_USER_DOC_TYPE | Já existe um usuário do tipo espeficiado para o documento enviado |
| 200 | 112 | REGISTER_SUCCESS | Registro realizado com sucesso |
| 400 | 113 | EXIST_CNPJ | O cnpj já está cadastrado |
| 400 | 114 | REGISTER_FAILED | Houve uma falha no registro |
| 400 | 115 | EXIST_EMAIL | O email já está cadastrado |
| 400 | 116 | EXIST_CPF | O cpf já está cadastrado |


## Retornos de login

| HTTP Status | Código | Menssagem | Descrição |
| ------ | ------ | ------ | ------ |
| 400 | 201 | MISSING_INPUT | Nem todos os inputs foram enviados |
| 400 | 202 | INVALID_INPUT_EMAIL | O campo email é inválido |
| 400 | 203 | INVALID_INPUT_SENHA | O campo senha é inválido |
| 200 | 204 | USER_INFO | O login foi realizado com sucesso |
| 401 | 205 | WRONG_USER_PASSWORD | Email e/ou senha inválidos |


## Retornos de registro/update de perfil

| HTTP Status | Código | Menssagem | Descrição |
| ------ | ------ | ------ | ------ |
| 400 | 301 | MISSING_INPUT | Nem todos os inputs foram enviados |
| 401 | 302 | INVALID_TOKEN | O token enviado não é válido |
| 400 | 303 | INVALID_USER_TYPE | O tipo do usuário é inválido |
| 201 | 304 | CREATED_PERFIL_SUCCESS| O pefil sem foto foi criado com sucesso |
| 201 | 305 | UPDATED_PERFIL_SUCCESS | A atualização sem foto do perfil foi concluida |
| 401 | 306 | IMAGE_UPLOAD_FAILED | Houve uma falha no upload da imagem |
| 201 | 307 | CREATED_PERFIL_SUCCESS| O pefil com foto foi criado com sucesso |
| 201 | 308 | UPDATED_PERFIL_SUCCESS | A atualização com foto do perfil foi concluida |


## Retornos de get pefil

| HTTP Status | Código | Menssagem | Descrição |
| ------ | ------ | ------ | ------ |
| 400 | 401 | MISSING_INPUT | Nem todos os inputs foram enviados |
| 401 | 402 | INVALID_TOKEN | O token enviado não é válido |
| 400 | 403 | INVALID_USER_TYPE | O tipo do usuário é inválido |
| 201 | 404 | PERFIL_INFO | O pefil foi retornado com sucesso |
| 201 | 405 | NON-EXISTENT_PROFILE | O perfil não existe |


## Retornos de index

| HTTP Status | Código | Menssagem | Descrição |
| ------ | ------ | ------ | ------ |
| 400 | 601 | MISSING_INPUT | Nem todos os inputs foram enviados |
| 401 | 602 | INVALID_TOKEN | O token enviado não é válido |
| 200 | 603 | PERFIS | Index de transportadores retornado com sucesso |
| 200 | 604 | PERFIS | Index de transportadores não retornou nenhum perfil |


## Retornos de collaborator

| HTTP Status | Código | Menssagem | Descrição |
| ------ | ------ | ------ | ------ |
| 400 | 701, 708, 716 e 720 | MISSING_INPUT | Nem todos os inputs foram enviados |
| 404 | 702 | METHOD_NOT_FOUND | O método solicitado não existe |
| 401 | 703 | INVALID_TOKEN | O token enviado não é válido |
| 405 | 704, 705, 706 e 707 | HTTP_METHOD_NOT_ALLOWED | O método http não é permitido |
| 400 | 709, 725 | INVALID_INPUT_NAME | O campo nome excedeu 40 caracteres |
| 400 | 710 | INVALID_INPUT_EMAIL | O campo email é inválido |
| 400 | 711, 723 | INVALID_INPUT_SENHA | O campo senha é inválido |
| 400 | 712, 724 | INVALID_INPUT_NIVEL | O campo nivel é inválido |
| 400 | 713, 717, 721, 727 | USER_NOT_AUTHORIZED | O usuário não possui permissão para a tarefa |
| 400 | 714 | EMAIL_IN_USE | O email já está em uso |
| 201 | 715 | COLLABORATOR_CREATED | Colaborador criado com sucesso |
| 200 | 718 | COLLABORATOR_DELETED | Colaborador deletado com sucesso |
| 400 | 719, 722 | COLLABORATOR_NOT_EXIST | Colaborador não existe |
| 200 | 726 | COLLABORATOR_UPDATED | Colaborador atualizado com sucesso |
| 200 | 728 | COLABORADORES | Lista de colaboradores retornada com sucesso |
| 200 | 729 | COLABORADORES | Nenhum colaborador retornado |


