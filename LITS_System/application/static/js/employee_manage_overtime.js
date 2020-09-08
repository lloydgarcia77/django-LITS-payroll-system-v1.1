$(document).ready(function () {   
    let table =  $('#tblOvertime').DataTable({
        'columnDefs': [ {
            'targets': 3, /* column index */
            'orderable': false, /* true or false */
        }]
    }); 

    
});
