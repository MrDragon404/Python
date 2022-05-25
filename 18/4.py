def palindrom (s):
    s = s.lower()
    if s == s[::-1]:
        print("Полидром")
    else:
        print("Нет")
palindrom('око')
palindrom('Анна')
palindrom('дед')
palindrom('вася')
