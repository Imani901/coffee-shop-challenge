import unittest
from models.Coffee import Coffee
from models.Order import Order
from models.Customer import Customer

class TestCoffee(unittest.TestCase):

    def setUp(self):
        self.coffee = Coffee("Latte")
        self.customer1 = Customer("Alice")
        self.customer2 = Customer("Bob")

    def test_coffee_initialization(self):
        self.assertEqual(self.coffee.name, "Latte")
        self.assertEqual(self.coffee.orders(), [])
        self.assertEqual(self.coffee.num_orders(), 0)

    def test_name_validation(self):
        with self.assertRaises(TypeError):
            Coffee(123)
        with self.assertRaises(ValueError):
            Coffee("A")

    def test_name_setter(self):
        self.coffee.name = "Cappuccino"
        self.assertEqual(self.coffee.name, "Cappuccino")

        with self.assertRaises(ValueError):
            self.coffee.name = "ab"

    def test_add_order_and_order_list(self):
        order1 = self.customer1.create_order(self.coffee, 4.0)
        order2 = self.customer2.create_order(self.coffee, 5.0)

        self.assertEqual(len(self.coffee.orders()), 2)
        self.assertIn(order1, self.coffee.orders())
        self.assertIn(order2, self.coffee.orders())

    def test_customers_list(self):
        self.customer1.create_order(self.coffee, 4.0)
        self.customer2.create_order(self.coffee, 5.0)
        self.customer1.create_order(self.coffee, 6.0)

        customers = self.coffee.customers()
        self.assertIn(self.customer1, customers)
        self.assertIn(self.customer2, customers)
        self.assertEqual(len(customers), 2)

    def test_num_orders(self):
        self.assertEqual(self.coffee.num_orders(), 0)
        self.customer1.create_order(self.coffee, 4.0)
        self.assertEqual(self.coffee.num_orders(), 1)

    def test_average_price(self):
        self.assertEqual(self.coffee.average_price(), 0.0)
        self.customer1.create_order(self.coffee, 4.0)
        self.customer2.create_order(self.coffee, 6.0)
        self.assertEqual(self.coffee.average_price(), 5.0)

    def test_repr(self):
        self.assertEqual(repr(self.coffee), "Coffee(name='Latte')")

if __name__ == '__main__':
    unittest.main()