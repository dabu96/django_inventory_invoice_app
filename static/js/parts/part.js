$(document).ready(function () {
    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-input").modal("show");
            },
            success: function (data) {
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
                        window.location.reload(true);
                    } else {
                        $("#modal-input .modal-content").html(data.html_form);
                        alert("Form is not valid, try again...")
                    }
                },
                error: function (data) {
                    console.log(data);
                },
            }
        );
        return false;
    };

    function getSelectedVals() {
        var ids = [];
        $(".selectCheck").each(function () {
            var check = false;
            if ($(this).prop('checked') === true) {
                ids.push($(this).val());
            }
        });
        return ids
    }


    function loadGeneratedInvoice() {
        selected = getSelectedVals();
        var myurl = "?id=" + selected;
        $.ajax({
            type: "GET",
            url: myurl,
            data: selected,
            cache: false,

            success: function (data) {
                console.log(data);
                window.location.href = "/invoice/create" + myurl

            }
        });
    }


    function deleteParts() {
        var selected = getSelectedVals();
        var part;
        var frm = $('#part-delete');

        let confirmation = confirm("Are you sure you want to delete the selected item(s)?");
        if (confirmation) {
            for (part of selected) {
                $.ajax({
                    type: frm.attr('method'),
                    url: part + "/delete/",
                    data: frm.serialize(),
                    success: function (data) {
                        window.location.reload(true);
                    }
                });
            }
        }
    }

    $(".js-delete-parts").click(deleteParts);

    $(".js-generate-invoice").click(loadGeneratedInvoice);

    /* Binding */
    // Create Part
    $(".js-create-part").click(loadForm);
    $("#modal-input").on("submit", ".js-part-create-form", saveForm);
    //
    // Update Part
    $(".js-update-part").click(loadForm);
    $("#modal-input").on("submit", ".js-part-update-form", saveForm);


});