$(document).ready(function(){

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
                console.log('before after send load vehicle form')
            },
            success: function (data) {
                console.log("after send load vehicle form");
                $("#modal-input .modal-content").html(data.html_form);
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
                    // $("#manufacturer-table tbody").html(data.manufacturer_list);
                    window.location.reload(true);
                    $("#modal-input").modal("hide");

                } else {
                    $("#modal-input .modal-content").html(data.html_form);
                }

            },
            error: function (data) {
                console.log(data);
            }
        });
        return false;
    };


    function getSelectedVals() {
        var ids = [];
        $(".selectCheck").each(function () {
            var check = false;
            if ($(this).prop('checked') == true) {
                ids.push($(this).val());
            }
        });
        return ids
    }



    function deleteVehicles() {
        var selected = getSelectedVals();
        var vehicle;
        var frm = $('#vehicle-delete');

        let confirmation = confirm("Are you sure you want to delete the selected item(s)?");
        if (confirmation) {
            for (vehicle of selected) {
                $.ajax({
                    type: frm.attr('method'),
                    url: vehicle + "/delete/",
                    data: frm.serialize(),
                    success: function (data) {
                        window.location.reload(true);
                    }
                });
            }
        }
    }

    /* Binding */
    $(".js-delete-vehicles").click(deleteVehicles);

    $(".js-create-vehicle").click(loadForm);
    $("#modal-input").on("submit", ".js-vehicle-create-form", saveForm);
    //
    // // Update book
    $(".js-update-vehicle").click(loadForm);
    $("#modal-input").on("submit", ".js-vehicle-update-form", saveForm);

    // Deelete manufacturer
    $(".js-delete-vehicle").click(loadForm);
    $("#modal-input").on("submit", ".js-vehicle-delete-form", saveForm);

});




