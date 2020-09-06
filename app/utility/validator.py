import re 
def validate_name(name):
    digit = re.findall("[0-9]", name)
    sp = re.findall("[!?@#$%^&*()_+]",name)
    space = re.findall("[\s]",name)
    if digit or sp or not name or space:
        return False
    else:
        return True



def validate_id(id):
    digit = re.findall("[0-9]", id)
    sp = re.findall("[!?@#$%^&*()_+]",id)
    space = re.findall("[\s]",id)
    if len(id.split()) < 13 or not digit or None or sp or space:
        return False
    else :
        return True


def validate_phone_number(phone_number):
    return True
