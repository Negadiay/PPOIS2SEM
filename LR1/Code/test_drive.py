from car import Car
from customer import Customer
from salesperson import Salesperson

class TestDrive:
    def __init__(self, car, customer, salesperson):
        self.car = car
        self.customer = customer
        self.salesperson = salesperson

    def conduct(self):
        return f"{self.customer.name} is test-driving {self.car} with {self.salesperson.name}."
