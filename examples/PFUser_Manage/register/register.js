
function validInputs(){
    if($("#nome").val() == "" || $("#email").val() == "" || $("#cpf").val() == "" || $("#senha").val() == "" || $("#confirmsenha").val() == "" || $("#fone").val() == ""){
        return true
    }

    if($("#senha").val() != $("#confirmsenha").val()){
        return true
    }

    return false
}


function verifyResult(result){
    let codReturn = result['COD']

    switch(codReturn){
        case '100':
            alert("Foi utilizado um método HTTP inválido")
            break

        case '101':
            alert("Nem todos os inputs foram enviados")
            break

        case '102':
            alert("O campo nome excedeu 40 caracteres")
            break

        case '103':
            alert("O campo cpf é menor ou maior do que 11 caracteres")
            break

        case '104':
            alert("O campo email é inválido")
            break

        case '105':
            alert("O campo fone é inválido")
            break

        case '106':
            alert("O campo senha é inválido")
            break

        case '107':
            alert("O registro foi efetuado com sucesso")
            break

        case '108':
            alert("O email já está cadastrado")
            break

        case '109':
            alert("O cpf já está cadastrado")
            break

        case '110':
            alert("O registro falhou (Erro no DB)")
            break
    }
}
   

function register(){

    if(validInputs()){
        alert("Preencha todas as informações corretamente")
    }

    else{

        var formdata = new FormData();
        formdata.append("method", "register");
        formdata.append("nome", $("#nome").val());
        formdata.append("email", $("#email").val());
        formdata.append("fone", $("#fone").val());
        formdata.append("cpf", $("#cpf").val());
        formdata.append("senha", $("#senha").val());

        fetch('http://127.0.0.1:5000/api/v1/pfuser', {
            method: "POST",
            redirect: 'manual',
            body: formdata
        }).then(response => response.text()).then(result => verifyResult(JSON.parse(result)))




    }
    
}



