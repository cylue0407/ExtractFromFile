#Regualr Expression Class
import re
#match DateTime
def reEXBirth(usrInput):
    pattern = '^\d{4}-\d{2}-\d{2}$'
    result = re.match(pattern, usrInput)
    return result

#match Email
def reEXEmail(usrInput):
    pattern_list = ['^.*@163.com$','','']
    if(re.match(pattern, usrInput)):
        re.findall(pattern, usrInput)
    
    return result

#match phone number+
