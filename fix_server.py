import os
import pickle
import hmac
import hashlib

def reverse_fun():
      try:
        with open("users.json","rb") as f:
            data = f.read()
      except FileNotFoundError:
        return "users.json NOT found"

      try:
          safecode,recvd_digest = data.split(bytes('-','utf-8'))
      except ValueError:
          return "Not enough arguments or empty json"
      
      digest = hmac.new(bytes('I-w1ll-h3ck-Y0u','utf-8'),safecode,hashlib.sha1).hexdigest()
      
      if hmac.compare_digest(recvd_digest,bytes(digest,'utf-8')):
          d = pickle.loads(safecode)
          return d
      else:
          return "Invalid Hash"

if __name__ == '__main__':
      print(reverse_fun())
