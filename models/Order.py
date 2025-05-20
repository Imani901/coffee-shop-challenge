
from .Customer import Customer  # Importing ON GLOBAL to avoid circular dependency
from .Coffee import Coffee     

class Order:
    def __init__(self, customer, coffee, price):
        self._customer = self._validate_customer(customer)
        self._coffee = self._validate_coffee(coffee)
        self._price = self._validate_price(price)

    @property
    def customer(self):
        return self._customer

    def _validate_customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("Order must be associated with a Customer instance.")
        return customer

    @property
    def coffee(self):
        return self._coffee

    def _validate_coffee(self, coffee):
        if not isinstance(coffee, Coffee):
            raise TypeError("Order must include a Coffee instance.")
        return coffee

    @property
    def price(self):
        return self._price

    def _validate_price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number.")
        if not 1.0 <= price <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0.")
        return float(price)

    def __repr__(self):
        return f"Order(customer={self.customer.name}, coffee={self.coffee.name}, price={self.price})"