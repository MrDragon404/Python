import random

players = ["Андрей", "Тихон", "Павел", "Дарлин", "Егор.Ев", "Егор.Яр", "Данил"]
p = ["-300$", "+1000$", "-500$", "-9999$", "0", "+100000000000000000000$", "-400$"]

player = random.choice(players)
money = random.choice(p)

if "-" or "0" in money:
   print(f"Игрок {player} проиграл {money}")
else:
   print(f"Игрок {player} выйграл {money}")
