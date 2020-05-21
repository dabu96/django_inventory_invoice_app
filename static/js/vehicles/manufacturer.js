$(document).ready(function(){


    $('#id_manufacturer.form-control').on('change', function() {
        var url = $("#vehicleForm").attr("data-model-url");  // get the url of the `load_models` view
        var manufacturerId = $(this).val();  // get the selected country ID from the HTML input

      $.ajax({                       // initialize an AJAX request
        url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
        data: {
          'manufacturer': manufacturerId       // add the country id to the GET parameters
        },
        success: function (data) {   // `data` is the return of the `load_cities` view function
                 console.log('success');

          $("#id_vehicle_model").html(data);  // replace the contents of the city input with the data that came from the server
        }
      });

    });

});