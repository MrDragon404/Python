# for
#s = 'hello world And Python'
s = input("Введите строку  : ")
# letter1 = 'a', letter2 = 'b', letter1 < letter2

big = 0
small  = 0

for letter in s:
    if letter >= 'a' and letter <= 'z':
        small += 1
    elif letter >= 'A' and letter <= 'Z':
        big += 1

print(f'Small = {small} Big = {big}')




