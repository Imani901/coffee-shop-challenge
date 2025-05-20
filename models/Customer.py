
class Customer:
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
            raise TypeError("Customer name must be a string.")
        if not 1 <= len(name) <= 15:
            raise ValueError("Customer name must be between 1 and 15 characters long.")
        return name

    def create_order(self, coffee, price):
        from .Order import Order  # Avoiding Circular Imports
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee._add_order(order)  
        return order

    def orders(self):
        return list(self._orders)

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    @classmethod #operates on the class
    def most_aficionado(cls, coffee):
        aficionado = None
        max_spent = 0
        customer_spending = {}

        #loop through oders for given coffe
        for order in coffee.orders():
            customer = order.customer
            price = order.price
            customer_spending[customer] = customer_spending.get(customer, 0) + price
            
        # Determine the customer who spent the most
        for customer, total_spent in customer_spending.items():
            if total_spent > max_spent:
                max_spent = total_spent
                aficionado = customer

        return aficionado

    #returning string that represents the obj
    def __repr__(self):
        return f"Customer(name='{self.name}')"