import unittest
from models.Customer import Customer
from models.Coffee import Coffee
from models.Order import Order

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Alice")
        self.coffee1 = Coffee("Latte")
        self.coffee2 = Coffee("Espresso")

    def test_customer_initialization(self):
        self.assertEqual(self.customer.name, "Alice")
        self.assertEqual(self.customer.orders(), [])

    def test_name_validation(self):
        with self.assertRaises(TypeError):
            Customer(123)

        with self.assertRaises(ValueError):
            Customer("")  # Too short

        with self.assertRaises(ValueError):
            Customer("A" * 16)  # Too long

    def test_name_setter(self):
        self.customer.name = "Bob"
        self.assertEqual(self.customer.name, "Bob")

        with self.assertRaises(ValueError):
            self.customer.name = ""  # Invalid

    def test_create_order(self):
        order = self.customer.create_order(self.coffee1, 4.5)
        self.assertIn(order, self.customer.orders())
        self.assertIn(order, self.coffee1.orders())
        self.assertEqual(order.price, 4.5)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, self.coffee1)

    def test_coffees(self):
        self.customer.create_order(self.coffee1, 4.5)
        self.customer.create_order(self.coffee2, 3.0)
        self.customer.create_order(self.coffee1, 5.0)

        coffees = self.customer.coffees()
        self.assertIn(self.coffee1, coffees)
        self.assertIn(self.coffee2, coffees)
        self.assertEqual(len(coffees), 2)

    def test_most_aficionado(self):
        customer2 = Customer("Bob")
        customer3 = Customer("Charlie")

        customer2.create_order(self.coffee1, 4.0)
        customer2.create_order(self.coffee1, 6.0)
        customer3.create_order(self.coffee1, 7.0)

        aficionado = Customer.most_aficionado(self.coffee1)
        self.assertEqual(aficionado, customer2)  # Bob spent 10, Charlie 7

    def test_repr(self):
        self.assertEqual(repr(self.customer), "Customer(name='Alice')")

if __name__ == '__main__':
    unittest.main()