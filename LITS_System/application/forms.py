from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from application.models import PersonalInfo, MobileNumberInfo, SkillsInfo, CompanyInfo,TelephoneNumberInfo,CutOffPeriodInfo, AttendanceInfo, EmployeePayroll, EmployeeSalary, EmployeeLeaves, EmployeeItenerary, EmployeeIteneraryDetails,Concerns,Overtime,OvertimeDetails
import os
from decimal import Decimal

def file_validator(value):

    file_size = value.size
    valid_file_extension = ['.xlsx','.xls']

    file_extension = os.path.splitext(value.name)[1]

    print("File Name: ", value.name)
    print("File Extension: ", file_extension)

    file_size_kb = file_size * 0.001
    file_size_mb = file_size_kb * 0.0001

    print("File Size: ", file_size, " Bytes")
    print("File Size: ", file_size_kb, " KB")
    print("File Size: ", file_size_mb, " MB")

    if not file_extension in valid_file_extension:
        print("Invalid file! Valid files only: ('.xlsx', '.xls')")
        raise ValidationError("Invalid file! Valid files only: ('.xlsx', '.xls')")

    else:
        if file_size_mb > 5: # 5MB
            print("File too large! The maximum file size can be upload is 5 MB")
            raise ValidationError("The maximum file size can be upload is 5 MB")
        else:
            print('FILE is VALID')
            return value


class UserAccountCredentialsForm(UserCreationForm):
    class Meta():
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(UserAccountCredentialsForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Username',
        }

        self.fields['email'].widget.attrs = {
            'type': 'email',
            'class': 'form-control',
            'placeholder': 'Email',
            'required': 'required',
        }

        self.fields['password1'].widget.attrs = {
            'type': 'password',
            'class': 'form-control',
            'placeholder': 'Password',
        }

        self.fields['password2'].widget.attrs = {
            'type': 'password',
            'class': 'form-control',
            'placeholder': 'Retype password',
        }

class PersonalForm(forms.ModelForm):

    dob = forms.DateField(
        widget=forms.DateInput(
            format='%m/%d/%Y',
            attrs={
                'id': 'dob',
                'type': 'text',
                'class': 'form-control pull-right',
            }
        ),
        input_formats=('%m/%d/%Y', )
    )

    date_started = forms.DateField(
        widget=forms.DateInput(
            format='%m/%d/%Y',
            attrs={
                'id': 'date_started',
                'type': 'text',
                'class': 'form-control pull-right',
            }
        ),
        input_formats=('%m/%d/%Y', )
    )

    class Meta():
        model = PersonalInfo
        exclude = ("fk_user", "key_id", "date_added")

    def __init__(self, *args, **kwargs):
        super(PersonalForm, self).__init__(*args, **kwargs)

        self.fields['suffix'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Suffix if any',
        }
        self.fields['first_name'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'First name', 
            'maxlength': '10',
        }
        self.fields['middle_name'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Middle Name',
            'maxlength': '10',
        }
        self.fields['last_name'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Last name',
            'maxlength': '10',
        }
        self.fields['age'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Age',
        }
        # self.fields['gender'].widget.attrs = {
        #     'class': 'form-control select2',
        #     'style': 'width: 100%;',
        # }

        self.fields['gender'].widget.attrs = {
            'type': 'text',
            'class': 'form-control', 
        }
        self.fields['address'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Address',
        }

        self.fields['education'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Education',
        }

        self.fields['experience'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Experience',
        }

        self.fields['notes'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Notes',
        }

        self.fields['emer_cont_pers'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Emergency Contact Person',
        }

        self.fields['emer_cont_pers_cont_no'].widget.attrs = {
            'type': 'number',
            'class': 'form-control',
            'placeholder': 'Emergency Contact Person Number',
        }

class MobileNumberForm(forms.ModelForm):
    class Meta():
        model = MobileNumberInfo
        exclude = ("fk_mobile_user",)

    def __init__(self, *args, **kwargs):
        super(MobileNumberForm, self).__init__(*args, **kwargs)

        self.fields['mobile_number'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Mobile Number',
            'required': 'required',
        }

