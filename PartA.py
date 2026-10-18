
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Battery Size: {self.battery_size} kWh")

#Car classs Test
c1 = Car("Mazda", "CX-50", 2025)
c1.display_info()

# Elec Car Test
e1 = ElectricCar("Tesla", "X", 2024, 30)
e1.display_info()
e1.describe_battery()