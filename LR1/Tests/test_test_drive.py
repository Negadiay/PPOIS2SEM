import unittest
from car import Car
from customer import Customer
from salesperson import Salesperson
from test_drive import TestDrive

class TestTestDrive(unittest.TestCase):
    def setUp(self):
      
        self.car = Car("Toyota", "Camry", 2022, 30000)
        self.customer = Customer("Иван Иванов", "+7 900 123-45-67")
        self.salesperson = Salesperson("Анна Смирнова")
        self.test_drive = TestDrive(self.car, self.customer, self.salesperson)

    def test_conduct(self):
        
        expected_output = f"{self.customer.name} is test-driving {self.car} with {self.salesperson.name}."
        self.assertEqual(self.test_drive.conduct(), expected_output)

if __name__ == "__main__":
    unittest.main()
