class Pet:

#Defining a class
    def __init__(self, name, category, age = 0):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = False

#Using special __str__ method to print statement
    def __str__(self):
         my_status = '\nName: ' + self.name + '\nCategory: ' + self.category + '\nAge: ' + self.age + '\nCredit Card information: ' + self.ccard + "\nVaccinated?: " + self.vaccinated

#function is returned
         return my_status

#Allcoate all variables from 'defining class function' to 1 variable
p1 = Pet('\nBonnie' , '\nCat', 5)

#print the name, category and age.
print(p1.name, p1.category, str(p1.age))
