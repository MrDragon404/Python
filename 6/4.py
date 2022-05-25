class Human:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def voice(self):
        print(f"My name is {self.name}")

BoB = Human("BoB", 23, 45)
Jon = Human("Jon", 23, 79)
Tom = Human("Tom", 65, 99)
Tom.voice()
BoB.voice()
