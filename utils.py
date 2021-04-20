import random
import string

def genname(length):
    name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    return name