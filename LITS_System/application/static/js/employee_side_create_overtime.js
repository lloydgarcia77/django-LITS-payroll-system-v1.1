$(document).ready(function () {     
     
    init_widgets();
     //Initialize Select2 Elements
     let days_of_week = [
        "SUN",
        "MON",
        "TUE",
        "WED",
        "THU",
        "FRI",
        "SAT" 
    ]
     $('.select2').select2();
    //  $('.frmDateRender').datepicker({ 
    //     autoclose: true,
    // }).datepicker("setDate",'now'); 
    $(".frmDateRender").each(function(index){
        $(this).datepicker({
            format: "mm/dd/yyyy",
            autoclose: true,
            //enableOnReadonly: false,
            clearBtn: true,
            //disableTouchKeyboard: true,
          }).on(`changeDate`, function(e) {
            // `e` here contains the extra attributes
            let date = new Date(e.date);
            
            $(`#id_overtime-${index}-day`).val(days_of_week[date.getDay()]);
        });
    });

    function init_widgets(){
        $("#formOvertimeDetailsOuter .frmDateRender, #formOvertimeDetailsOuter .frmProduct, #formOvertimeDetailsOuter .frmDescription").prop("required",true);
        $(".frmDateRender").keydown(function(e){
            e.preventDefault();
        });
    }
    
    function calculateTime(index){
        if ($(`#id_overtime-${index}-timeIn`).val() == "0:00" || $(`#id_overtime-${index}-timeOut`).val() == "0:00"){
            $(`#id_overtime-${index}-duration`).val("");  
        }else{ 
            let time_in = $(`#id_overtime-${index}-timeIn`).val(); 
            let time_out = $(`#id_overtime-${index}-timeOut`).val();    
              
    
            let time_in_hour = parseInt(time_in.split(":")[0], 10);
            let time_in_min = parseInt(time_in.split(":")[1], 10);
    
            let time_out_hour = time_out.split(":")[0];
            let time_out_min = time_out.split(":")[1];

            let duration = 0;

            const ti = new Date();
            ti.setHours(time_in_hour,time_in_min,0,0)

            const to = new Date();
            to.setHours(time_out_hour,time_out_min,0,0);

            if(to.getTime() > ti.getTime()){
                let milliseconds = to.getTime() - ti.getTime();
                let seconds = milliseconds / 1000.0;
                let minutes = seconds / 60.0;
                let hours = minutes / 60.0;
                // console.log(milliseconds);
                // console.log(seconds);
                // console.log(minutes);
                // console.log(hours);
                $(`#id_overtime-${index}-duration`).val(hours); 
            }else{
                $(`#id_overtime-${index}-duration`).val(0); 
            }
        }
    }

    $('.frmTimeIn').each(function(index){
        $(this).timepicker({
            maxHours: 24,
            showInputs: false,
            showMeridian: false,
            defaultTime: "0:00",
        });

        $(this).change(function(){ 
             if($(this).val() == "0:00"){
                $(this).val("");
            }else{
                calculateTime(index);
            }
        });
    });

    $('.frmTimeOut').each(function(index){
        $(this).timepicker({
            maxHours: 24,
            showInputs: false,
            showMeridian: false,
            defaultTime: "0:00",
        });

        $(this).change(function(){
             if($(this).val() == "0:00"){
                $(this).val("");
            }else{
                calculateTime(index);
            }
        });
    });

    $("#add_field").click(function(e){
        e.preventDefault(); 
        //get the total forms
        let form_idx = $("#formOvertimeDetailsOuter #id_overtime-TOTAL_FORMS").val();
        //when edit mode or with query is enable initial form is set upon edit and deleting
        let form_idx_init = $("#formOvertimeDetailsOuter #id_overtime-INITIAL_FORMS").val();
        $("#formOvertimeDetailsOuter").append($("#empty_formOvertimeDetails").html().replace(/__prefix__/g, form_idx));
        $("#formOvertimeDetailsOuter #id_overtime-TOTAL_FORMS").val(parseInt(form_idx) + 1);
        // date rendered
        $(`#id_overtime-${form_idx}-date_rendered`).datepicker({
            format: "mm/dd/yyyy",
            autoclose: true,
            //enableOnReadonly: false,
            clearBtn: true,
            //disableTouchKeyboard: true,
          }).on(`changeDate`, function(e) {
            // `e` here contains the extra attributes
            let date = new Date(e.date);
            
            $(`#id_overtime-${form_idx}-day`).val(days_of_week[date.getDay()]);
        });
        // time in 
        $(`#id_overtime-${form_idx}-timeIn`).timepicker({
            maxHours: 24,
            showInputs: false,
            showMeridian: false,
            defaultTime: "0:00",
        });

        $(`#id_overtime-${form_idx}-timeIn`).change(function(){ 
                if($(this).val() == "0:00"){
                $(this).val("");
            }else{
                calculateTime(form_idx);
            }
        }); 
        // time out 
        $(`#id_overtime-${form_idx}-timeOut`).timepicker({
            maxHours: 24,
            showInputs: false,
            showMeridian: false,
            defaultTime: "0:00",
        });

        $(`#id_overtime-${form_idx}-timeOut`).change(function(){
                if($(this).val() == "0:00"){
                $(this).val("");
            }else{
                calculateTime(form_idx);
            }
        }); 

        init_widgets();
        if(form_idx > 0){
            $("#del_field").show();
        }else{
            $("#del_field").hide();
        }
        return false;
    });

    $("#del_field").click(function(e){
        e.preventDefault();
        let form_idx = $("#formOvertimeDetailsOuter #id_overtime-TOTAL_FORMS").val();
        $('#formOvertimeDetailsOuter .formOvertimeDetailsInner').last().remove();
        $("#formOvertimeDetailsOuter #id_overtime-TOTAL_FORMS").val(parseInt(form_idx) - 1); 
        let form_idx_after = $("#formOvertimeDetailsOuter #id_overtime-TOTAL_FORMS").val();
        
        if(form_idx_after <= 1){
            $("#del_field").hide();
        }
        return false;
    });
});