class SkillsForm(forms.ModelForm):

    SKILL_LIST = (
       ('Actuarial/Statistics','Actuarial/Statistics'),
        ('Advertising','Advertising'),
        ('Agriculture','Agriculture'),
        ('Architect/Interior Design','Architect/Interior Design'),
        ('Arts/Creative Design','Arts/Creative Design'),
        ('Audit Taxation','Audit Taxation'),
        ('Aviation','Aviation'),
        ('Banking/Financial','Banking/Financial'),
        ('Biotechnology','Biotechnology'),
        ('Chemical Engineering','Chemical Engineering'),
        ('Chemistry','Chemistry'),
        ('Civil Engineering/Construction','Civil Engineering/Construction'),
        ('Civil/Government Services','Civil/Government Services'),
        ('Clerical/Administrative','Clerical/Administrative'),
        ('Corporate Finance/Investment','Corporate Finance/Investment'),
        ('Customer Service','Customer Service'),
        ('Digital Marketing','Digital Marketing'),
        ('Doctor/Diagnosis','Doctor/Diagnosis'),
        ('E-commerce','E-commerce'),
        ('Education','Education'),
        ('Electrical Engineering','Electrical Engineering'),
        ('Electronics Engineering','Electronics Engineering'),
        ('Entertainment','Entertainment'),
        ('Environmental Engineering','Environmental Engineering'),
        ('Executive Assistant','Executive Assistant'),
        ('Food Tech/Nutritionist','Food Tech/Nutritionist'),
        ('Food/Beverage/Restaurant','Food/Beverage/Restaurant'),
        ('General Manager','General Manager'),
        ('General Work','General Work'),
        ('General/Cost Accounting','General/Cost Accounting'),
        ('Geology/Geophysics','Geology/Geophysics'),
        ('Hotel/Tourism','Hotel/Tourism'),
        ('Human Resources','Human Resources'),
        ('Industrial Engineering','Industrial Engineering'),
        ('IT - Hardware','IT - Hardware'),
        ('IT - Network/Sys/DB Admin','IT - Network/Sys/DB Admin'),
        ('IT - Software Engineering','IT - Software Engineering'),
        ('Journalist/Editors','Journalist/Editors'),
        ('Law/Legal Services','Law/Legal Services'),
        ('Logistics/Supply Chain','Logistics/Supply Chain'),
        ('Maintenance','Maintenance'),
        ('Management Trainee','Management Trainee'),
        ('Manufacturing','Manufacturing'),
        ('Marketing/Business Dev','Marketing/Business Dev'),
        ('Mechanical/Automotive Engineering','Mechanical/Automotive Engineering'),
        ('Merchandising','Merchandising'),
        ('Nurse/Medical Support','Nurse/Medical Support'),
        ('Oil/Gas Engineering','Oil/Gas Engineering'),
        ('Other Engineering','Other Engineering'),
        ('Others','Others'),
        ('Personal Care','Personal Care'),
        ('Pharmacy','Pharmacy'),
        ('Process Design Control','Process Design Control'),
        ('Product Management','Product Management'),
        ('Property/Real Estate','Property/Real Estate'),
        ('Public Relations','Public Relations'),
        ('Publishing','Publishing'),
        ('Purchasing/Material Mgmt','Purchasing/Material Mgmt'),
        ('Quality Assurance','Quality Assurance'),
        ('Quantity Surveying','Quantity Surveying'),
        ('Retail Sales','Retail Sales'),
        ('Sales - Corporate','Sales - Corporate'),
        ('Sales - Eng/Tech/IT','Sales - Eng/Tech/IT'),
        ('Sales - Financial Services','Sales - Financial Services'),
        ('Science Technology','Science Technology'),
        ('Secretarial','Secretarial'),
        ('Security/Armed Forces','Security/Armed Forces'),
        ('Social Services','Social Services'),
        ('Tech Helpdesk Support','Tech Helpdesk Support'),
        ('Telesales/Telemarketing','Telesales/Telemarketing'),
        ('Top Management','Top Management'),
        ('Training Dev.','Training Dev.'),
    )

    class Meta():
        model = SkillsInfo
        exclude = ("fk_skills_user",)

    skills = forms.ChoiceField(choices=SKILL_LIST,)

    def __init__(self, *args, **kwargs):
        super(SkillsForm, self).__init__(*args, **kwargs)

        self.fields['skills'].widget.attrs = {
            'type': 'text',
            'class': 'form-control select2',
            'width': '100%',
            'required': 'required',
        }

