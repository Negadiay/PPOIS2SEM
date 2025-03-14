from car import Car
from customer import Customer

class Salesperson:
    def __init__(self, name):
        self.name = name

    def sell_car(self, car, customer):
        if car.is_sold:
            return f"Car {car} is already sold."
        if not car.is_prepared:
            return f"Car {car} is not prepared for sale. Please prepare it first."
        car.is_sold = True
        return f"{self.name} sold {car} to {customer.name}."

    def provide_info(self, car):
        return str(car)
