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
    let table =  $('#tblSettings').DataTable({
        'columnDefs': [ {
            'targets': 5, /* column index */
            'orderable': false, /* true or false */
        }]
    }); 


    // $('#mySelect2').val(['Alabama', 'Alaska']);
    // $('#mySelect2').trigger('change');
    // $('.select2').select2({
    //     // ...
    //     templateSelection: function (data, container) {
    //         // Add custom attributes to the <option> tag for the selected option
    //         $(data.element).attr('data-custom-attribute', data.customValue);
    //         return data.text;
    //     }
    // }); 
    
    $("#newRole").click(function(e){
        e.preventDefault();
        let url = $(this).attr("href");

        $.ajax({
            url: url,
            type: 'GET',
            dataType: 'json',
            beforeSend: () =>{
                $("#modal-default").modal("show");
                $("#div_immidiate_supervisor").hide();//will hide the immidiate supervisor list before loading the content on the modal
            },
            success: (data) => {
                $("#modal-default .modal-content").html(data.html_form);
               // $("#modal-default #employeeList").select2();
                $("#modal-default .select2").select2(); 
                let json = JSON.stringify(data.list_of_employees, undefined, 2); 
                list_of_employees = JSON.parse(json); 
            },
            complete: (data) => {

            },
            error: (data) => {

            }
        });
        
        return false;
    }); 
    
    $("#modal-default").on("change",".create-roles-and-permission #id_role", function(e){
        e.preventDefault();
        let value = $(this).val();

        let bar = JSON.stringify(list_of_employees, undefined, 2);
        // console.log(bar);

        if(value.toUpperCase() == "Managing Director".toUpperCase()){
            $("#div_immidiate_supervisor").hide();
        }else if(value.toUpperCase() == "Human Resource".toUpperCase()){  
            immidiateSupervisorGenerator("Managing Director");
        }else if(value.toUpperCase() == "Business Unit Head".toUpperCase()){ 
            immidiateSupervisorGenerator("Human Resource");
            $("#div_immidiate_supervisor").show();
        }else if(value.toUpperCase() == "Employee".toUpperCase()){ 
            immidiateSupervisorGenerator("Business Unit Head");
            $("#div_immidiate_supervisor").show();
        }
 
        return false;
    });

    function immidiateSupervisorGenerator(role){
        //clear options

        $("#immidiateSupervisorList").empty();
        // filtering the option
        let option = list_of_employees.filter(function(item){ 
            return item.Role ==  role;
        })
        // console.log(option);
        //adding the option to select
        for(let o = 0; o < option.length; o++){
            let val = option[o].Employee;
            console.log(val);
            $("#immidiateSupervisorList").append(new Option(val,val));                
        }
        //show th select option            
        $("#div_immidiate_supervisor").show();
    } 

    function loadImmidiateSupervisorGenerator(role, json_response){
        //clear options

        $("#immidiateSupervisorList").empty();
        // filtering the option
        json_response = JSON.parse(json_response);
        let option = json_response.filter(function(item){ 
            return item.Role ==  role;
        })
        //adding the option to select
        for(let o = 0; o < option.length; o++){
            let val = option[o].Employee;
            $("#immidiateSupervisorList").append(new Option(val,val));                
        }
        //show th select option            
        $("#div_immidiate_supervisor").show();
    }

    function loadImmidiateSupervisor(role, json_response){
        if(role.toUpperCase() == "Managing Director".toUpperCase()){
            $("#div_immidiate_supervisor").hide();
        }else if(role.toUpperCase() == "Human Resource".toUpperCase()){  
            loadImmidiateSupervisorGenerator("Managing Director",json_response);
        }else if(role.toUpperCase() == "Business Unit Head".toUpperCase()){ 
            loadImmidiateSupervisorGenerator("Human Resource",json_response);
            $("#div_immidiate_supervisor").show();
        }else if(role.toUpperCase() == "Employee".toUpperCase()){ 
            loadImmidiateSupervisorGenerator("Business Unit Head",json_response);
            $("#div_immidiate_supervisor").show();
        }
    } 

    function editImmidiateSupervisorGenerator(role, value) {
        //clear options

        $("#immidiateSupervisorList").empty(); 
        // filtering the option
        let option = list_of_employees.filter(function(item){ 
            return item.Role ==  role;
        })
        // console.log(option);
        //adding the option to select
        for(let o = 0; o < option.length; o++){
            let val = option[o].Employee; 
            if (val != value){ 
                $("#immidiateSupervisorList").append(new Option(val,val));                
            }            
        }
        //show th select option            
        $("#div_immidiate_supervisor").show();
    }
   
    $("#modal-default").on("change",".edit-roles-and-permission #roleList", function(e){
        e.preventDefault();

        let value = $(this).val(); 
        let employeeName = $(".edit-roles-and-permission #employeeName").val();

        if(value.toUpperCase() == "Managing Director".toUpperCase()){
            $("#div_immidiate_supervisor").hide();
        }else if(value.toUpperCase() == "Human Resource".toUpperCase()){  
            editImmidiateSupervisorGenerator("Managing Director", employeeName);
        }else if(value.toUpperCase() == "Business Unit Head".toUpperCase()){ 
            editImmidiateSupervisorGenerator("Human Resource", employeeName);
            $("#div_immidiate_supervisor").show();
        }else if(value.toUpperCase() == "Employee".toUpperCase()){ 
            editImmidiateSupervisorGenerator("Business Unit Head", employeeName);
            $("#div_immidiate_supervisor").show();
        }
        
        return false;
    });
    
    $("#modal-default").on("submit",".create-roles-and-permission", function(e){
        e.preventDefault();
        let form = $(this);  
        let employee = $("#employeeList").val();
        let role = $("#id_role").val();
        let title = $("#titleList").val();
        let immidiate_supervisor = $("#immidiateSupervisorList").val();
        
        let data = {
            'employee': employee,
            'role': role,
            'title': title,
            'immidiate_supervisor':immidiate_supervisor
        }

        data = JSON.stringify(data);
 
        $.ajax({
            headers: { "X-CSRFToken": getCookie("csrftoken") },
            url: form.attr("data-url"),
            data: data,//form.serialize(),
            cache: false,
            type: form.attr("method"),
            dataType: 'json',
            beforeSend: () => {

            },
            success: (data) =>{

                if(data.form_is_valid){
                    $("#modal-default").modal('hide');
                    let json_reponse = JSON.stringify(data.record_data, undefined, 4); 
                    let employee = data.record_data['employee'];
                    let designation = data.record_data['designation'];
                    let role = data.record_data['role'];
                    let title = data.record_data['title'];
                    let edit_role_url = data.record_data['edit_role_url'];
                    let delete_role_url = data.record_data['delete_role_url']; 
                    let immidiate_supervisor = data.record_data['immidiate_supervisor'];
              
                    table.row.add([
                        `<i class="fa fa-fw fa-users"></i>
                         ${employee}`,
                        `${designation}`,
                        `${role}`,
                        `${title}`,
                        `${immidiate_supervisor}`,
                        `
                        <div class="text-center">                                        
                                    <div class="btn-group">
                                        <div class="btn-group">
                                            <button type="button" class="btn btn-default btn-flat">Action</button>
                                            <button type="button" class="btn btn-default btn-flat dropdown-toggle" data-toggle="dropdown" aria-expanded="false">
                                            <span class="caret"></span>
                                            <span class="sr-only">Toggle Dropdown</span>
                                            </button>
                                            <ul class="dropdown-menu" role="menu">
                                            <li><a class="editRolesPermission" href="${edit_role_url}"><i class="fa fa-fw fa-pencil"></i>Edit</a></li>
                                            <li><a class="deleteRolesPermission" href="${delete_role_url}"><i class="fa fa-fw fa-trash"></i>Delete</a></li> 
                                            </ul>
                                        </div>                                            
                                    </div>
                                    </div>
                        `
                    ]).draw(false);

                }else{
                    $("#modal-default .modal-content").html(data.html_form);
                }
                

            },
            complete: (data) => {

            },
            error: (data) => {

            }
        }); 
        return false;
    });     
    
    $("#modal-default").on("submit",".edit-roles-and-permission", function (e) {
        e.preventDefault();
        let form = $(this);
        let row = $("#modal-default").data('tr');
        let employee = $("#employeeName").val();
        let role = $("#roleList").val();
        let title = $("#titleList").val();
        let immidiate_supervisor = $("#immidiateSupervisorList").val(); 
        let data = {
            'employee': employee,
            'role': role,
            'title': title,
            'immidiate_supervisor':immidiate_supervisor
        }

        data = JSON.stringify(data);

        $.ajax({
            headers: { "X-CSRFToken": getCookie("csrftoken") },
            url: form.attr("data-url"),
            data: data,//form.serialize(),
            cache: false,
            type: form.attr("method"),
            dataType: 'json',
            beforeSend: () => {

            },
            success: (data) =>{

                if(data.form_is_valid){
                    $("#modal-default").modal('hide');
                    let json_reponse = JSON.stringify(data.rp_data, undefined, 4);  
                    let employee = data.rp_data['_employee_name']; 
                    let role = data.rp_data['_role'];
                    let title = data.rp_data['_title'];
                    let immidiate_supervisor = data.rp_data['_immidiate_supervisor']; 
 
                    let row_data = table.row(row).data();
                    row_data[0] = `<i class="fa fa-fw fa-users"></i> `+employee; 
                    row_data[2] = role; 
                    row_data[3] = title; 
                    row_data[4] = immidiate_supervisor; 
                    $("#tblSettings").dataTable().fnUpdate(row_data, row, undefined, false);

                    
                }else{
                    $("#modal-default .modal-content").html(data.html_form);
                }

            },
            complete: (data) => {

            },
            error: (data) => {

            }
        }); 

        
        return false;
    });

    $("#tblSettings").on("click",".editRolesPermission",function(e){
        e.preventDefault();
        let href = $(this).attr('href');
        let row = $(this).closest('tr');  
 

        $.ajax({
            headers: { "X-CSRFToken": getCookie("csrftoken") },
            url: href,
            type:'GET',
            dataType: 'json',
            beforeSend: () => {
                $("#modal-default").data('tr',row).modal("show");               
            },
            success: (data) => {
                $("#modal-default .modal-content").html(data.html_form); 
                $("#modal-default .modal-body .select2").select2();   
                let json_response_list_emp = JSON.stringify(data.list_emp, undefined, 4); 
                // Update
                list_of_employees = JSON.parse(json_response_list_emp); 
                
                data = JSON.stringify(data.rp_data,undefined, 4); 
                data = JSON.parse(data);
                let _employee_name = data['_employee_name'];
                let _role = data['_role'];
                let _title = data['_title'];
                let _immidiate_head = data['_immidiate_head']; 
                
                // Adding values
                $("#modal-default .modal-body #employeeName").val(_employee_name);  
                $("#modal-default .modal-body #roleList").val([_role]).trigger('change');  
                $("#modal-default .modal-body #titleList").val(_title).trigger('change');                  
                loadImmidiateSupervisor(_role,json_response_list_emp);
                $("#modal-default .modal-body #immidiateSupervisorList").val(_immidiate_head).trigger('change');  
                
            },
            complete: (data) => {

            },
            error: (data) => {

            }
        });
        return false;
    });

    $("#tblSettings").on("click", ".deleteRolesPermission", function(e){
        e.preventDefault();

        let url = $(this).attr("href");
        let row = $(this).closest('tr');  
        $.ajax({
            url: url,
            type: 'GET',
            dataType: 'json',
            beforeSend: () => { 
                $("#modal-default").data('tr',row).modal("show");
            },
            success: (data) => {
                $("#modal-default .modal-content").html(data.html_form);
            },
            complete: (data) => {

            },
            error: (data) => {

            }
        });
        return false;
    });

    $("#modal-default").on("submit",".delete-role-form", function(e){
        e.preventDefault();
        let form = $(this); 
        let row = $("#modal-default").data('tr');
        
        $.ajax({
            url: form.attr("data-url"),
            data: form.serialize(),
            cache: false,
            type: form.attr("method"),
            dataType: 'json',
            success: (data) => {
                if(data.form_is_valid){  
                    $("#modal-default").modal("hide");
                    table.row(row).remove().draw();    
                }else{
                    $("#modal-form .modal-content").html(data.html_form);
                }
            }
        });
        return false;
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