import unittest
from models.order import Order
from models.customer import Customer
from models.coffee import Coffee

class TestOrder(unittest.TestCase):

    def test_valid_order(self):
        customer = Customer("Anna")
        coffee = Coffee("Mocha")
        order = Order(customer, coffee, 5.0)
        self.assertEqual(order.customer, customer)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 5.0)

    def test_invalid_price(self):
        customer = Customer("Tom")
        coffee = Coffee("Americano")
        with self.assertRaises(ValueError):
            Order(customer, coffee, 15.0)

    def test_invalid_customer_type(self):
        coffee = Coffee("Flat White")
        with self.assertRaises(TypeError):
            Order("not a customer", coffee, 4.0)

    def test_invalid_coffee_type(self):
        customer = Customer("Ella")
        with self.assertRaises(TypeError):
            Order(customer, "not coffee", 3.5)