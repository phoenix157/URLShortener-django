import random, string

options = string.ascii_letters + string.digits

def code_generator():
    return ''.join(random.choice(options) for _ in range(7))

print(code_generator())