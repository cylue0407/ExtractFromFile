#Regualr Expression Class
import re
#match DateTime
def reEXBirth(usrInput):
    pattern = '^\d{4}-\d{2}-\d{2}$'
    result = re.match(pattern, usrInput)
    return result

#match Email
def reEXEmail(usrInput):
    pattern_list = ['^.*@126\.com$','^.*@139\.com$','^.*@163\.com.?','^.*@sina\.com$','^.*@qq\.com$','^.*@sohu\.com$','^.*@zohomail\.com$','^.*@189\.com$','^.*@yeah\.net$','^.*@.+\.cn$',]
    matchStr = ''
    for pattern in pattern_list:
        print(pattern)
        if(re.match(pattern, usrInput)):
            #matchStr += re.findall(pattern, usrInput)
            print(re.findall(pattern,usrInput))
    result = matchStr
    return result

#match phone number+
