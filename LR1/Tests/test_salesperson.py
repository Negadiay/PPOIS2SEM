import unittest
from salesperson import Salesperson
from car import Car
from customer import Customer

class TestSalesperson(unittest.TestCase):
    def setUp(self):
        self.salesperson = Salesperson("Анна Смирнова")
        self.car = Car("Toyota", "Camry", 2022, 30000)
        self.customer = Customer("Иван Иванов", "+7 900 123-45-67")

    def test_salesperson_creation(self):
        self.assertEqual(self.salesperson.name, "Анна Смирнова")

    def test_sell_car_not_prepared(self):
        result = self.salesperson.sell_car(self.car, self.customer)
        expected_output = f"Car {self.car} is not prepared for sale. Please prepare it first."
        self.assertEqual(result, expected_output)
        self.assertFalse(self.car.is_sold)

    def test_sell_car_already_sold(self):
        self.car.prepare_for_sale()  # Подготавливаем машину к продаже
        self.car.is_sold = True  # Помечаем её как проданную
        result = self.salesperson.sell_car(self.car, self.customer)
        expected_output = f"Car {self.car} is already sold."
        self.assertEqual(result, expected_output)

    def test_successful_sell_car(self):
        self.car.prepare_for_sale()  # Подготавливаем машину к продаже
        result = self.salesperson.sell_car(self.car, self.customer)
        expected_output = f"Анна Смирнова sold {self.car} to Иван Иванов."
        self.assertEqual(result, expected_output)
        self.assertTrue(self.car.is_sold)

    def test_provide_info(self):
        self.assertEqual(self.salesperson.provide_info(self.car), str(self.car))

if __name__ == "__main__":
    unittest.main()
