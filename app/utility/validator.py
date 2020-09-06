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
    return True


def validate_phone_number(phone_number):
    return True
