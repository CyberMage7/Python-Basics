class Car:
    color= "black"

    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped...")
    
class toyotaCar(Car):
    def __init__(self, name):
        self.name = name

class Fortuner(toyotaCar):    #Multi-level Inheritance
    def __init__(self, type):
        self.type = type


car1 = Fortuner("petrol")
print(car1.start())