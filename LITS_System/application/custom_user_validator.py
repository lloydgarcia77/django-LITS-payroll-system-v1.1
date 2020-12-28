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
            
        except (models.PersonalInfo.DoesNotExist): 
            return False
        except (models.CompanyInfo.DoesNotExist):
            return False
        except (models.RolesPermission.DoesNotExist):
            return False

        # finally:
        #     return True

    else: 
        raise Http404()

def check_order(current_user, form_user):
    order = ['Managing Director','Human Resource','Business Unit Head','Employee']

    form_user_role = form_user.employee_leave_fk.fk_user.company_to_user.employee_ci_rp_fk_r.role
    form_user_immidiate_head = form_user.employee_leave_fk.fk_user.company_to_user.employee_ci_rp_fk_r.immidiate_head

    current_user_immidiate_head = current_user.company_to_user.employee_ci_rp_fk_r.immidiate_head
    current_user_role = current_user.company_to_user.employee_ci_rp_fk_r.role
    current_user = current_user.company_to_user
    """
    list index() parameters
    The list index() method can take a maximum of three arguments:

    element - the element to be searched
    start (optional) - start searching from this index
    end (optional) - search the element up to this index
    """ 
    if form_user_role in order:
        index = order.index(form_user_role)
        print(index,'->',form_user_role, '->', form_user_immidiate_head)
    if current_user_role in order:
        index = order.index(current_user_role)
        print(index,'->',current_user_role, '->', current_user_immidiate_head)

    print("Current User:",type(current_user),'vs',type(current_user_immidiate_head))

# __ prefix private
def __private():
    print("This function is private!")

# _ prefix protected
def _protected():
    print("This function is protected!")