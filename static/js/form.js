$(document).ready(function () {
    // counter for the number of ingredients being shown
    var ingredientID = 1;

    // function to add an ingredient once the add ingredient button is selected
    $('#add_ing').click(function (e) {
        e.preventDefault();
        // Add another option for an ingredient and it's amount
        $('#ingredients-list').append(`
        <div class="input-field col s6">
            <input type="text" id="ingredient_name` + ingredientID + `" name="ingredient_name` + ingredientID + `" class="materialize-textarea">
            <label for="ingredient_name` + ingredientID + `">Ingredient</label>
        </div>
        <div class="input-field col s6">
            <input type="text" id="ingredient_amount` + ingredientID + `" name="ingredient_amount` + ingredientID + `" class="materialize-textarea">
            <label for="ingredient_amount` + ingredientID + `">Amount</label>
        </div>`);

        // increment Ingedient counter after the add ingredient button is pressed
        ingredientID++;

        // show the remove ingredient button if there is greater than 1 ingredient shown
        if (ingredientID > 1) {
            $("#remove_ing").show();
        }

        // remove the add ingredient button if there is the maximum of 6 ingredients shown
        if (ingredientID >= 6) {
            $("#add_ing").hide();
        }
    });

    // function to remove an ingredient once the remove ingredient button is selected
    $('#remove_ing').click(function (e) {
        e.preventDefault();
        // removes the last two Div's from the ingredient-list div, once the remove ingredient button is pressed
        $("#ingredients-list  > div").slice(-2).remove();

        // reduces the count on the number of ingredients
        ingredientID--;


        // hide the remove ingredient button if there is less than 1 ingredient shown
        if (ingredientID <= 1) {
            $("#remove_ing").hide();
        }

        // show the add ingredient button if there is less than 6 ingredients shown
        if (ingredientID < 6) {
            $("#add_ing").show();
        }
    });



    // counter for the number of steps being shown
    var methodID = 1;

    // function to add a step once the add step button is selected
    $('#add_step').click(function (e) {
        e.preventDefault();
        // Add another option for a step
        $('#method-list').append(`
        <div class="input-field col s12">
            <input type="text" id="method` + methodID + `" name="method` + methodID + `" class="materialize-textarea validate">
            <label for="method` + methodID + `">Enter step details</label>
        </div>`);

        // increment the step counter after the add step button is pressed
        methodID++;

        // show the remove step button if there is greater than 1 step shown
        if (methodID > 1) {
            $("#remove_step").show();
        }


        // remove the add step button if there is the maximum of 6 steps shown
        if (methodID >= 6) {
            $("#add_step").hide();
        }
    });

    // function to remove a step once the remove step button is selected
    $('#remove_step').click(function (e) {
        e.preventDefault();

        // removes the last div from the method-list div, once the remove step button is pressed
        $("#method-list  > div").slice(-1).remove();

        // reduces the count on the number of steps
        methodID--;

        // hide the remove step button if there is less than 1 step shown
        if (methodID <= 1) {
            $("#remove_step").hide();
        }

        // show the add step button if there is less than 6 step shown
        if (methodID < 6) {
            $("#add_step").show();
        }
    });


});