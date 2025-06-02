import unittest
from models.coffee import Coffee
from models.customer import Customer

class TestCoffee(unittest.TestCase):

    def test_valid_name(self):
        c = Coffee("Latte")
        self.assertEqual(c.name, "Latte")

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            Coffee("Hi")

    def test_num_orders_and_avg_price(self):
        coffee = Coffee("Cappuccino")
        cust = Customer("John")
        cust.create_order(coffee, 2.0)
        cust.create_order(coffee, 4.0)
        self.assertEqual(coffee.num_orders(), 2)
        self.assertAlmostEqual(coffee.average_price(), 3.0)