class CompanyForm(forms.ModelForm):
    class Meta():
        model = CompanyInfo
        exclude = ("fk_company_user",)
    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)


        self.fields['biometrics_id'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Biometrics ID',
            'required': 'required',
        }
        self.fields['company_id'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Company ID',
            'required': 'required',
        }

        self.fields['company_tin'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Company TIN',
            'required': 'required',
        }

        self.fields['designation'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Designation',
            'required': 'required',
        }

        self.fields['department'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Department',
            'required': 'required',
        } 

        self.fields['personal_tin'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Personal TIN',
        }

        self.fields['sss_number'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'SSS Number',
        }

        self.fields['pagibig'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Pag-ibig',
        }

        self.fields['philhealth'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Philhealth',
        }
        self.fields['vacation_leave_credits'].widget.attrs = {
            'class': 'form-control',  
            'readonly':'readonly',
        }
        self.fields['sick_leave_credits'].widget.attrs = {
            'class': 'form-control',  
            'readonly':'readonly',
        }

class TelephoneNumberForm(forms.ModelForm):
    class Meta():
        model = TelephoneNumberInfo
        exclude = ("fk_telephone_user",)

    def __init__(self, *args, **kwargs):
        super(TelephoneNumberForm, self).__init__(*args, **kwargs)

        self.fields['telephone_number'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Telephone Number',
            'required': 'required',
        }

class CutOffPeriodForm(forms.ModelForm):
    attendance_file = forms.FileField(validators=[file_validator], label="Attendance .xlsx file")
    class Meta:
        model = CutOffPeriodInfo
        fields = ("attendance_file",)

class AttendanceForm(forms.ModelForm):
    class Meta():
        model = AttendanceInfo
        exclude = ("id", "employee_profile", "cut_off_period")

        time_in = forms.TimeField(
        widget=forms.TimeInput(
            format='%I:%M', 
        ),
        input_formats=('%I:%M',),
        required=False,
        )

        time_out = forms.TimeField(
        widget=forms.TimeInput(
            format='%I:%M', 
        ),
        input_formats=('%I:%M',),
        required=False,
        )


    def __init__(self, *args, **kwargs):
        super(AttendanceForm, self).__init__(*args, **kwargs)

        self.fields['days_of_week'].label = False
        self.fields['days_of_week'].widget.attrs = {
            'class': 'form-control',
            'readonly': 'readonly',
        }
        self.fields['date'].label = False
        self.fields['date'].widget.attrs = {
            'class': 'form-control',
            'readonly': 'readonly',
            
        }
        self.fields['time_in'].label = False
        self.fields['time_in'].widget.attrs = {
            'class': 'form-control timeIn timepicker', 
            # 'autofocus': 'autofocus',
            'readonly': 'readonly',
        }
        self.fields['time_out'].label = False
        self.fields['time_out'].widget.attrs = { 
            'class': 'form-control timeOut timepicker', 
            # 'autofocus': 'autofocus',
            'readonly': 'readonly',
        }
        self.fields['late'].label = False
        self.fields['late'].widget.attrs = {
            'class': 'form-control',
            'readonly': 'readonly',
        }   
        self.fields['undertime'].label = False
        self.fields['undertime'].widget.attrs = {
            'class': 'form-control',
            'readonly': 'readonly',
        }
        self.fields['overtime'].label = False
        self.fields['overtime'].widget.attrs = { 
            'class': 'form-control', 
            # 'readonly': 'readonly',
        }
        # self.fields['payment_computation_for_work_done'].label = False
        # self.fields['payment_computation_for_work_done'].widget.attrs = {
        #     'class': 'form-control select2',
        # }
        # self.fields['payment_computation_overtime'].label = False
        # self.fields['payment_computation_overtime'].widget.attrs = {
        #     'class': 'form-control select2',
        # }
        self.fields['has_itenerary'].label = False
        self.fields['has_itenerary'].widget.attrs = {
            # 'class': 'form-control',
        }
        self.fields['has_leave'].label = False
        self.fields['has_leave'].widget.attrs = {
            # 'class': 'form-control',
        }
        self.fields['overtime_category'].label = False
        self.fields['overtime_category'].widget.attrs = {
            'class': 'form-control select2',
        }  
        self.fields['holiday'].label = False
        self.fields['holiday'].widget.attrs = {
            'class': 'form-control select2',
        }    

