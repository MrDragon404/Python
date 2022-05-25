name1 = 'Вася'
name2 = 'Кузя'

name1, name2 = name2, name1

# if условие1 правда:
#    команды1
# elif Условие2 правда:
#    команда2
# elif:
#    команда3

n1 = input("1 оценка")
n2 = input("2 оценка")
n3 = input("3 оценка")

srf = (int(n1) + int(n2) + int(3) ) / 3

if 2 < srf <= 3:
    print('Фу двоечник')
elif 3 < srf <= 4:
    print('Почти абоба')
elif 4 < srf < 5:
    print('Хорошист')
elif srf == 5:
    print('БОТАНИК')
else:
    print('Введи правильные оценки')
