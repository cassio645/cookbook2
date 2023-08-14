// Função para deletar uma receita
function deleteFunction(id, title){
    var r = confirm(`Tem certeza que deseja apagar a receita\n ${title}?`);
    if (r == true){
        location.replace("/deletar/" + id);
    }
}

// Função para editar imagem
const opcaoNao = document.querySelector('input[name="opcao"][value="nao"]');
const opcaoSim = document.querySelector('input[name="opcao"][value="sim"]');
const imagemUpload = document.getElementById('imagemUpload');

function toggleImagemUpload() {
    if (opcaoSim.checked) {
        imagemUpload.style.display = 'block';
    } else {
        imagemUpload.style.display = 'none';
    }
}

opcaoSim.addEventListener('change', toggleImagemUpload);
opcaoNao.addEventListener('change', toggleImagemUpload);


// Função adicionar Dica
const dicaNao = document.querySelector('input[name="dica"][value="nao"]');
const dicaSim = document.querySelector('input[name="dica"][value="sim"]');
const inputDica = document.getElementById('inputDica');

function toggleinputDica() {
    if (dicaSim.checked) {
        inputDica.style.display = 'block';
    } else {
        inputDica.style.display = 'none';
    }
}

dicaSim.addEventListener('change', toggleinputDica);
dicaNao.addEventListener('change', toggleinputDica);


dicaSim.addEventListener('change', toggleinputDica);
dicaNao.addEventListener('change', toggleinputDica);