import unittest
from models.Customer import Customer
from models.Coffee import Coffee
from models.Order import Order

class TestOrder(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Alice")
        self.coffee = Coffee("Latte")

    def test_order_initialization(self):
        order = Order(self.customer, self.coffee, 5.0)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, self.coffee)
        self.assertEqual(order.price, 5.0)

    def test_invalid_customer(self):
        with self.assertRaises(TypeError):
            Order("NotACustomer", self.coffee, 4.0)

    def test_invalid_coffee(self):
        with self.assertRaises(TypeError):
            Order(self.customer, "NotACoffee", 4.0)

    def test_invalid_price_type(self):
        with self.assertRaises(TypeError):
            Order(self.customer, self.coffee, "free")

    def test_price_out_of_range(self):
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 0.5)  # Too low

        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 11.0)  # Too high

    def test_price_is_float(self):
        order = Order(self.customer, self.coffee, 7)
        self.assertIsInstance(order.price, float)
        self.assertEqual(order.price, 7.0)

    def test_repr(self):
        order = Order(self.customer, self.coffee, 5.5)
        expected = "Order(customer=Alice, coffee=Latte, price=5.5)"
        self.assertEqual(repr(order), expected)

if __name__ == '__main__':
    unittest.main()