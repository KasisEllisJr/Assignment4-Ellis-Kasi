
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.__mileage = 0

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

    def get_mileage(self):
        return self.__mileage

    def set_mileage(self, mileage):
        if mileage >= self.__mileage:
            self.__mileage = mileage
        else:
            print("Mileage cannot be decreased.")

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Battery Size: {self.battery_size} kWh")

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

#Car classs Test
c1 = Car("Mazda", "CX-50", 2025)
c1.display_info()

# Elec Car Test
e1 = ElectricCar("Tesla", "X", 2024, 30)
e1.display_info()
e1.describe_battery()

#Mileage Test
print(f"Current Mileage: {c1.get_mileage()} km")

c1.set_mileage(15000)
print(f"Updated Mileage: {c1.get_mileage()} km")

c1.set_mileage(-500)
print(f"Final Mileage: {c1.get_mileage()} km")