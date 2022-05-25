# list, tuple, dict, set

# list
# Mutable, Immutable
marks = [3, 4, 5, 3, 4]
      #  0  1  2  3  4
marks[4] = 5
marks.append(2)
#print(marks[5], len(marks))
#print(marks[0:3], marks[::-1])

arr = list(("Вася", 5, True, 12.5))
#print(arr)

lessons = ("Мат", "История","Информатика")

t = tuple((3, 4, 5))
#print(len(lessons))

s = {"Вася", "Вася", 1, 2, 4, 1,}
#print(s)


### dict
d = {
    "Егор1":14,
    "Егор2":13,
    "Павел":9,
    "Андрей":12,
    "Тихон":14
}
d["Павел"] = 10
