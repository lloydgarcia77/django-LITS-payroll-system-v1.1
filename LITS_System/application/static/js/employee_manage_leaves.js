$(document).ready(function () {  
    let table =  $('#tblLeaves').DataTable({
        "order": [[ 0, "desc" ]],
        'columnDefs': [ {
            'targets': 7, /* column index */
            'orderable': false, /* true or false */ 
        }]
    }); 
});