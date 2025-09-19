import random, time 

class Fighter:
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.__health = starting_health
        self.weapon = weapon
        self.shield = shield
  
    def report(self):
        print(self.name+':'+ ' Health: '+ str(self.__health))

    def is_dead(self):
        if self.__health <= 0:
            return True
        else:
            return False

    def random_attack(self):
        attack_power = random.randint(self.weapon/2, self.weapon*2)
        print('Attack power:', attack_power)
        return attack_power
    
    def skill_attack(self):
        attack_power = random.randint(self.weapon//2, self.weapon*2)
        target = random.randint(2,6)
        print("Hit enter in exactly",target,'seconds')
        tic = time.time()
        input()
        toc = time.time()
        time_taken = toc - tic
        multiplier = 3 - abs(target - time_taken)
        if multiplier < 2:
            multiplier = 0
            
        print('Attack power:', attack_power)
        print('Multiplier:', round(multiplier, 2))
        return int(attack_power * multiplier)

    def defend(self,attack_power):
        damage = attack_power - self.shield
        if damage >  0:
            self.__health -= damage
            print('Damage:', damage)
        else:
            print('No damage')

class Wizard(Fighter):
    def __init__(self,name,starting_health,weapon,shield,magic):
        super().__init__(name,starting_health,weapon,shield)
        self.magic = magic

    def random_attack(self):
        attack_power = random.randint(self.weapon/2,self.weapon)
        print('Attack power:',attack_power)
        return attack_power + self.magic

you = Fighter('You',100,60,20)
wiz = Wizard('The Grey Wizard',300,30,10,50)

you.report()
wiz.report()

while True:
    print('YOU ATTACK THE WIZARD!')
    wiz.defend(you.skill_attack())
    wiz.report()
    time.sleep(2)
    print("")
    if wiz.is_dead():
        print("YOU WIN!")
        break
    print("The Wizard attacks you...")
    you.defend(wiz.random_attack())
    you.report()
    time.sleep(2)
    if you.is_dead():
        print('The Grey Wizard wins :(')
        break
    print("")