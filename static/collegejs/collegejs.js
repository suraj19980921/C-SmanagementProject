
function deleteCollege(id)
{
    document.getElementById('deleteCollegeId').value = id;
}


$('#addCollegeDetails').click(function () { 
   
    $('#exampleModalLabel').text('Add college Details');
    $('#collegeForm').attr('action', 'collegeDetails');
    $('#submitButton').text('Add');
    $('#college_name').val('');
    $('#college_address').val('');
    $('#college_phone').val('');
    $('#college_description').val('');

});


function fetchCollege(id)
{
    $('#exampleModalLabel').text('Edit college Details');
    $('#collegeForm').attr('action', 'update_details');
    $('#submitButton').text('Update');

    $.ajax({
        type: "get",
        url :'fetch',
        data:{id:id},
        success: function (response) {

            var data = JSON.parse(response.colleges);
            $('#collegeId').val(id);
            $('#college_name').val(data[0].fields.college_name);
            $('#college_address').val(data[0].fields.college_address);
            $('#college_phone').val(data[0].fields.college_phone);
            $('#college_description').val(data[0].fields.college_description);
        
        }
        
       
        
    });
   
}


$("#search").keyup(function (e) { 

    var value = $("#search").val();

    $.ajax({
        type: "get",
        url :'search',
        data:{value:value},
        success: function (response) {
           
            var data = JSON.parse(response.colleges);
           
            console.log(data[0].fields);

        }

        });
   
  

    
});
    



