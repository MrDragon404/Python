# blueprint -> object

class Unit:
    def run(self):
        print("run")

    def die(self):
        print("die")


class Worker(Unit):
    def work(self):
        print("work")

class Warior(Unit):
    def fight(self):
        print("fight")

class Wizard(Warior):
    def magic(self):
        print("magic")

worker1 = Worker()
worker2 = Worker()
worker1.run()
worker1.work()

warior1 = Warior()
warior1.fight()

wizard = Wizard()
wizard.magic()
wizard.fight()






