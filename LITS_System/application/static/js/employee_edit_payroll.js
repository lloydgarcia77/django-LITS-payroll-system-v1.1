$(document).ready(function() { 
    let totalDeduction = $("#totalDeduction").val() == "" || isNaN($("#totalDeduction").val()) ? 0 : $("#totalDeduction").val(); 
 
    function calculate() { 
        let basicPay = $("#basicPay").val() == "" || isNaN($("#basicPay").val()) ? 0 : $("#basicPay").val();
        let allowance = $("#allowance").val() == "" || isNaN($("#allowance").val()) ? 0 : $("#allowance").val();
        let overtimePay = $("#overtimePay").val() == "" || isNaN($("#overtimePay").val()) ? 0 : $("#overtimePay").val();
        let holidayPay = $("#holidayPay").val() == "" || isNaN($("#holidayPay").val()) ? 0 : $("#holidayPay").val(); 
        let salaryCashAdvance = $("#salaryCashAdvance").val() == "" || isNaN($("#salaryCashAdvance").val()) ? 0 : $("#salaryCashAdvance").val();
        
    
        let withholdingTax = $("#withholdingTax").val() == "" || isNaN($("#withholdingTax").val()) ? 0 : $("#withholdingTax").val();
        let pagibigLoan = $("#pagibigLoan").val() == "" || isNaN($("#pagibigLoan").val()) ? 0 : $("#pagibigLoan").val();
        let deductionSalaryCashAdvance = $("#deductionSalaryCashAdvance").val() == "" || isNaN($("#deductionSalaryCashAdvance").val()) ? 0 : $("#deductionSalaryCashAdvance").val();
   
        let sssPremius =  $("#sssPremius").val() == "" || isNaN($("#sssPremius").val()) ? 0 : $("#sssPremius").val();
        let philhealContribution = $("#philhealContribution").val() == "" || isNaN($("#philhealContribution").val()) ? 0 : $("#philhealContribution").val();
        let pagibigContribution = $("#pagibigContribution").val() == "" || isNaN($("#pagibigContribution").val()) ? 0 : $("#pagibigContribution").val();
 

        let gp = parseFloat(basicPay) + parseFloat(allowance) + parseFloat(overtimePay) + parseFloat(salaryCashAdvance) + parseFloat(holidayPay);
        td = parseFloat(philhealContribution) + parseFloat(pagibigContribution) + parseFloat(sssPremius) + parseFloat(withholdingTax) + parseFloat(pagibigLoan) + parseFloat(deductionSalaryCashAdvance) + parseFloat(totalDeduction);
        let np = gp - td;  
        $("#grossPay").val(gp.toFixed(2));
        $("#totalDeduction").val(td.toFixed(2));
        $("#netPay").val(np.toFixed(2)); 
    }
 
 
    $("#basicPay, #allowance, #salaryCashAdvance, #overtimePay, #sssPremius, #lateAbsences, #philhealContribution, #pagibigContribution, #withholdingTax, #pagibigLoan, #deductionSalaryCashAdvance").change(function() {
        calculate();
    });

    $("#btnDeletePayroll").on("click", function(e){
        e.preventDefault();
        var button = $(this);
        $.ajax({
            url: button.attr("data-url"),
            type: 'GET',
            dataType: 'json',
            beforeSend: function () {
                
                $("#modal-default").modal("show");
            },
            success: function (data) { 
                $("#modal-default .modal-content").html(data.html_form);
            }
        });
        return false;
    });

    $("#modal-default").on("submit", ".frm-delete-payroll", function(e){
        e.preventDefault();
        let form = $(this);

        $.ajax({
            url: form.attr("data-url"),
            data: form.serialize(),
            cache: false,
            type: form.attr("method"),
            dataType: 'json',
            success: (data) => {
                // Note: The difference between href and replace, is that replace() removes the URL of 
                // the current document from the document history, meaning that it is not possible to 
                // use the "back" button to navigate back to the original document.
                if (data.form_is_valid) {
                    $("#modal-default").modal('hide'); 
                    window.location.replace(data.link);
                } else {
                    $("#modal-default .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    });


});