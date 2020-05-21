$(document).ready(function () {
    var card_number_field = document.getElementById("div_id_card_number");
    card_number_field.style.display = "none";

    $('#add_more').click(function () {
        var form_idx = $('#id_parts_bought-TOTAL_FORMS').val();
        console.log(form_idx);
        // var = add_select(form_idx);

        $('#form_set').append($('#empty_form').html().replace(/__prefix__/g, form_idx));

        $('#id_parts_bought-TOTAL_FORMS').val(parseInt(form_idx) + 1);
    });


    function add_select(id_num) {
        var clone = $('#manufacturer_select_0').clone();
        var vehicle_select = document.createElement("select");
        var manufacturer_select = document.createElement("select");

        vehicle_select.id = "vehicles_select_" + id_num;
        manufacturer_select.id = "manufacturers_select_" + id_num;
        var manufacturer_options = $('#manufacturers_select_0').html();
        var form = $('#form_set');
        form.append(manufacturer_select);


    }


    $('#id_payment_type').on('change', function () {
        var option = $(this).val();
        if (option === 'CC' || option === 'DC') {
            card_number_field.style.display = "block";
        } else card_number_field.style.display = "none";

    });


    function getNum(current_id) {
        return current_id.match(/\d+$/);
    }

    $('.manufacturers_select').on('change', function () {
        var url = $("#load-models").attr("data-model-url");
        var current_id = $(this).attr("id");
        var vehicles_select_id = 'vehicles_select_' + getNum(current_id);
        var manufacturer = $(this).val();
        $.ajax({
            url: url,
            data: {
                'manufacturer': manufacturer
            },
            success: function (data) {
                var vehicle_selected = $('#' + vehicles_select_id);
                vehicle_selected.empty();
                vehicle_selected.append($('<option>').text('...........').attr('value', ''));

                data.vehicle_models = $.parseJSON(data.vehicle_models);
                $(data.vehicle_models).each(function (index, record) {
                    var vehicle = record.fields.sku;
                    var replaced_string = vehicle.substring(0, 4);
                    vehicle = vehicle.replace(replaced_string, '');
                    vehicle_selected.append($('<option>').text(vehicle).attr('value', record.pk));
                });
            }
        });
    });


    $('.vehicles_select').on('change', function () {
        var url = $("#load-parts").attr("data-model-url");
        var current_id = $(this).attr("id");
        var parts_select_id = 'id_parts_bought-' + getNum(current_id) + '-part';
        var model = $(this).val();
        $.ajax({
            url: url,
            data: {
                'model': model
            },
            success: function (data) {
                $('#' + parts_select_id).empty();
                data.parts = $.parseJSON(data.parts);
                $(data.parts).each(function (index, record) {
                    var part;
                    if (!record.fields.side) {
                        part = record.fields.name;
                    } else part = record.fields.name + ' ' + record.fields.side;
                    $('#' + parts_select_id).append($('<option>').text(part).attr('value', record.pk));
                });
            }
        });
    });
});