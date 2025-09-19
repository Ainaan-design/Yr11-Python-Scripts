class Car:
    def __init__(self,make,model,year,for_sale,price=None):
        self.make = make
        self.model = model
        self.year = year
        self.for_sale = for_sale
        self.price = price

    def __str__(self):
        my_status = '\nMake: ' + self.make + '\nModel: ' + self.model + '\nYear: ' + str(self.year) + '\nPrice: ' + str(self.price) + '\nFor sale or not for sale: ' + self.for_sale
        return my_status

c1 = Car('Mazda','6',2005,'Not for sale')

cars = [c1]

for car in cars:
    print(car)

class Car2:  
    def __init__(self,make,model,year,for_sale,price=5000):
        self.make = make
        self.model = model
        self.year = year
        self.for_sale = for_sale
        self.price = price

    def __str__(self):
        my_status = '\nMake: ' + self.make + '\nModel: ' + self.model + '\nYear: ' + str(self.year) + '\nPrice: ' + str(self.price) + '\nFor sale or not for sale: ' + self.for_sale
        return my_status
    
c2 = Car2('Toyota','Yaris',2007,'For sale')

cars = [c2]

for car in cars:
    print(car)

class Car3:  
    def __init__(self,make,model,year,for_sale,price_two=35000):
        self.make = make
        self.model = model
        self.year = year
        self.for_sale = for_sale
        self.price_two = price_two

    def __str__(self):
        my_status = '\nMake: ' + self.make + '\nModel: ' + self.model + '\nYear: ' + str(self.year) + '\nPrice: ' + str(self.price_two) + '\nFor sale or not for sale: ' + self.for_sale
        return my_status


c3 = Car3('Toyota','Hilux',2011,'For sale')

cars = [c3]

for car in cars:
    print(car)
    

class Car4:  
    def __init__(self,make,model,year,for_sale,price_two=None):
        self.make = make
        self.model = model
        self.year = year
        self.for_sale = for_sale
        self.price_two = price_two

    def __str__(self):
        my_status = '\nMake: ' + self.make + '\nModel: ' + self.model + '\nYear: ' + str(self.year) + '\nPrice: ' + str(self.price_two) + '\nFor sale or not for sale: ' + self.for_sale
        return my_status


c3 = Car4('BMW','M4 Competition',2021,'Not for sale')

cars = [c3]

for car in cars:
    print(car)
    
class Car5:  
    def __init__(self,make,model,year,for_sale,price_two=300000):
        self.make = make
        self.model = model
        self.year = year
        self.for_sale = for_sale
        self.price_two = price_two

    def __str__(self):
        my_status = '\nMake: ' + self.make + '\nModel: ' + self.model + '\nYear: ' + str(self.year) + '\nPrice: ' + str(self.price_two) + '\nFor sale or not for sale: ' + self.for_sale
        return my_status


c3 = Car5('Porsche','GT3RS',2021,'For sale')

cars = [c3]

for car in cars:
    print(car)