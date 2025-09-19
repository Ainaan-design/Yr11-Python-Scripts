import random

class Fighter:
    def __init__(self, name, starting_health, weapon, shield):
        self.name = name
        self.health = starting_health
        self.weapon = weapon
        self.shield = shield
    
#2. Create methods: report and random_attack:
    def report(self):
        print(self.name,":",' Health: '+str(self.health))
    
    def random_attack(self):
        attack_power = random.randint(self.weapon/2, self.weapon*2)
        print('Attack power:',attack_power)
        return attack_power

#3. Create 2 Fighter objects and test out the methods:
you = Fighter("You",100,60,20)
troll = Fighter("Troll",200,30,10)

you.report()
troll.report()

while True:
    print("YOU ATTACK THE TROLL")
    troll.health -= (you.random_attack())
    troll.report()
    print("")
    print("THE TROLL ATTACKS YOU...")
    you.health -= (troll.random_attack())
    you.report
    break

