import random, time 

class Fighter:
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.health = starting_health
        self.weapon = weapon
        self.shield = shield

#Function for the health status  
    def report(self):
        print(self.name+':'+' Health: '+str(self.health))

#Function for generating random attack power:
    def random_attack(self):
        attack_power = random.randint(self.weapon/2, self.weapon*2)
        print('Attack power: ', attack_power)
        return attack_power
   
#Function used for calculating the damage done to either player or troll.
    def defend(self,attack_power):
        damage = attack_power - self.shield
        if damage > 0:
            self.health -= damage
            print('Damage:',damage)
        else:
            print('No damage')
           


you = Fighter("You",100,60,20)
troll = Fighter('Troll',200,30,10)

#The health of both player and troll after a fight.
you.report()
troll.report()

#Using a loop to show the battle between troll and player
while True:
#Code for when player is attacking troll
    print("You attack the troll".upper())
    troll.defend(you.random_attack())
    troll.report()
    time.sleep(4)
    if troll.health <= 0:
        print('You win!')
        print("")
        break
#Code for when troll is attacking you
    print("The troll attacks you...".upper())
    you.defend(troll.random_attack())
    you.report()
    time.sleep(4)
    if you.health <= 0:
        print('The troll wins, You lose...')
        print("")
        break
    


