$( function() {
    
    const date = new Date(); 
    // Holds the value of JSON
    let list_of_employees;
    year = date.getFullYear();
    month = date.getMonth() + 1;
    c_date = date.getDate();
 
    
    $("#current_date_display").text(`Current Date: ${month}/${c_date}/${year}`); 
 
    // for testing
    //https://select2.org/advanced/default-adapters/array
    //Initialize Select2 Elements 
    let table =  $('#tblEmployeeForms').DataTable({
        'columnDefs': [ {
            'targets': 5, /* column index */
            'orderable': false, /* true or false */
        }]
    }); 

 
 
    function getCookie(cname) {
        var name = cname + "=";
        var decodedCookie = decodeURIComponent(document.cookie);
        var ca = decodedCookie.split(';');
        for (var i = 0; i < ca.length; i++) {
            var c = ca[i];
            while (c.charAt(0) == ' ') {
                c = c.substring(1);
            }
            if (c.indexOf(name) == 0) {
                return c.substring(name.length, c.length);
            }
        }
        return "";
    }
     


}); 