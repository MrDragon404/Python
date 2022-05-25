def primeNumber(number):
    flag = False
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                flag = True
                break

        if flag == True:
            print(number, "Число не простое")
        else:
            print(number, "Простое число")

for i in range(1, 100):
    primeNumber(i)
