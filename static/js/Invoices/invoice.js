
$( function() {
    var loadForm = function () {
        var link = $(this);
        console.log(link);
        $.ajax({
            url: link.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-input").modal("show");
            },
            success: function (data) {
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

    $(".js-delete-invoice").click(loadForm);
    $("#modal-input").on("submit", ".js-invoice-delete-form", saveForm);

    $(".js-refund-invoice").click(loadForm);
    $("#modal-input").on("submit", ".js-invoice-refund-form", saveForm);

} );