class AttendanceFormManual(forms.ModelForm):
    class Meta():
        model = AttendanceInfo
        exclude = ("id", "employee_profile", "cut_off_period")

        time_in = forms.TimeField(
        widget=forms.TimeInput(
            format='%I:%M', 
        ),
        input_formats=('%I:%M',),
        required=False,
        )

        time_out = forms.TimeField(
        widget=forms.TimeInput(
            format='%I:%M', 
        ),
        input_formats=('%I:%M',),
        required=False,
        )


    def __init__(self, *args, **kwargs):
        super(AttendanceFormManual, self).__init__(*args, **kwargs)

        self.fields['days_of_week'].label = False
        self.fields['days_of_week'].widget.attrs = {
            'class': 'form-control',
            'readonly': 'readonly',
        }
        self.fields['date'].label = False
        self.fields['date'].widget.attrs = {
            'class': 'form-control mydate',
            'readonly': 'readonly',
            
        }
        self.fields['time_in'].label = False
        self.fields['time_in'].widget.attrs = {
            'class': 'form-control timeIn timepicker', 
            # 'autofocus': 'autofocus',
            'readonly': 'readonly',
        }
        self.fields['time_out'].label = False
        self.fields['time_out'].widget.attrs = { 
            'class': 'form-control timeOut timepicker', 
            # 'autofocus': 'autofocus',
            'readonly': 'readonly',
        }
        self.fields['late'].label = False
        self.fields['late'].widget.attrs = {
            'class': 'form-control',
            'readonly': 'readonly',
        }   
        self.fields['undertime'].label = False
        self.fields['undertime'].widget.attrs = {
            'class': 'form-control',
            'readonly': 'readonly',
        }
        self.fields['overtime'].label = False
        self.fields['overtime'].widget.attrs = {
            'class': 'form-control',
            'type': 'number',
            #'readonly': 'readonly',
        }
        self.fields['has_itenerary'].label = False
        self.fields['has_itenerary'].widget.attrs = {
            # 'class': 'form-control',
        }
        self.fields['has_leave'].label = False
        self.fields['has_leave'].widget.attrs = {
            # 'class': 'form-control',
        }
        self.fields['overtime_category'].label = False
        self.fields['overtime_category'].widget.attrs = {
            'class': 'form-control select2',
        }   
        self.fields['holiday'].label = False
        self.fields['holiday'].widget.attrs = {
            'class': 'form-control select2',
        } 

        # self.fields['payment_computation_for_work_done'].label = False
        # self.fields['payment_computation_for_work_done'].widget.attrs = {
        #     'class': 'form-control select2',
        # }
        # self.fields['payment_computation_overtime'].label = False
        # self.fields['payment_computation_overtime'].widget.attrs = {
        #     'class': 'form-control select2',
        # }
  
class EmployeePayrollForm(forms.ModelForm):
    default_val = Decimal('0.00')

    # payroll_date = forms.DateField(
    #     widget=forms.DateInput(
    #         format='%b %d %Y',
    #         attrs={
    #             'id': 'payroll_date',
    #         }
    #     ),
    #     input_formats=('%b %d %Y',)
    # )
    #monthly_rate = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val, required=True)
    #monthly_allowance = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val)
    basic_pay = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val, required=True)
    allowance = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val)
    overtime_pay = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val)
    # legal_holiday = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val)
    # special_holiday = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val)
    late_or_absences = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val)
    salary_or_cash_advance = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val)

    # deductions
    sss_premiums = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val)
    philhealth_contribution = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val)
    pagibig_contribution = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val)
    withholding_tax = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val)
    pagibig_loan = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val)
    deducted_salary_cash_advance = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val)
    #thirteenth_month_pay = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val)


    class Meta():
        model = EmployeePayroll
        exclude = ("employee_fk","payroll_cutoff_period","payroll_date" ,"date_added","is_seen","thirteenth_month_pay")
    
    def __init__(self, *args, **kwargs):
        super(EmployeePayrollForm, self).__init__(*args, **kwargs)

        self.fields['basic_pay'].widget.attrs = {
            'id':'basicPay',
            'class': 'form-control',
            'step': 'any',
        }
        self.fields['allowance'].widget.attrs = {
            'id':'allowance',
            'class': 'form-control',
            'step': 'any',
        }
        self.fields['overtime_pay'].widget.attrs = {
            'id':'overtimePay',
            'class': 'form-control',
            'step': 'any',
        }
        # self.fields['legal_holiday'].widget.attrs = {
        #     'id':'legalHoliday',
        #     'class': 'form-control',
        # }
        # self.fields['special_holiday'].widget.attrs = {
        #     'id':'sundaySpecialHoliday',
        #     'class': 'form-control',
        # }
        self.fields['late_or_absences'].widget.attrs = {
            'id':'lateAbsences',
            'class': 'form-control',
            'step': 'any',
        }
        self.fields['salary_or_cash_advance'].widget.attrs = {
            'id':'salaryCashAdvance',
            'class': 'form-control',
            'step': 'any',
        } 
        self.fields['gross_pay'].widget.attrs = {
            'id': 'grossPay',
            'class': 'form-control text-green',
            'readonly': 'readonly',
            'step': 'any',
        }
        self.fields['net_pay'].widget.attrs = {
            'id': 'netPay',
            'class': 'form-control text-green',
            'style': 'font-weight:bold;',
            'readonly': 'readonly',
            'step': 'any',
        }
        #---
        self.fields['philhealth_contribution'].widget.attrs = {
            'id':'philhealContribution',
            'class': 'form-control',
            'step': 'any',
        } 
        self.fields['pagibig_contribution'].widget.attrs = {
            'id':'pagibigContribution',
            'class': 'form-control',
            'step': 'any',
        } 
        self.fields['sss_premiums'].widget.attrs = {
            'id':'sssPremius',
            'class': 'form-control',
            'step': 'any',
        }
        self.fields['withholding_tax'].widget.attrs = {
            'id':'withholdingTax',
            'class': 'form-control',
            'step': 'any',
        } 
        self.fields['pagibig_loan'].widget.attrs = {
            'id':'pagibigLoan',
            'class': 'form-control',
            'step': 'any',
        } 
        self.fields['deducted_salary_cash_advance'].widget.attrs = {
            'id':'deductionSalaryCashAdvance',
            'class': 'form-control',
            'step': 'any',
        }  
        self.fields['total_deduction'].widget.attrs = {
            'id': 'totalDeduction',
            'class': 'form-control text-red',
            'readonly': 'readonly',
            'step': 'any',
        }

