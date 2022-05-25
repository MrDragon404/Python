import random
array = []

for i in range(1, 100):
    array.append(random.randint(1, i))

def bubbleSort(arr):
    for i in range(len(arr)):
        for k in range(len(arr)):
            if arr[i] < arr[k]:
                arr[i], arr[k] = arr[k], arr[i]















print("До ПОоослеее")
print(array)
bubbleSort(array)
print("После сортировки")
print(array)
