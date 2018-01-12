import re
def is_valid_email(addr):
    if re.match(r'[a-zA-Z_.]+@[a-zA-Z]*.com',addr):
        return True
    else:
        return False


print(is_valid_email('@gmail.com'))
print(is_valid_email('bill.gates@microsoft.cm'))
print(is_valid_email('bob#example.com'))
print(is_valid_email('mr-bob@example.com'))

