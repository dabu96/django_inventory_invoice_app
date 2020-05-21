$(function () {

    /* Functions */

    var loadForm = function () {

        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                console.log("before send load vehicle form");
                $("#modal-input").modal("show");
            },
            success: function (data) {
                console.log("after send load vehicle form");
                $("#modal-input .modal-content").html(data.html_form);
            },
            error: function (data) {
                console.log(data)
            }
        });
    };


    var saveForm = function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    console.log('here save');
                    $("#modal-input").modal("hide");
                    $(".table").html(data.models_list);
                    $("#modal-input").modal("hide");

                } else {
                    $("#modal-input .modal-content").html(data.html_form);
                }

            },
            error: function (data) {
                console.log('error');
                console.log(data);
            }
        });
        return false;
    };



    /* Binding */

    // Create Model
    $(".js-create-vehicle-model").click(loadForm);
    $("#modal-input").on("submit", ".js-vehicle-model-create-form", saveForm);

    // Update Model
    $(".js-update-vehicle-model").click(loadForm);
    $("#modal-input").on("submit", ".js-vehicle-model-update-form", saveForm);

    // Delete Model
    $(".js-delete-vehicle-model").click(loadForm);
    $("#modal-input").on("submit", ".js-vehicle-model-delete-form", saveForm);

});




