import re
def name_of_email(addr):
    re_email = re.compile(r'^(<?)([\w\s]*)(>?)([\w\s]*)@([\w.]+)')
    if not re_email.match(addr):
        return None
    else:
        g = re_email.match(addr)
        return g.group(2)


print(name_of_email('<Tom Paris> tom@voyager.org'))