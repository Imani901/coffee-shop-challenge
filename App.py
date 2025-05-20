# debug.py
from models.Customer import Customer
from models.Coffee import Coffee
from models.Order import Order

if __name__ == "__main__":
    # customers
    customer1 = Customer("Alice")
    customer2 = Customer("Bobby")
    customer3 = Customer("Charlie")

    # coffees
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Cappuccino")
    coffee3 = Coffee("Espresso")

    # orders
    order1 = customer1.create_order(coffee1, 4.5)
    order2 = customer1.create_order(coffee2, 5.0)
    order3 = customer2.create_order(coffee1, 4.0)
    order4 = customer3.create_order(coffee3, 3.5)
    order5 = customer3.create_order(coffee1, 4.5)
    order6 = customer1.create_order(coffee3, 3.0)
    order7 = customer2.create_order(coffee2, 5.5)

    # relationships
    print("\nRelationships:")
    print(f"{customer1.name}'s orders: {customer1.orders()}")
    print(f"{coffee1.name}'s orders: {coffee1.orders()}")
    print(f"{order1} belongs to {order1.customer.name} and ordered {order1.coffee.name} for ${order1.price}")
    print(f"{coffee1.name} was ordered by: {coffee1.customers()}")
    print(f"{customer3.name} ordered: {customer3.coffees()}")

    # aggregate methods
    print("\nAggregates:")
    print(f"{coffee1.name} has been ordered {coffee1.num_orders()} times.")
    print(f"Average price of {coffee2.name}: ${coffee2.average_price():.2f}")

    # most_aficionado class method
    print("\nMost Aficionado:")
    most_loyal_latte_drinker = Customer.most_aficionado(coffee1)
    if most_loyal_latte_drinker:
        print(f"The most aficionado for {coffee1.name} is: {most_loyal_latte_drinker.name}")
    else:
        print(f"No orders for {coffee1.name} yet.")

    most_loyal_espresso_drinker = Customer.most_aficionado(coffee3)
    if most_loyal_espresso_drinker:
        print(f"The most aficionado for {coffee3.name} is: {most_loyal_espresso_drinker.name}")
    else:
        print(f"No orders for {coffee3.name} yet.")