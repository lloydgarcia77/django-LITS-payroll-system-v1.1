from django import template
# https://docs.djangoproject.com/en/3.1/howto/custom-template-tags/

register = template.Library()


@register.simple_tag
def sum(val1, val2, *args):  
    return float(val1) + float(val2)

@register.simple_tag
def iterate(list): 
    output = ""
    arr = list.strip("[]")
    newList = [arr]
    for l in newList:        
        output = l.replace("'","")
    return output
 