class EmployeeSalaryForm(forms.ModelForm):
    default_val = Decimal('0.00')
    amount = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val, required=True)
    allowance = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val, required=True)
    class Meta():
        model = EmployeeSalary
        exclude = ("employee_salary_fk","date_added")

    def __init__(self, *args, **kwargs):
        super(EmployeeSalaryForm, self).__init__(*args, **kwargs)

        self.fields['amount'].widget.attrs = {
            'class': 'form-control',
            'required': 'required',
            'placeholder': "Enter the amount.",
        }
        self.fields['allowance'].widget.attrs = {
            'class': 'form-control',
            'required': 'required',
            'placeholder': "Enter the allowance.",
        }
        self.fields['reason'].widget.attrs = {
            'class': 'form-control',
            'required': 'required',
            'placeholder': "Enter the reason.",
        }

class EmployeeLeavesForm(forms.ModelForm):
    default_val = Decimal('0.00')
    # leave_credits = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val)
    # less_this_application = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val)
    # balance_as_of_this_date = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val)

    class Meta():
            model = EmployeeLeaves
            exclude = ("employee_leave_fk","date_filed","department","status","noted_by","checked_by","approved_by",)

    def __init__(self, *args, **kwargs):
        super(EmployeeLeavesForm, self).__init__(*args, **kwargs)

        # self.fields['department'].widget.attrs = {
        #     'class': 'form-control', 

        #     'placeholder': "Enter the department.",
        # }
        #status must be disabled on the employee side
        # self.fields['status'].widget.attrs = {
        #     'class': 'form-control',  
        # }
        self.fields['no_days'].widget.attrs = {
            'id': 'noOfDays',
            'class': 'form-control',  
            'readonly': 'readonly',
        }
        self.fields['inclusive_dates'].widget.attrs = {
            'id': 'inclusiveDates',
            'readonly': 'readonly',
            'class': 'form-control',  
        }
        self.fields['reasons'].widget.attrs = {
            'class': 'form-control', 
            'placeholder': "Enter the reasons.",
        }
        self.fields['classification_of_leave'].widget.attrs = {
            'id': 'classificationOfLeave',
            'class': 'form-control',  
            'style': 'width:100%',
        }
        self.fields['leave_credits'].widget.attrs = {
            'class': 'form-control',  
            'readonly':'readonly',
        }
        self.fields['less_this_application'].widget.attrs = {
            'class': 'form-control',  
            'readonly':'readonly',
        }
        self.fields['balance_as_of_this_date'].widget.attrs = {
            'class': 'form-control',  
            'readonly':'readonly',
        }
        self.fields['remarks'].widget.attrs = {
            'class': 'form-control',  
            'readonly':'readonly',
        } 
        # self.fields['noted_by'].widget.attrs = {
        #     'class': 'form-control',  
        # }
        # self.fields['checked_by'].widget.attrs = {
        #     'class': 'form-control',  
        # }
        # self.fields['approved_by'].widget.attrs = {
        #     'class': 'form-control',  
        # }

