# month = input("Месяц : ")
# month = month.lower()
# if month == "июнь" or month == "апрель" or month=="сентябрь" or month=="ноябрь":
#     print("30 days in month")
# elif month == "февраль":
#     print("28 - 29 days")
# else:
#     print("31 days")
month = input("месяц")
day30 = ["июнь", "апрель", "сентябрь", "ноябрь",]
day31 = ["май", "март", "июль","август","декабрь","октябрь","январь"]
day28 = ["февраль"]

if month in day30:
    print("30 дней")
elif month in day31:
    print("31дней")
elif month == "февраль":
    print("28-29 дней")
else:
    print("Гуляй Вася")
