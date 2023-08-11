function deleteFunction(id, title){
    var r = confirm(`Tem certeza que deseja apagar a receita\n ${title}?`);
    if (r == true){
        location.replace("/deletar/" + id);
    }
}