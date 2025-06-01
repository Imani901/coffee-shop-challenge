
class Coffee:
    def __init__(self, name):
        self._name = self._validate_name(name)
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = self._validate_name(new_name)

    def _validate_name(self, name):
        if not isinstance(name, str):
            raise TypeError("Coffee name must be a string.")
        if not len(name) >= 3:
            raise ValueError("Coffee name must be at least 3 characters long.")
        return name

    def _add_order(self, order):
        self._orders.append(order)

    def orders(self):
        return list(self._orders)

    def customers(self):
        return list(set(order.customer for order in self._orders))

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0.0
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders)

    def __repr__(self): #returning string that represents the obj
        return f"Coffee(name='{self.name}')"