#Defining a class
class Pet:
    def __init__(self, name, category, age = 0):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = True
 #Using special string print function   
    def __str__(self):
        payment_status = 'unregistered'
        if len(self.ccard) == 19:
            payment_status = 'registered'
        my_status = '\nName: ' + self.name + '\nCategory: ' + self.category + '\nAge: ' + str(self.age) + '\nPayment Status: ' + payment_status + '\nVaccinated: ' + str(self.vaccinated)
        return my_status
#Pet classes
p1 = Pet('Bonnie', 'Cat')
p2 = Pet('Clyde' , 'Dog' , 7)
p3 = Pet(category = 'Rabbit' , name = 'Ruby' , age = 13)
p4 = Pet(age = 67 , name = "Bombardillo Crocoldillo" , category = "Crocodile")

#Assighning pets to 1 variable
pets = (p1,p2,p3,p4)

#Using 'for' loop to print all the pet classes
for pet in pets:
    print(pet)
    print("")