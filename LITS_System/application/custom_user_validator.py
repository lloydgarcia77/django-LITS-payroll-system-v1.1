from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from application import models

def validate(user, is_managing_director=False, is_human_resource=False, is_business_unit_head=False, is_employee=False):     
    if user.is_active and user.is_staff:
       
        try:
             
            # Check if the user has a complete detaiil
            profile = models.PersonalInfo.objects.all().get(fk_user=user)
            company = models.CompanyInfo.objects.all().get(fk_company_user=user)
            roles_and_permission = models.RolesPermission.objects.all().get(employee_ci_rp_fk=company)   
            
            is_valid = False
            
            if is_managing_director:  
              
                if roles_and_permission.role == "Managing Director":      
                    is_valid = True

            if is_human_resource: 
                if roles_and_permission.role == "Human Resource":    
                    is_valid = True 

            if is_business_unit_head:
                if roles_and_permission.role == "Business Unit Head":     
                    is_valid = True 

            if is_employee: 
                if roles_and_permission.role == "Employee":       
                    is_valid = True 
  
            
            if is_valid:
                return user           
            
        except (models.PersonalInfo.DoesNotExist,models.CompanyInfo.DoesNotExist,models.RolesPermission.DoesNotExist): 
            return False
        # finally:
        #     return True

    else: 
        raise Http404()



# __ prefix private
def __private():
    print("This function is private!")

# _ prefix protected
def _protected():
    print("This function is protected!")