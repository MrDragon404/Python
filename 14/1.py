def splitWord(s):
    result = []
    for letter in s:
        result.append(letter)
    return result

#print(splitWord("Вася"))

def annagramma(s1, s2):
    if len(s1) != len(s2):
        return False
    s1 = s1.lower()
    s2 = s2.lower()
    arr1 = splitWord(s1)
    arr1.sort()
    arr2 = splitWord(s2)
    arr2.sort()
    s1 = "".join(arr1)
    s2 = "".join(arr2)
    return s1 == s2

print(annagramma("Аня","Яна"))
