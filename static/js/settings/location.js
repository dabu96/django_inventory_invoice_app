$(function () {

  var loadForm = function () {

    console.log('hello');
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
    console.log('here save 1st');
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          console.log('here save');
          $("#location-table tbody").html(data.location_list);
          $("#modal-input").modal("hide");

        } else {
          $("#modal-input.modal-content").html(data.html_form);
          alert("Form is not valid, try again...")

        }

      },
      error: function (data) {
        console.log(data);
      }

    });
    return false;
  };


 $("#location-collapsible").click(function(){
   console.log('clicked')
 $(".fa-arrow-circle-down").toggleClass("down");
})



  /* Binding */
  // Create Location
  $(".js-create-location").click(loadForm);
  $("#modal-input").on("submit", ".js-location-create-form", saveForm);

  // Update Location
  $("#location-table").on("click", ".js-update-location", loadForm);
  $("#modal-input").on("submit", ".js-location-update-form", saveForm);

  // Delete Location
  $("#location-table").on("click", ".js-delete-location", loadForm);
  $("#modal-input").on("submit", ".js-location-delete-form", saveForm);

});