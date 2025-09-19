class Pet:
    def __init__(self, name, category, age = 0):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = False
        self.account_balance = 0
    
    def have_birthday(self):
        self.age += 1
    
    def vaccinate(self):
        if self.vaccinated == True:
            print(self.name,'is already vaccinated')
        else:
            self.vaccinated = True

    def clear_balance(self):
        self.account_balance = 0

    def calculate_human_age(self):
        if self.category == 'Dog':
            print(self.name,'human age:',self.age*7)
        elif self.category == 'Cat':
            print(self.name,'human age:',self.age*6)
        else:
            print(self.name,'human age is unknown')

    def __str__(self):
        payment_status = 'unregistered'
        if len(self.ccard) == 19:
            payment_status = 'registered'

        my_status = 'Name: ' + self.name +'\nCategory: ' + self.category + '\nAge: ' + str(self.age) +'\nPayment status: ' + payment_status + '\nVaccinated: '+ str(self.vaccinated)
        return my_status

p1 = Pet(name = 'Bonnie', category = 'Cat', age = 10)
p1.have_birthday()
p1.vaccinate()
p1.vaccinate()

print(p1)
p1.calculate_human_age()



 