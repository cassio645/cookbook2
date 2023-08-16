document.addEventListener("DOMContentLoaded", function() {

    // Pegando a div do input e o botão de adicionar ingredientes
    const ingredientsContainer = document.getElementById("div_id_ingredientes");
    const addIngredientButton = document.getElementById("add-ingredient");

    // Adicionando um evento, sempre que o botão for pressionado ele cria outro input.text com as mesmas caracteristicas
    addIngredientButton.addEventListener("click", function() {
        const newInput = document.createElement("input");
        newInput.type = "text";
        newInput.name = "ingredientes";
        newInput.classList.add("form-control");
        newInput.classList.add("ingredient-input");
        newInput.placeholder = "3 xícaras de farinha"
        ingredientsContainer.appendChild(newInput);
    });

    // Pega todos os campos com class "ingredient-input" e cria um array separado por vírgula
    const form = document.querySelector("form");
    form.addEventListener("submit", function(event) {
        const ingredientInputs = document.querySelectorAll(".ingredient-input");
        const combinedIngredients = Array.from(ingredientInputs).map(input => input.value).join(", ");

        // Cria um novo input com os ingredientes combinados em formato de array
        const hiddenInput = document.createElement("input");
        hiddenInput.type = "hidden";
        hiddenInput.name = "combined_ingredients";
        hiddenInput.value = combinedIngredients;
        form.appendChild(hiddenInput);
    });
});