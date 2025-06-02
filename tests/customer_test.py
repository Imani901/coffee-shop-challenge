import unittest
from models.customer import Customer
from models.coffee import Coffee

class TestCustomer(unittest.TestCase):

    def test_valid_name(self):
        c = Customer("Milly")
        self.assertEqual(c.name, "Milly")

    def test_invalid_name_type(self):
        with self.assertRaises(ValueError):
            Customer(123)

    def test_invalid_name_length(self):
        with self.assertRaises(ValueError):
            Customer("A" * 16)

    def test_create_order_and_coffees(self):
        c = Customer("Sam")
        coffee = Coffee("Espresso")
        c.create_order(coffee, 3.5)
        self.assertEqual(len(c.orders()), 1)
        self.assertEqual(c.coffees(), [coffee])