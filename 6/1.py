#Function

def summa(a, b):
    return a+b

#print(summa(3, 5))

def summa1(*args):
    s  = 0
    for number in args:
        s += number
    return s


#print(summa1(1,2,3,4,5,6,7,8,9,10,11,22,3,3,45,5,6,6))



def printNumbers():
    global a
    print(a,b)

a = 5
b = 6





