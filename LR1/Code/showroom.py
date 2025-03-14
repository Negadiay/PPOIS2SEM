from car import Car

class Showroom:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def list_cars(self):
        return [str(car) for car in self.cars if not car.is_sold]
