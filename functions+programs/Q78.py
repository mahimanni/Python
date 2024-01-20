import random
import secrets
#6 digit random secured otp(100000-999999)
securenum=secrets.randbits(100000,999999)
print(securenum)
