$(function () {

  //   $("#add_manufacturer").on("click",function (e) {
  //       e.preventDefault();
  //       if ($("#modal").modal("show")) {
  //           $("#modal").modal("reset");
  //       }
  //       $.ajax({
  //         url: '/inventory/vehicles/manufacturer/create/$/',
  //         type: 'get',
  //         dataType: 'json',
  //         beforeSend: function () {
  //           $("#manufacturerModal").modal("show");
  //           console.log('here')
  //         },
  //         success: function (data) {
  //           $("#manufacturerModal .modal-content").html(data.html_form).modal("show");
  //           console.log('here to')
  //
  //         }
  //       });
  // });

  //   $("#add_manufacturer").on("click",function (e) {
  //     e.preventDefault();
  //     if ($("#modal").modal("show")) {
  //         $("#modal").modal("hide");
  //     }
  //   $.ajax({
  //       url: '/inventory/vehicles/manufacturer/create/$/',
  //       type: 'get',
  //       dataType: 'json',
  //       beforeSend: function () {
  //           $("#modal").modal("show");
  //           console.log('here')
  //       },
  //       success: function (data) {
  //           $("#modal .modal-content").html(data.html_form).modal("show");
  //           console.log('here to')
  //       }
  //   });
  // });

        $("#add_vehicle_model").on("click",function (e) {
      e.preventDefault();
    $.ajax({
      url: '/inventory/vehicles/test/$',
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal").modal("show");
        console.log('here')
      },
      success: function (data) {
        $("#modal .modal-content").html(data.html_form).modal("show");
        console.log('here to')

      }
    });
  });



    var frm = $('#form');
    var manuf_form = $('#form_manufacturer')

        frm.submit(function () {
        $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
            data :frm.serialize(),

            success: function (data) {
                console.log(data)
                $("#modal").modal("hide")
                $('.modal-backdrop').remove()
                window.location.reload(true);
            },
            error: function (data) {
                console.log(data)
            }
        });

        return false;
    });


    manuf_form.submit(function () {
            $.ajax({
                type: manuf_form.attr('method'),
                url: manuf_form.attr('action'),
                data :manuf_form.serialize(),
                success: function (data) {
                    console.log(data)
                    $("#manufacturerModal").modal("hide")
                    $('.modal-backdrop').remove()
                    // window.location.reload(true);

                },
                error: function (data) {
                    console.log(data)
                    console.log('error msg')
                }
            });
            return false;
        });


    // var frm = $('#form');
    // var test = $('#modal');
    // frm.submit(function () {
    //     $.ajax({
    //         type: frm.attr('method'),
    //         url: frm.attr('action'),
    //         data :frm.serialize(),
    //
    //         success: function (data) {
    //
    //             console.log(data)
    //             $("#modal").modal("hide")
    //
    //         },
    //         error: function (data) {
    //             console.log(data)
    //             console.log('error msg')
    //         }
    //     });
    //
    //     return false;
    // });


});

// $(function () {
//     $("#add_another").click(function () {
//     $.ajax({
//         url: "{% url 'vehicle-model-create' %}",
//         context: document.body
//     }).done(function(response) {
//         modal.html(response);
//     })
//     })
//
//
// $('#modal').on('show.bs.modal', function (event) {
//     var modal = $(this);
//     $.ajax({
//         url: "{% url 'vehicle-model-create' %}",
//         context: document.body
//     }).done(function(response) {
//         modal.html(response);
//     });
// });