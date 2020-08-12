#Regualr Expression Class
import re
#match DateTime
def reEXBirth(usrInput):
    pattern = '^\d{4}-\d{2}-\d{2}$'
    result = re.match(pattern, usrInput)
    return result

#match Email
def reEXEmail(usrInput):
    pattern_list = ['@(?:126.com)','@(?:139.com)','@(?:163.com)',
        '@(?:sina.com)','@(?:qq.com)','@(?:sohu.com)','@(?:zohomail.com)',
        '@(?:189.com)','@(?:yeah.net)','@((?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?.)cn)']
    pattern_prefix = "[a-z0-9!#$%&*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`{|}~-]+)*"
    matchList = []
    for pattern in pattern_list:
        regx = re.compile(str("(" + pattern_prefix + pattern + ")"))
        matchStr = re.findall(regx,usrInput)
        for item in matchStr:
            matchList.append(format(item))
    result = matchList
    print("End")
    return result

#match phone number+
