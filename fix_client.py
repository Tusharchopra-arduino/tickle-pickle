import os
import pickle
import hmac
import hashlib

def fun(name,password):
    s = {"username":name,"password":password}
    safecode = pickle.dumps(s)

    # hashing with shared key
    digest = hmac.new(bytes('I-w1ll-h3ck-Y0u','utf-8'),safecode,hashlib.sha1).hexdigest()
    
    with open("users.json","wb") as f:
        f.write(safecode+bytes('-','utf-8'))
        f.write(bytes(digest,'utf-8'))
    return safecode

if __name__ == '__main__':
    # python 2 compatibility
    try:
        u = str(raw_input("Username : "))
        p = str(raw_input("Password : "))
    except NameError:
        u = input("Username : ")
        p = input("Password : ")

    yo_fun = fun(u,p)