class EmployeeIteneraryForm(forms.ModelForm):
    class Meta():
            model = EmployeeItenerary
            exclude = ("employee_itenerary_fk","date_filed",)

    def __init__(self, *args, **kwargs):
        super(EmployeeIteneraryForm, self).__init__(*args, **kwargs)

class EmployeeIteneraryDetailsForm(forms.ModelForm):
    class Meta():
        model = EmployeeIteneraryDetails
        exclude = ("employee_itenerary",)

    def __init__(self, *args, **kwargs):
        super(EmployeeIteneraryDetailsForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs = {  
            'class': 'form-control frmEIDDate',   
            'readonly': 'readonly',
            #'required': 'required',
        }
        self.fields['timeIn'].widget.attrs = { 
            'class': 'form-control frmEIDTimeIn',  
            'readonly': 'readonly', 
            #'required': 'required',
        }
        self.fields['timeOut'].widget.attrs = { 
            'class': 'form-control frmEIDTimeOut', 
            'readonly': 'readonly',  
           # 'required': 'required',
        }
        self.fields['reasons'].widget.attrs = { 
            'class': 'form-control ifReasons',   
            #'required': 'required',
        }

class ConcernsEmployeeForm(forms.ModelForm):
    class Meta():
        model = Concerns
        exclude = ("sender","reply","date_filed",)
    def __init__(self, *args, **kwargs):
        super(ConcernsEmployeeForm, self).__init__(*args, **kwargs)
        self.fields['receiver'].widget.attrs = {
            'id': 'concernTo',
            'style': 'width:100%',
            'required':'required', 
            'class': 'form-control',  
        }
        self.fields['subject'].widget.attrs = {
            'class': 'form-control',  
        }
        self.fields['message'].widget.attrs = {
            'class': 'form-control',  
        }

class ConcernsReplyEmployeeForm(forms.ModelForm):
    class Meta():
        model = Concerns
        exclude = ("sender","receiver","subject","message","date_filed",)
    def __init__(self, *args, **kwargs):
        super(ConcernsReplyEmployeeForm, self).__init__(*args, **kwargs)
      
      
        self.fields['reply'].widget.attrs = {
            'class': 'form-control',  
            'rows' : '5',
        }

class OvertimeForm(forms.ModelForm):
    class Meta():
        model = Overtime
        exclude = ("employee_overtime","date_filed")
    def __init__(self, *args, **kwargs):
            super(OvertimeForm, self).__init__(*args, **kwargs)

class OvertimeDetailsForm(forms.ModelForm):
    class Meta():
        model = OvertimeDetails
        exclude = ("overtime",)
    def __init__(self, *args, **kwargs):
        super(OvertimeDetailsForm, self).__init__(*args, **kwargs)
        self.fields['date_rendered'].widget.attrs = {  
            'class': 'form-control frmDateRender',   
            # 'readonly': 'readonly',
            #'required': 'required',
        }
        self.fields['day'].widget.attrs = {  
            'class': 'form-control',   
            'readonly': 'readonly',
            #'required': 'required',
        }
        self.fields['re_sp_ot'].widget.attrs = {  
            'class': 'form-control select2',  
            'width': '100%', 
            #'readonly': 'readonly',
            #'required': 'required',
        }
        self.fields['description'].widget.attrs = {  
            'class': 'form-control frmDescription',    
            #'readonly': 'readonly',
            #'required': 'required',
        }
        self.fields['product'].widget.attrs = {  
            'class': 'form-control frmProduct',    
            #'readonly': 'readonly',
            #'required': 'required',
        }
        self.fields['timeIn'].widget.attrs = {  
            'class': 'form-control frmTimeIn',   
            'readonly': 'readonly',
            #'required': 'required',
        }
        self.fields['timeOut'].widget.attrs = {  
            'class': 'form-control frmTimeOut',   
            'readonly': 'readonly',
            #'required': 'required',
        }
        self.fields['duration'].widget.attrs = {  
            'class': 'form-control',   
            'readonly': 'readonly',
            #'required': 'required',
        }

