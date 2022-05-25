import random

array = []

for i in range(100):
    array.append(random.randint(0,i))

#print(array)

def binary (arr, n):
    arr.sort()
    start = 0
    end = len(arr) - 1
    step = 0

    while start <= end:
        step += 1
        mid = (start + end)//2
        if n == arr[mid]:
            return mid

        if n < arr[mid]:
            end = mid - 1

        else:
            start = mid + 1

    return -1
array.sort()
print(array)
print(binary(array,11))
