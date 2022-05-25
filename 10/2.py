volwes_letters = ["а","и","у","е","о","ю","я","э","ё"]

s = input("Введите текст")

def countOfVolwsLerrers(str):
    count = 0
    for l in str:
        if l in volwes_letters:
            count += 1

    return count

print(countOfVolwsLerrers(s))
