$(document).ready(function () {

    var ingredientID = 1;

    $('#add_ing').click(function (e) {
        e.preventDefault();
        $('#ingredients-list').append(`<div class="input-field col s6">
        <input type="text" id="ingredient_name` + ingredientID + `" name="ingredient_name` + ingredientID + `" class="materialize-textarea">
        <label for="ingredient_name` + ingredientID + `">Ingredient</label>
    </div>
    <div class="input-field col s6">
        <input type="text" id="ingredient_amount` + ingredientID + `" name="ingredient_amount` + ingredientID + `" class="materialize-textarea">
        <label for="ingredient_amount` + ingredientID + `">Amount</label>
    </div>`);

        ingredientID++;

        if (ingredientID > 1) {
            $("#remove_ing").show();
        }
    });

    $('#remove_ing').click(function (e) {
        e.preventDefault();
        $("#ingredients-list  > div").slice(-2).remove();
        ingredientID--;
        if (ingredientID <= 1) {
            $("#remove_ing").hide();
        }

    });




    var methodID = 1;

    $('#add_step').click(function (e) {
        e.preventDefault();
        $('#method-list').append(`
        <div class="input-field col s12">
            <input type="text" id="method` + methodID + `" name="method` + methodID + `" class="materialize-textarea validate">
            <label for="method` + methodID + `">Enter step details</label>
        </div>`);

        methodID++;

        if (methodID > 1) {
            $("#remove_step").show();
        }
    });

    $('#remove_step').click(function (e) {
        e.preventDefault();
        $("#method-list  > div").slice(-1).remove();
        methodID--;

        if (methodID <= 1) {
            $("#remove_step").hide();
        }

    });


});