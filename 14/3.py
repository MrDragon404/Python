array1 = [57, 100, 32, ]
array2 = [34,  53, 100]
result = []

#for i in array1:
#    for j in array2:
#        if i == j:
#            result.append(i)
#            break

array1.sort()
array2.sort()
n = min(len(array1), len(array2))

for i in range(n):
    if array1[i] == array2[i]:
        result.append(array1[i])

print(result)
