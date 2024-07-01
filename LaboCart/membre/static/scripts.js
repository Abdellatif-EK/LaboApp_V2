// $(document).ready(function() {
//     $('#matrice-button').click(function(e) {
//         e.preventDefault();  // Prevent the default link behavior
        
//         $.ajax({
//             url: $(this).attr('href'),  // Use the href attribute of the button
//             type: 'GET',
//             dataType: 'json',
//             success: function(data) {
//                 // Manipulate the JSON data and update the matrix container
//                 var appareil = data['appareil'];

//                 var matrixContent = 'login: ' + appareil.login + ', Name: ' + appareil.Nom;
//                 var matrixRow = '<tr><td>' + matrixContent + '</td></tr>';
//                 $('#matrice-container tbody').append(matrixRow);
//                 $('#matrice-container').show(); 
//             },
//             error: function(xhr, status, error) {
//                 console.error(error);
//             }
//         });
//     });
// });



// $(document).ready(function() {
//     $.ajax({
//         url: 'matrice-detail/app_id/',  // Replace 'app_id' with the actual value
//         type: 'GET',
//         dataType: 'json',
//         success: function(data) {
//             // Manipulate the JSON data and display it in the <div>
//             var appareil = data[0].fields;  // Assuming the JSON has a 'fields' property

//             // Access the properties of 'appareil' and update the <div> with the desired content
//             $('#demo').html('Num: ' + appareil.Num + ', Name: ' + appareil.Name);
//         },
//         error: function(xhr, status, error) {
//             console.error(error);
//         }
//     });
// });


