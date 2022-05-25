n = input("Введите числа : ")

def fizzBuzz(number):
    s = ""
    number = int(number)
    for x in range(1, number+1):
        if x % 3 == 0 and x % 5 != 0:
            s += "fizz\n"
        elif x % 5 == 0 and x % 3 != 0:
            s += "buss\n"
        elif x % 3 ==0 and x % 5 == 0:
            s += "fizzbuzz\n"
        else:
            s += str(x) + "\n"
    return s

print(fizzBuzz(n))
