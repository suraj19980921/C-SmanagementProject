
function deleteStaff(id)
{
    document.getElementById('deletestaffId').value = id;
}


$('#addstaffDetails').click(function () { 
   
    $('#exampleModalLabel').text('Add staff Details');
    $('#staffForm').attr('action', 'staffDetails');
    $('#submitButton').text('Add').show();
    $("#resetButton").show();
    $('.form-control').attr('readonly',false);
    $('#staff_name').val('');
    $('#staff_address').val('');
    $('#staff_phone').val('');
    $('#staff_description').val('');

});


function fetchstaff(id)
{
    $('#exampleModalLabel').text('Edit staff Details');
    $('#staffForm').attr('action', 'update_details');
    $('#submitButton').text('Update').show();
    $("#resetButton").show();
    $('.form-control').attr('readonly',false);

    

    $.ajax({
        type: "get",
        url :'fetchStaff',
        data:{id:id},
        success: function (response) {

            var data = JSON.parse(response.staffs);
            $('#staffId').val(id);
            $('#staff_name').val(data[0].fields.staff_name);
            $('#staff_address').val(data[0].fields.staff_address);
            $('#staff_phone').val(data[0].fields.staff_phone);
            $('#staff_description').val(data[0].fields.staff_description);
        
        }
        
       
        
    });
   
}

$('#viewStaff').click(function (e) { 
    
    $('#exampleModalLabel').text(' Staff Details');
    $('.form-control').attr('readonly',true);
    $('#submitButton').hide();
    $("#resetButton").hide();
    
});

$("#search").keyup(function (e) { 

    var value = $("#search").val();

    $.ajax({
        type: "get",
        url :'search',
        data:{value:value},
        success: function (response) {
           
            var data = JSON.parse(response.staffs);
           
            console.log(data[0].fields);

        }

        });
   
  

    
});
    



