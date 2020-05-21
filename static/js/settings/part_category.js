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
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#part-category-table tbody").html(data.part_category_list);
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



  $("#part-category-collapsible").click(function(){
    console.log('clicked')
    $(".fa-arrow-circle-down.rotate.company").toggleClass("up");
  })



  // Create Category
  $(".js-create-part-category").click(loadForm);
  $("#modal-input").on("submit", ".js-part-category-create-form", saveForm);

  // Update Category
  $("#part-category-table").on("click", ".js-update-part-category", loadForm);
  $("#modal-input").on("submit", ".js-part-category-update-form", saveForm);

  // Delete Category
  $("#part-category-table").on("click", ".js-delete-part-category", loadForm);
  $("#modal-input").on("submit", ".js-part-category-delete-form", saveForm);

});