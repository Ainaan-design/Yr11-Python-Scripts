class Car:
    def __init__(self, make, model, year, colour):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour
    
    def start(self):
        print(f"{self.make} {self.model} is starting.")

    def stop(self):
        print(f"{self.make} {self.model} is stopping.")

car1 = Car("Ford", "Mustang", 2021, "Black")

car1.start()
car1.stop()     

print(f"Make: {car1.make}, Model: {car1.model}, Year: {car1.year}, Colour: {car1.colour}")