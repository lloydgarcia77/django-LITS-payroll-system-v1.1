$(document).ready(function () {   
    //Initialize Select2 Elements
    $('#classificationOfLeave').select2();
    //Date range picker http://www.daterangepicker.com/
    //https://stackoverflow.com/questions/36600687/moment-js-two-dates-difference-in-number-of-days/36600770
    $('#reservation, #inclusiveDates').daterangepicker();

    $('#reservation, #inclusiveDates').on('apply.daterangepicker', function(ev, picker) {
        let _startDate = picker.startDate.format('YYYY-MM-DD');
        let _endDate = picker.endDate.format('YYYY-MM-DD');
        let mStartDate = moment(_startDate, 'YYYY-MM-DD');
        let mEndDate = moment(_endDate, 'YYYY-MM-DD');
        let _noDays = mEndDate.diff(mStartDate, 'days');
        $("#noOfDays").val(_noDays); 
        // console.log(picker.startDate.format('YYYY-MM-DD'));  
        // console.log(picker.endDate.format('YYYY-MM-DD'));
        let val = $("#inputVLC").val();
        $("#id_leave_credits").val(val);
        $('#id_less_this_application').val(_noDays);
        let balance = parseInt(val) - parseInt(_noDays);
        $("#id_balance_as_of_this_date").val(balance);

    }); 
    $("#classificationOfLeave").change(function(e){
        e.preventDefault();
      
        let value = $(this).val();
        let closestDivVLC = $("#inputVLC").closest('div');
        let closestDivSLC = $("#inputSLC").closest('div'); 
        if(value == "Vacation Leave"){ 
            closestDivVLC.removeClass("has-warning");
            closestDivVLC.addClass("has-error"); 
        }else{  
            closestDivVLC.removeClass("has-error");
            closestDivVLC.addClass("has-warning"); 
        }
        if(value == "Sick Leave"){ 
            closestDivSLC.removeClass("has-success");
            closestDivSLC.addClass("has-error"); 
        }else{  
            closestDivSLC.removeClass("has-error");
            closestDivSLC.addClass("has-success"); 
        }
        
        
       // alert(value);
        return false;
    });
});