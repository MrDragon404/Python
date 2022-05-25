import string

upper_case = False
lower_case = False
special_chars = False
digits = False
length = False

password = input("Введите пароль для проверки : ")

for letter in password:
    if letter in string.ascii_lowercase:
        lower_case = True
    if letter in string.ascii_uppercase:
        upper_case = True

    if letter in string.digits:
        digits = True

    if letter in string.punctuation:
        special_chars = True

if len(password) > 10:
    length = True

characters = [upper_case,
              lower_case,
              digits,
              special_chars,
              length
]
# print(characters)
score = 0
error = ""

for i in range(0, len(characters)):
    if characters[i] == True:
        score += 1
    else:
        if i == 0:
            error += " нет заглавных букв, "
        elif i == 1:
            error += " нет строчных символов, "

        elif i == 2:
            error += " нет цифер, "

        elif i == 3:
            error += " нет спец символов, "

        elif i == 4:
            error += " длина > 10 имволов, "

print(f"Надежность пароля {score} из 5, ошибки: {error}")