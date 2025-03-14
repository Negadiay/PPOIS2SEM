import unittest
from car import Car  

class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car("Toyota", "Camry", 2022, 30000)

    def test_car_creation(self):
        self.assertEqual(self.car.make, "Toyota")
        self.assertEqual(self.car.model, "Camry")
        self.assertEqual(self.car.year, 2022)
        self.assertEqual(self.car.price, 30000)
        self.assertFalse(self.car.is_sold)
        self.assertFalse(self.car.is_prepared)

    def test_car_str(self):
        expected_output = "Toyota Camry 2022 - $30000 (Not Prepared)"
        self.assertEqual(str(self.car), expected_output)

    def test_prepare_for_sale(self):
        self.car.prepare_for_sale()
        self.assertTrue(self.car.is_prepared)
        expected_output = "Toyota Camry 2022 - $30000 (Prepared) has been prepared for sale."
        self.assertEqual(self.car.prepare_for_sale(), expected_output)

if __name__ == "__main__":
    unittest.main()
