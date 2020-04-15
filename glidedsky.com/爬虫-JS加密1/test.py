def get_str_sha1_secret_str(res:str):
    import hashlib
    """
    使用sha1加密算法，返回str加密后的字符串
    """
    sha = hashlib.sha1(res.encode('utf-8'))
    encrypts = sha.hexdigest()
    print(encrypts)
    return encrypts


print(get_str_sha1_secret_str("Xr0Z-javascript-obfuscation-1157107341556"))

import math

t = math.floor((int(157107475107)-99)/99)
print(t)