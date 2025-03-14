import unittest
from car import Car
from showroom import Showroom

class TestShowroom(unittest.TestCase):
    def setUp(self):
        self.showroom = Showroom()
        self.car1 = Car("Toyota", "Camry", 2022, 30000)
        self.car2 = Car("Honda", "Civic", 2021, 25000)
        self.car3 = Car("BMW", "X5", 2023, 60000)

    def test_add_car(self):
        self.showroom.add_car(self.car1)
        self.assertIn(self.car1, self.showroom.cars)

    def test_list_cars(self):
        
        self.showroom.add_car(self.car1)
        self.showroom.add_car(self.car2)
        self.car2.is_sold = True  

        expected_list = [str(self.car1)]  
        self.assertEqual(self.showroom.list_cars(), expected_list)

    def test_list_cars_empty(self):
        
        self.showroom.add_car(self.car1)
        self.showroom.add_car(self.car2)

        self.car1.is_sold = True
        self.car2.is_sold = True  

        self.assertEqual(self.showroom.list_cars(), [])

if __name__ == "__main__":
    unittest.main()
