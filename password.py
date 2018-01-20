import hashlib
def calc_md5(password):

    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    print(md5.hexdigest())


calc_md5('gy972856')