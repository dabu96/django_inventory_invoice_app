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
          $("#company-table tbody").html(data.company_list);
          $("#modal-input").modal("hide");

        } else {
          $("#modal-input.modal-content").html(data.html_form);

        }

      },
      error: function (data) {
        console.log(data);
      }


    });
    return false;
  };


 $("#company-collapsible").click(function(){
   console.log('clicked')
 $(".rotate").toggleClass("down");
})



  /* Binding */
  // Create company
  $(".js-create-company").click(loadForm);
  $("#modal-input").on("submit", ".js-company-create-form", saveForm);

  // Update company
  $("#company-table").on("click", ".js-update-company", loadForm);
  $("#modal-input").on("submit", ".js-company-update-form", saveForm);

  // Delete company
  $("#company-table").on("click", ".js-delete-company", loadForm);
  $("#modal-input").on("submit", ".js-company-delete-form", saveForm);
});