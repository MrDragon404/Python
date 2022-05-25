import random

def randomPassword(n):
    str ="1234567890zxcvbnm,./';lkjhgfdsaqwertyuiop[]!@#$%^&*()_+|"
    password = ""
    i = 0
    while i <= n:
        password += random.choice(str)
        i += 1

    return password

print(randomPassword(1200000000))
