$(function () {

  /* Functions */

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
          $("#manufacturer-table tbody").html(data.manufacturer_list);
          $("#modal-input").modal("hide");

        } else {
          $("#modal-input .modal-content").html(data.html_form);
          alert("Form is not valid, try again...")

        }

      },
      error: function (data) {
        console.log(data);
      }


    });
    return false;
  };


 $("#manufacturer-collapsible").click(function(){
   console.log('clicked')
 $(".fa-arrow-circle-down").toggleClass("down");
})



  /* Binding */
  // Create Manufacturer
  $(".js-create-manufacturer").click(loadForm);
  $("#modal-input").on("submit", ".js-manufacturer-create-form", saveForm);

  // // Update Manufacturer
  $("#manufacturer-table").on("click", ".js-update-manufacturer", loadForm);
  $("#modal-input").on("submit", ".js-manufacturer-update-form", saveForm);

  // Delete manufacturer
  $("#manufacturer-table").on("click", ".js-delete-manufacturer", loadForm);
  $("#modal-input").on("submit", ".js-manufacturer-delete-form", saveForm);
});