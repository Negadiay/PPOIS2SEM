import unittest
from car import Car
from service import Service

class TestService(unittest.TestCase):
    def setUp(self):
        
        self.car = Car("Toyota", "Camry", 2022, 30000)
        self.service = Service(self.car)

    def test_perform_service(self):
        
        expected_output = f"Service completed for {self.car}."
        self.assertEqual(self.service.perform_service(), expected_output)

if __name__ == "__main__":
    unittest.main()
