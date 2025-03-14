import unittest
from customer import Customer 

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Иван Иванов", "+7 900 123-45-67")

    def test_customer_creation(self):
        self.assertEqual(self.customer.name, "Иван Иванов")
        self.assertEqual(self.customer.phone, "+7 900 123-45-67")

    def test_customer_str(self):
        expected_output = "Customer: Иван Иванов, Phone: +7 900 123-45-67"
        self.assertEqual(str(self.customer), expected_output)

if __name__ == "__main__":
    unittest.main()
