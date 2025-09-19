class Pet:
    def __init__(self, name, category, breed = None, age = 0):
        self._name = name
        self.__category = category
        self.__breed = breed
        self.age = age
        self.__ccard = 'unknown'
        self.vaccinated = False
        self.weight = 0

    
    def get_weight(self):
        return self.weight
    
    
    
    def set_weight(self, new_weight):
        if type(new_weight) == int or type(new_weight) == float:
            if new_weight > 0:
                self.weight = new_weight
            else:
                print("Please enter a positive number for weight")
        else:
            print("Please enter a number for weight")

p1 = Pet(name = 'Bonnie',category = 'Cat',age = 12)

p1.set_weight(23)

print('Bonnies weight:', p1.weight)
print(p1)







